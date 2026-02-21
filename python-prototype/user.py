from datetime import date


class User:
    def __init__(self, name: str, starship_name = None, log_entries = []):
        self.name = name
        self.starship_name = starship_name
        self.log_entries = log_entries
        self.alert_state = max(log_entry.alert_state for log_entry in
                                   log_entries)
        self.start_date = date.today()