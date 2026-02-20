from datetime import date, timedelta


class LogEntry:
    ALERTS = ['green', 'yellow', 'red', 'infrared']
    TJD_OFFSET = date(1968, 05, 24).toordinal()

    def __init__(self, content: str, frequency: int, date_last = None):
        self.content = content
        self.frequency = frequency
        if date_last is None:
            date_last = date.today()
        self.date_last = date_last
        self.date_next = self.date_last + timedelta(days=self.frequency)
        if self.date_next >= date.today():
            self.alert_state = 0
        else:
            self.alert_state = 1

    def to_dict(self):
        return {
            "content": self.content,
            "frequency": self.frequency,
            "date_last": self.date_last.toordinal(),
            "date_next": self.date_next.toordinal(),
            "alert_state": self.alert_state
        }

    def get_alert_state(self):
        return self.ALERTS[self.alert_state]

    @classmethod
    def from_dict(cls, data: dict):
        entry = cls(data['content'], data['frequency'])
        entry.date_last = date.fromordinal(data['date_last'])
        entry.date_next = date.fromordinal(data['date_next'])
        entry.alert_state = data['alert_state']
        return entry

    @staticmethod
    def to_tjd(date_to_convert):
        return date_to_convert.toordinal() - LogEntry.TJD_OFFSET