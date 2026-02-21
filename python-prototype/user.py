from datetime import date
from log_entry import LogEntry
from constants import ALERTS


class User:
    def __init__(self, name: str, starship_name = None, log_entries = []):
        self.name = name
        self.starship_name = starship_name
        self.log_entries = log_entries
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
    def ship_alert_color(self):
        today = date.today()
        ship_last_state = 0
        for log_entry in self.log_entries:
            last_state = log_entry.alert_state
            if log_entry.next < today:
                last_state += 1
            if last_state > ship_last_state:
                ship_last_state = last_state
        return ALERTS[ship_last_state]

    @property
    def alert_durations_since_last_update(self):
        today = date.today()
        alert_start_dates = [today for _ in range(len(ALERTS))]
        alert_start_dates[0] = self.date_last_update

        for log_entry in self.log_entries:
            last_state = log_entry.alert_state
            if log_entry.next < alert_start_dates[last_state+1]:
                alert_start_dates[last_state + 1] = log_entry.next

        alert_durations = {ALERTS[i]: alert_start_dates[i+1].toordinal() -
                              alert_start_dates[i].toordinal() for i in
                           range(len(ALERTS)-1)}
        alert_durations[ALERTS[-1]] = today.toordinal() - alert_start_dates[
            -1].toordinal()

        return alert_durations