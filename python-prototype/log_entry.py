from datetime import date, timedelta
from constants import ALERTS


class LogEntry:
    TJD_OFFSET = date(1968, 5, 24).toordinal()

    def __init__(self, content: str, frequency: int, date_last=None):
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

    def postpone_task(self, new_date: date):
        self.alert_state += 1
        self.date_next = new_date

    def complete_task(self):
        self.date_last = date.today()
        self.date_next = self.date_last + timedelta(days=self.frequency)
        self.alert_state = 0

    def change_frequency(self, frequency):
        self.frequency = frequency
        self.date_next = self.date_last + timedelta(days=self.frequency)
        if self.date_next >= date.today():
            self.alert_state = 0

    @property
    def frequency(self):
        return self._frequency

    @frequency.setter
    def frequency(self, value):
        if not isinstance(value, int):
            raise TypeError
        if not (0 < value < 3650):
            raise ValueError
        self._frequency = value

    @property
    def date_last(self):
        return self._date_last

    @date_last.setter
    def date_last(self, value):
        if not isinstance(value, date):
            raise TypeError
        if value > date.today():
            raise ValueError("The task completion date is in the future.")
        self._date_last = value

    @property
    def date_next(self):
        return self._date_next

    @date_next.setter
    def date_next(self, value):
        if not isinstance(value, date):
            raise TypeError
        self._date_next = value

    @property
    def alert_state(self):
        return self._alert_state

    @alert_state.setter
    def alert_state(self, value):
        if not isinstance(value, int):
            raise TypeError
        if not (0 <= value < 4):
            raise ValueError
        self._alert_state = value

    @property
    def alert_color(self):
        return ALERTS[self._alert_state]

    @classmethod
    def from_dict(cls, data: dict):
        date_last = date.fromordinal(data['date_last'])
        entry = cls(data['content'], data['frequency'], date_last=date_last)
        entry.date_next = date.fromordinal(data['date_next'])
        entry.alert_state = data['alert_state']
        return entry

    @staticmethod
    def to_tjd(date_to_convert):
        return date_to_convert.toordinal() - LogEntry.TJD_OFFSET