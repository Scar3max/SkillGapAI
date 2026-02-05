from app.core.database import Base
from sqlalchemy import Column,BigInteger,Integer,TIMESTAMP,String,func,ForeignKey,CheckConstraint,UniqueConstraint
from sqlalchemy.dialects.mysql import TINYINT

class UserSkill(Base):
    __tablename__="user_skills"
    id=Column(BigInteger,nullable=False,primary_key=True,autoincrement=True)
    user_id=Column(BigInteger,ForeignKey("users.id",onupdate="CASCADE",ondelete="RESTRICT"),nullable=False)
    skill_id=Column(Integer,ForeignKey("skills.id",ondelete="RESTRICT",onupdate="CASCADE"),nullable=False)
    confidence_level=Column(TINYINT,nullable=False)
    updated_at=Column(TIMESTAMP,server_default=func.now(),onupdate=func.now(),nullable=False)

    __table_args__=(
        UniqueConstraint(
            "user_id","skill_id",
            name="uq_user_skills_user_id_skill_id"
        ),
        CheckConstraint(
            "confidence_level BETWEEN 0 AND 4",
            name="user_skills_chk_1"
        ),
    )
