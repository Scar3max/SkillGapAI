from dataclasses import dataclass
from app.events.base import Event

@dataclass
class CareerAnalysisRequested(Event):
    user_id:int
    name:str="CareerAnalysisRequested"

@dataclass
class CareerAnalysisGenerated(Event):
    user_id:int
    prediction_id:int
    name:str="CareerAnalysisGenerated"