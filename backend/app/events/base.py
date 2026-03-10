from dataclasses import dataclass,field
from datetime import datetime

@dataclass
class Event:
    occurred_at: datetime = field(default_factory=datetime.now, init=False)
