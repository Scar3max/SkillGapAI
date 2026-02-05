from app.core.database import Base
from sqlalchemy import Column,BigInteger,Integer,TIMESTAMP,Text,String,func

class Skill(Base):
    __tablename__='skills'
    id=Column(Integer,nullable=False,autoincrement=True,primary_key=True)
    name=Column(String(100),nullable=False,unique=True)
    category=Column(String(50))
    description=Column(Text)
