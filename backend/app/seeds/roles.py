from sqlalchemy.orm import Session

from app.core.database import SessionLocal
from app.models.role import Role


# Canonical roles list (keep this stable)
ROLES = [
    {
        "name": "Software Engineer",
        "domain": "Engineering",
        "description": "Builds and maintains software systems and applications."
    },
    {
        "name": "Backend Engineer",
        "domain": "Engineering",
        "description": "Designs server-side logic, databases, and APIs."
    },
    {
        "name": "Frontend Engineer",
        "domain": "Engineering",
        "description": "Builds user-facing interfaces and client-side logic."
    },
    {
        "name": "Data Analyst",
        "domain": "Data",
        "description": "Analyzes data to generate insights and support decisions."
    },
    {
        "name": "Data Scientist",
        "domain": "Data",
        "description": "Applies statistics and machine learning to solve complex problems."
    },
    {
        "name": "Machine Learning Engineer",
        "domain": "ML",
        "description": "Builds and deploys machine learning systems in production."
    },
    {
        "name": "DevOps Engineer",
        "domain": "Cloud",
        "description": "Manages infrastructure, CI/CD pipelines, and system reliability."
    },
    {
        "name": "Product Manager",
        "domain": "Product",
        "description": "Defines product vision, roadmap, and coordinates execution."
    },
    {
        "name": "Business Analyst",
        "domain": "Business",
        "description": "Bridges business needs with data and technical teams."
    },
    {
        "name": "QA Engineer",
        "domain": "Engineering",
        "description": "Ensures software quality through testing and validation."
    },
]


def seed_roles():
    session: Session = SessionLocal()

    inserted = 0
    skipped = 0

    try:
        for role_data in ROLES:
            exists = (
                session.query(Role)
                .filter(Role.name == role_data["name"])
                .first()
            )

            if exists:
                skipped += 1
                continue

            role = Role(
                name=role_data["name"],
                domain=role_data["domain"],
                description=role_data["description"]
            )

            session.add(role)
            inserted += 1

        session.commit()

    except Exception as e:
        session.rollback()
        raise e

    finally:
        session.close()

    print(f"Roles seeding completed | Inserted: {inserted}, Skipped: {skipped}")


if __name__ == "__main__":
    seed_roles()
