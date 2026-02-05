from sqlalchemy.orm import Session

from app.core.database import SessionLocal
from app.models.skill import Skill


# Canonical skill list (start small, expand later)
SKILLS = [
    # Programming
    {"name": "Python", "category": "Programming"},
    {"name": "Java", "category": "Programming"},
    {"name": "JavaScript", "category": "Programming"},

    # Data
    {"name": "SQL", "category": "Data"},
    {"name": "Data Analysis", "category": "Data"},
    {"name": "Data Visualization", "category": "Data"},

    # Machine Learning
    {"name": "Machine Learning", "category": "ML"},
    {"name": "Deep Learning", "category": "ML"},
    {"name": "Model Evaluation", "category": "ML"},

    # Backend / Systems
    {"name": "REST APIs", "category": "Backend"},
    {"name": "Database Design", "category": "Backend"},

    # Cloud / DevOps
    {"name": "Docker", "category": "Cloud"},
    {"name": "Cloud Basics", "category": "Cloud"},

    # Soft Skills
    {"name": "Communication", "category": "Soft Skills"},
    {"name": "Problem Solving", "category": "Soft Skills"},
]


def seed_skills():
    session: Session = SessionLocal()

    inserted = 0
    skipped = 0

    try:
        for skill_data in SKILLS:
            exists = (
                session.query(Skill)
                .filter(Skill.name == skill_data["name"])
                .first()
            )

            if exists:
                skipped += 1
                continue

            skill = Skill(
                name=skill_data["name"],
                category=skill_data["category"],
                description=None
            )

            session.add(skill)
            inserted += 1

        session.commit()

    except Exception as e:
        session.rollback()
        raise e

    finally:
        session.close()

    print(f"Skills seeding completed | Inserted: {inserted}, Skipped: {skipped}")


if __name__ == "__main__":
    seed_skills()
