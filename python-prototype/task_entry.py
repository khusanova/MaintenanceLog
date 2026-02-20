from datetime import datetime, timedelta


ALERTS = ['green','yellow', 'red', 'infrared']


class TaskEntry:
    content: str
    frequency: int
    date_last: datetime
    date_next: datetime
    alert_state: int

    def __init__(self, content: str, frequency: int):
        self.content = content
        self.frequency = frequency
        self.date_last = datetime.now()
        self.date_next = datetime.now() + timedelta(days = self.frequency)
        self.alert_state = 0