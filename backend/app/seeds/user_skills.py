from app.core.database import SessionLocal
from app.models.user import User
from app.models.skill import Skill
from app.models.user_skill import UserSkill

def seed_user_skills():
    db = SessionLocal()

    # Make sure user exists
    user = db.query(User).filter(User.id == 1).first()
    if not user:
        print("User with id=1 not found. Seed users first.")
        db.close()
        return

    # Define skill -> confidence mapping
    user_skill_data = {
        "Python": 3,
        "SQL": 2,
        "HTML": 4,
        "CSS": 3,
        "JavaScript": 3,
        "Problem Solving": 4
    }

    for skill_name, confidence in user_skill_data.items():
        skill = db.query(Skill).filter(Skill.name == skill_name).first()

        if not skill:
            print(f"Skill '{skill_name}' not found. Skipping.")
            continue

        # Avoid duplicate entries
        existing = (
            db.query(UserSkill)
            .filter(
                UserSkill.user_id == user.id,
                UserSkill.skill_id == skill.id
            )
            .first()
        )

        if existing:
            print(f"User already has skill '{skill_name}'. Skipping.")
            continue

        db.add(
            UserSkill(
                user_id=user.id,
                skill_id=skill.id,
                confidence_level=confidence
            )
        )

    db.commit()
    db.close()
    print("User skills seeded successfully.")


if __name__ == "__main__":
    seed_user_skills()