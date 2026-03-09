from app.events.user_events import UserSkillUpdated
from app.events.career_events import CareerAnalysisRequested,CareerAnalysisGenerated
from app.services.career_analysis_engine import analyze_user_career_fit
from app.core.database import Session
from app.events.bus import EventBus

def handle_user_skill_updated(event: UserSkillUpdated,db):
    EventBus.publish(EventBus,CareerAnalysisRequested(user_id=event.user_id))


def handle_career_analysis_requested(event: CareerAnalysisRequested,db:Session):
    prediction_id=analyze_user_career_fit(db, event.user_id)
    EventBus.publish(EventBus,CareerAnalysisGenerated(user_id=event.user_id,prediction_id=prediction_id),db)
    

def handle_career_analysis_generated(event: CareerAnalysisGenerated):
    print(f"analysis generated {event}")