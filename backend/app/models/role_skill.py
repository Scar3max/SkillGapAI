from backend.app.core.database import Base
from sqlalchemy.orm import relationship
from sqlalchemy import Column,BigInteger,Integer,TIMESTAMP,String,func,ForeignKey,Boolean,CheckConstraint,UniqueConstraint
from sqlalchemy.dialects.mysql import TINYINT
class RoleSkill(Base):
    __tablename__='role_skills'
    id=Column(BigInteger,autoincrement=True,primary_key=True,nullable=False)
    role_id=Column(Integer,ForeignKey('roles.id',onupdate='CASCADE',ondelete='RESTRICT'),nullable=False)
    skill_id=Column(Integer,ForeignKey('skills.id',ondelete='RESTRICT',onupdate='CASCADE'),nullable=False)
    importance_weight=Column(TINYINT(unsigned=True),nullable=False)
    is_mandatory=Column(Boolean,nullable=False)

    __table_args__=(
        UniqueConstraint(
            "role_id","skill_id",
            name="skill_id" 
        ),
        CheckConstraint(
            "importance_weight BETWEEN 1 AND 5",
            name="uq_role_skills_role_id_skill_id"
        ),
    )
    role = relationship("Role", back_populates="role_skills")
    skill = relationship("Skill", back_populates="role_skills")
