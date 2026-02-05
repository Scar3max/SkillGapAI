from app.core.database import Base
from sqlalchemy import Column,BigInteger,Integer,TIMESTAMP,String,func,Text
class Role(Base):
    __tablename__='roles'
    id=Column(Integer,nullable=False,primary_key=True,autoincrement=True)
    name=Column(String(100),nullable=False,unique=True)
    domain=Column(String(50))
    description=Column(Text)