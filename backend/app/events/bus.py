from typing import Callable, Dict, List, Type
from backend.app.events.base import Event


class EventBus:
    def __init__(self):
        self._subscribers: Dict[Type[Event], List[Callable]] = {}

    def subscribe(self, event_type: Type[Event], handler: Callable):
        if event_type not in self._subscribers:
            self._subscribers[event_type] = []
        self._subscribers[event_type].append(handler)

    def publish(self, event: Event,**kwargs):
        handlers = self._subscribers.get(type(event), [])
        for handler in handlers:
            handler(event,**kwargs)


event_bus=EventBus()