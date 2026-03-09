from dataclasses import dataclass
from app.events.base import Event

@dataclass
class CareerAnalysisRequested(Event):
    user_id:int

@dataclass
class CareerAnalysisGenerated(Event):
    user_id:int
    prediction_id:int