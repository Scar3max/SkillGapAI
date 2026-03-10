from backend.app.events.roadmap_events import RoadmapRequested

def handle_roadmap(event:RoadmapRequested):
    print(f"Roadmap Generated {event}")