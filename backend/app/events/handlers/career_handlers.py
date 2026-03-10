from backend.app.events.user_events import UserSkillUpdated
from backend.app.events.career_events import CareerAnalysisRequested,CareerAnalysisGenerated
from backend.app.services.career_analysis_engine import analyze_user_career_fit
from sqlalchemy.orm import Session
from backend.app.events.bus import event_bus

def handle_user_skill_updated(event: UserSkillUpdated,db):
    event_bus.publish(CareerAnalysisRequested(user_id=event.user_id),db=db)


def handle_career_analysis_requested(event: CareerAnalysisRequested,db:Session):
    print("UserSkillUpdated handler triggered")
    prediction_id=analyze_user_career_fit(db, event.user_id)
    event_bus.publish(CareerAnalysisGenerated(user_id=event.user_id,prediction_id=prediction_id))
    

def handle_career_analysis_generated(event: CareerAnalysisGenerated):
    print(f"Analysis generated for user {event.user_id}, prediction {event.prediction_id}")