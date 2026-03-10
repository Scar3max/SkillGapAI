from dataclasses import dataclass
from datetime import datetime

@dataclass
class Event:
    name: str
    user_id:int
    occurred_at: datetime = datetime.now()