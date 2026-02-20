class User:
    def __init__(self, name: str, starship_name = None, log_entries = []):
        self.name = name
        self.starship_name = starship_name
        self.log_entries = log_entries
        