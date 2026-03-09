from app.seeds.skills import seed_skills
from app.seeds.roles import seed_roles
from app.seeds.role_skills import seed_role_skills

if __name__ == "__main__":
    seed_skills()
    seed_roles()
    seed_role_skills()