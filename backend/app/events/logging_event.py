from dataclasses import dataclass
from app.events.base import Event

@dataclass
class ProgressLogging(Event):
    user_id:int
    roadmap_id:int
    skill_id:int|None
    action_type:str
    name:str="ProgressLogging"