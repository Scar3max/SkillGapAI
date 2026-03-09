from typing import Dict, List
from sqlalchemy.orm import Session

from app.models.user_skill import UserSkill
from app.models.role import Role
from app.models.role_skill import RoleSkill
from app.models.career_prediction import CareerPrediction

# ------------------------
# Configuration constants
# ------------------------

MAX_CONFIDENCE = 4
REQUIRED_CONFIDENCE = 3
IMPROVEMENT_THRESHOLD = 2
PENALTY_LAMBDA = 0.05





# ------------------------
# Public entry point
# ------------------------

def analyze_user_career_fit(
    db: Session,
    user_id: int
)->int:

    user_skills = _get_user_skills(db, user_id)
    roles = db.query(Role).all()

    eligible_roles = []
    ineligible_roles = []

    for role in roles:
        result = _evaluate_role(
            db=db,
            role=role,
            user_skills=user_skills
        )

        if result["status"] == "INELIGIBLE":
            ineligible_roles.append(result)
        else:
            eligible_roles.append(result)

    eligible_roles.sort(
        key=lambda r: r["final_score"],
        reverse=True
    )
    prediction_payload={
        "ranked_roles":[
            {
                "Role_id":r["role_id"],
                "Role_name":r["role_name"],
                "Role_domain":r["domain"],
                "Description":r["description"]
            }
            for r in eligible_roles
        ]
    }
    evaluation_payload={
        "eligible_roles": eligible_roles,
        "ineligible_roles": ineligible_roles,
        "model_version": "rule_based_engine"
    }
    evaluated_prediction=CareerPrediction(user_id=user_id,model_version="Evaluation Engine",prediction_payload=prediction_payload,explanation_payload=evaluation_payload)
    db.add(evaluated_prediction)
    db.flush()
    return evaluated_prediction.id
    # return {
    #     "user_id": user_id,
    #     "eligible_roles": eligible_roles,
    #     "ineligible_roles": ineligible_roles
    # }


# ------------------------
# Core role evaluation
# ------------------------

def _evaluate_role(
    db: Session,
    role: Role,
    user_skills: Dict[int, int]
) -> dict:

    role_skills: List[RoleSkill] = (
        db.query(RoleSkill)
        .filter(RoleSkill.role_id == role.id)
        .all()
    )

    # ---- Step 0: mandatory skill check ----

    missing_mandatory = []

    for rs in role_skills:
        if rs.is_mandatory:
            user_conf = user_skills.get(rs.skill_id, 0)
            if user_conf == 0:
                missing_mandatory.append(rs.skill.name)

    if missing_mandatory:
        return {
            "role_id": role.id,
            "role_name": role.name,
            "status": "INELIGIBLE",
            "reason": "Missing mandatory skills",
            "missing_mandatory_skills": missing_mandatory
        }

    # ---- Step 1–4: scoring & gap detection ----

    raw_score = 0.0
    max_score = 0.0
    penalty = 0.0
    skill_gaps = []

    for rs in role_skills:
        importance = rs.importance_weight
        max_score += importance

        user_conf = user_skills.get(rs.skill_id, 0)
        normalized_conf = user_conf / MAX_CONFIDENCE

        # accumulate weighted score
        raw_score += normalized_conf * importance

        # ---- Gap Classification ----

        gap_type = None

        if user_conf == 0:
            gap_type = "MISSING"

        elif user_conf < IMPROVEMENT_THRESHOLD:
            gap_type = "CRITICAL"

        elif user_conf < REQUIRED_CONFIDENCE:
            gap_type = "IMPROVEMENT"

        if gap_type:
            skill_gaps.append({
                "skill_id": rs.skill_id,
                "skill_name": rs.skill.name,
                "current_level": user_conf,
                "importance_weight": importance,
                "gap_type": gap_type
            })

        # ---- Smooth penalty scaling ----
        if user_conf < REQUIRED_CONFIDENCE:
            weakness_ratio = (REQUIRED_CONFIDENCE - user_conf) / REQUIRED_CONFIDENCE
            penalty += weakness_ratio * importance

    # ---- Final scoring ----

    base_score = raw_score / max_score if max_score > 0 else 0
    final_score = base_score * max(0, (1 - PENALTY_LAMBDA * penalty))
    final_score = max(final_score, 0.0)

    # ---- Fit level classification ----

    if final_score >= 0.75:
        fit_level = "STRONG_MATCH"
    elif final_score >= 0.5:
        fit_level = "MODERATE_MATCH"
    elif final_score >= 0.3:
        fit_level = "WEAK_MATCH"
    else:
        fit_level = "POOR_MATCH"

    return {
        "role_id": role.id,
        "role_name": role.name,
        "status": "ELIGIBLE",
        "fit_level": fit_level,
        "base_score": round(base_score, 4),
        "final_score": round(final_score, 4),
        "skill_gaps": skill_gaps
    }


# ------------------------
# Data helpers
# ------------------------

def _get_user_skills(
    db: Session,
    user_id: int
) -> Dict[int, int]:

    rows = (
        db.query(UserSkill.skill_id, UserSkill.confidence_level)
        .filter(UserSkill.user_id == user_id)
        .all()
    )

    return {skill_id: confidence for skill_id, confidence in rows}