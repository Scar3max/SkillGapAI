from backend.app.core.database import Base
from sqlalchemy import Column,BigInteger,Integer,TIMESTAMP,String,func,Text,ForeignKey,CheckConstraint

class ProgressLog(Base):
    __tablename__='progress_logs'
    id=Column(BigInteger,autoincrement=True,primary_key=True,nullable=False)
    user_id=Column(BigInteger,ForeignKey('users.id',ondelete='RESTRICT',onupdate='CASCADE'),nullable=False)
    roadmap_id=Column(BigInteger,ForeignKey('roadmap_versions.id',ondelete='RESTRICT',onupdate='CASCADE'))
    skill_id=Column(Integer,ForeignKey('skills.id',ondelete='RESTRICT',onupdate='CASCADE'))
    action_type=Column(String(100),nullable=False)
    notes=Column(Text)
    created_at=Column(TIMESTAMP,server_default=func.now(),nullable=False)

    __table_args__=(
        CheckConstraint(
            "(roadmap_id IS NOT NULL) OR (skill_id IS NOT NULL)",
    name="progress_logs_target_chk"
        ),
        CheckConstraint(
    "action_type IN ('task_completed', 'milestone_reached', 'self_reported_improvement')",
    name="progress_logs_action_type_chk"
        ),
    )