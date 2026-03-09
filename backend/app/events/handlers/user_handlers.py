from app.events.user_events import UserRegistered

def handle_registration(event:UserRegistered):
    print(f"User is registered {event}")
