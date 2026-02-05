from sqlalchemy.orm import Session

from app.core.database import SessionLocal
from app.models.role import Role
from app.models.skill import Skill
from app.models.role_skill import RoleSkill


# Role → Skill mapping with weights and mandatory flags
ROLE_SKILL_MAP = {
    "Backend Engineer": [
        ("Python", 5, True),
        ("SQL", 4, True),
        ("Database Design", 4, True),
        ("REST APIs", 5, True),
        ("Docker", 3, False),
        ("Cloud Basics", 3, False),
        ("Problem Solving", 4, False),
        ("Communication", 2, False),
    ],

    "Software Engineer": [
        ("Python", 4, False),
        ("Java", 4, False),
        ("JavaScript", 3, False),
        ("SQL", 3, False),
        ("Problem Solving", 5, True),
        ("Communication", 3, False),
        ("REST APIs", 3, False),
    ],

    "Data Analyst": [
        ("SQL", 5, True),
        ("Data Analysis", 5, True),
        ("Data Visualization", 4, True),
        ("Python", 3, False),
        ("Communication", 4, False),
        ("Problem Solving", 3, False),
    ],

    "Data Scientist": [
        ("Python", 5, True),
        ("Machine Learning", 5, True),
        ("Model Evaluation", 4, True),
        ("SQL", 4, False),
        ("Data Analysis", 4, False),
        ("Communication", 3, False),
        ("Problem Solving", 4, False),
    ],

    "Machine Learning Engineer": [
        ("Python", 5, True),
        ("Machine Learning", 5, True),
        ("Model Evaluation", 4, True),
        ("Deep Learning", 4, False),
        ("Docker", 4, True),
        ("Cloud Basics", 4, False),
        ("Database Design", 3, False),
    ],

    "DevOps Engineer": [
        ("Docker", 5, True),
        ("Cloud Basics", 5, True),
        ("Problem Solving", 4, False),
        ("Database Design", 3, False),
        ("Communication", 3, False),
    ],

    "Product Manager": [
        ("Communication", 5, True),
        ("Problem Solving", 4, True),
        ("Data Analysis", 3, False),
        ("SQL", 2, False),
    ],
}


def seed_role_skills():
    session: Session = SessionLocal()

    inserted = 0
    skipped = 0

    try:
        for role_name, skills in ROLE_SKILL_MAP.items():
            role = session.query(Role).filter(Role.name == role_name).first()
            if not role:
                raise ValueError(f"Role not found: {role_name}")

            for skill_name, weight, mandatory in skills:
                skill = session.query(Skill).filter(Skill.name == skill_name).first()
                if not skill:
                    raise ValueError(f"Skill not found: {skill_name}")

                exists = (
                    session.query(RoleSkill)
                    .filter(
                        RoleSkill.role_id == role.id,
                        RoleSkill.skill_id == skill.id,
                    )
                    .first()
                )

                if exists:
                    skipped += 1
                    continue

                role_skill = RoleSkill(
                    role_id=role.id,
                    skill_id=skill.id,
                    importance_weight=weight,
                    is_mandatory=mandatory,
                )

                session.add(role_skill)
                inserted += 1

        session.commit()

    except Exception as e:
        session.rollback()
        raise e

    finally:
        session.close()

    print(
        f"Role–Skill seeding completed | Inserted: {inserted}, Skipped: {skipped}"
    )


if __name__ == "__main__":
    seed_role_skills()
