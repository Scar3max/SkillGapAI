from backend.app.events.bus import event_bus
from fastapi import Depends,APIRouter
from backend.app.events.career_events import CareerAnalysisRequested
from pydantic import BaseModel
from sqlalchemy.orm import Session
from backend.app.core.database import get_db
class AnalysisDetails(BaseModel):
    id:int

router=APIRouter()

@router.post('/requested')
def generate_analysis(user:AnalysisDetails,db:Session=Depends(get_db)):
    print("Publishing UserSkillUpdated event")
    event_bus.publish(CareerAnalysisRequested(user.id,db),db=db)
    
