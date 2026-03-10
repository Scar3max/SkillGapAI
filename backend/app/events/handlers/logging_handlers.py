from backend.app.events.logging_event import ProgressLogging


def handle_logging(event: ProgressLogging):
    print(f"Progress Logging Handled: {event}")
