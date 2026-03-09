from app.core.database import Base
from sqlalchemy.orm import relationship
from sqlalchemy import Column,BigInteger,Integer,TIMESTAMP,String,func,CheckConstraint
class User(Base):
    __tablename__="users"
    id=Column(BigInteger, primary_key=True,autoincrement=True)
    email=Column(String(255), nullable=False,unique= True)
    password_hash=Column(String(255), nullable=False)
    education_level=Column(String(100))
    years_of_experience=Column(Integer)
    career_interest=Column(String(100))
    created_at=Column(TIMESTAMP,nullable=False,server_default=func.now())
    updated_at=Column(TIMESTAMP,server_default=func.now(),nullable=False,onupdate=func.now())

    __table_args__=(
        CheckConstraint(
            "years_of_experience >= 0", name="user_experience_chk"
        ),
    )

    user_skills = relationship(
        "UserSkill",
        cascade="all, delete-orphan"
    )