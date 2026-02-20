from datetime import date, timedelta


class LogEntry:
    ALERTS = ['green', 'yellow', 'red', 'infrared']
    TJD_OFFSET = date(1968, 5, 24).toordinal()

    def __init__(self, content: str, frequency: int, date_last = None):
        self.content = content
        self.frequency = frequency
        if date_last is None:
            date_last = date.today()
        self.date_last = date_last
        self.date_next = self.date_last + timedelta(days=self.frequency)
        if self.date_next >= date.today():
            self._alert_state = 0
        else:
            self._alert_state = 1

    def to_dict(self):
        return {
            "content": self.content,
            "frequency": self.frequency,
            "date_last": self.date_last.toordinal(),
            "date_next": self.date_next.toordinal(),
            "alert_state": self.alert_state
        }

    def postpone_task(self, new_date: date):
        self._alert_state += 1
        self.date_next = new_date

    @property
    def alert_state(self):
        return self.ALERTS[self._alert_state]

    @alert_state.setter
    def alert_state(self, value):
        if type(value) is not int:
            raise TypeError
        if not (0 <= value < 4):
            raise ValueError
        else:
            self._alert_state = value

    @classmethod
    def from_dict(cls, data: dict):
        date_last = date.fromordinal(data['date_last'])
        date_next = date.fromordinal(data['date_next'])
        entry = cls(data['content'], data['frequency'], date_last = date_last)
        entry.date_next = date_next
        return entry

    @staticmethod
    def to_tjd(date_to_convert):
        return date_to_convert.toordinal() - LogEntry.TJD_OFFSET