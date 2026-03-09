from app.events.bus import EventBus
from app.events.user_events import UserSkillUpdated,UserRegistered
from app.events.roadmap_events import RoadmapRequested
from app.events.career_events import CareerAnalysisGenerated,CareerAnalysisRequested
from app.events.logging_event import ProgressLogging
from app.events.handlers.logging_handlers import handle_logging 
from app.events.handlers.career_handlers import handle_user_skill_updated,handle_career_analysis_generated,handle_career_analysis_requested
from app.events.handlers.roadmap_handlers import handle_roadmap
from app.events.handlers.user_handlers import handle_registration

event_bus = EventBus()

event_bus.subscribe(UserSkillUpdated, handle_user_skill_updated)

event_bus.subscribe(UserRegistered,handle_registration)

event_bus.subscribe(CareerAnalysisRequested,handle_career_analysis_requested)

event_bus.subscribe(CareerAnalysisGenerated,handle_career_analysis_generated)

event_bus.subscribe(RoadmapRequested,handle_roadmap)

event_bus.subscribe(ProgressLogging, handle_logging)