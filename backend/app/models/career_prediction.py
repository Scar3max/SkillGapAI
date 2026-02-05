from app.core.database import Base
from sqlalchemy import Column,BigInteger,Integer,TIMESTAMP,String,func,ForeignKey,JSON

class CareerPrediction(Base):
    __tablename__='career_predictions'
    id=Column(BigInteger,nullable=False,primary_key=True,autoincrement=True)
    user_id=Column(BigInteger,ForeignKey('users.id',ondelete='RESTRICT',onupdate='CASCADE'),nullable=False)
    model_version=Column(String(100),nullable=False)
    prediction_payload=Column(JSON,nullable=False)
    explanation_payload=Column(JSON)
    created_at=Column(TIMESTAMP,server_default=func.now(),nullable=False)