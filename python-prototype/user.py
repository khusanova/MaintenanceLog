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

    def update_status(self):
        today_ordinal = date.today().toordinal()
        alert_state_duration = max(today_ordinal -
                                   log_entry.date_next.toordinal() for
                                   log_entry in self.log_entries)
        self.distance += (today_ordinal - self.date_last_update.toordinal() -
                          alert_state_duration)
        self.date_last_update = date.today()

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