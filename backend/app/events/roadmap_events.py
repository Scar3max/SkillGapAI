from dataclasses import dataclass
from backend.app.events.base import Event

@dataclass
class RoadmapRequested(Event):
    user_id:int
    prediction_id:int
    predicted_role_id:int
    name:str="RoadmapRequested"