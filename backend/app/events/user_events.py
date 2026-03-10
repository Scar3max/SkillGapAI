from dataclasses import dataclass
from backend.app.events.base import Event

@dataclass
class UserSkillUpdated(Event):
    skill_id: int
    new_confidence: int

@dataclass
class UserRegistered(Event):
    user_id:int