from dataclasses import dataclass
from app.events.base import Event

@dataclass
class UserSkillUpdated(Event):
    user_id: int
    skill_id: int
    new_confidence: int

@dataclass
class UserRegistered(Event):
    user_id: int