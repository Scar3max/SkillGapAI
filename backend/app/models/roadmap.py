from backend.app.core.database import Base
from sqlalchemy import Column,BigInteger,Integer,TIMESTAMP,String,func,JSON,ForeignKey

class RoadmapVersion(Base):
    __tablename__='roadmap_versions'
    id=Column(BigInteger,nullable=False,autoincrement=True,primary_key=True)
    user_id=Column(BigInteger,ForeignKey('users.id',ondelete='RESTRICT',onupdate='CASCADE'),nullable=False)
    role_id=Column(Integer,ForeignKey('roles.id',ondelete='RESTRICT',onupdate='CASCADE'),nullable=False)
    roadmap_payload=Column(JSON,nullable=False)
    created_at=Column(TIMESTAMP,server_default=func.now(),nullable=False)


