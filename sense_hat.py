# sense_hat.py

mapping_event_command = {
    "left": "LEFT",
    "down": "REV",
    "right": "RIGHT",
    "up": "FWD",
    "middle": "STOP"
}

class MockStick:
    def __init__(self, events):
        self._events = events

    def get_events(self):
        for event in self._events:
            yield event

class SenseHat:
    def __init__(self, events=None):
        if events is None:
            events = []
        self.stick = MockStick(events)
