from datetime import date
from log_entry import LogEntry
from constants import ALERTS


class User:
    def __init__(self, name: str, starship_name = None, log_entries = []):
        self.name = name
        self.starship_name = starship_name
        self.log_entries = log_entries
        self.alert_state = max(log_entry.alert_state for log_entry in
                                   log_entries)
        self.start_date = date.today()
        self.date_last_update = date.today()
        self.distance = 0

    @property
    def log_entries(self):
        return self._log_entries

    @log_entries.setter
    def log_entries(self, value):
        if not isinstance(value, list):
            raise TypeError
        if not all(isinstance(x, LogEntry) for x in value):
            raise TypeError
        self._log_entries = value

    @property
    def alert_color(self):
        return ALERTS[self.alert_state]