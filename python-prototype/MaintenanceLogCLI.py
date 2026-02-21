import json
import logging
from datetime import date
import questionary


LOADTASKSERROR = "Could not load old list of tasks. Created an empty list."
PATHTOTASKS = './tasks.json'


def get_content():
    while True:
        try:
            content = input("Enter your task: ")
            if not content.strip():
                raise ValueError("Received empty string.")
        except ValueError as e:
            print(e)
        else:
            return content


def parse_date(date_string):
    try:
        day, month, year = date_string.split("/")
        day, month, year = int(day), int(month), int(year)
        return day, month, year
    except Exception as e:
        logging.error(e)


def get_date():
    pass


def create_task():
    content = get_content()


def load_tasks():
    """Load tasks from the JSON file at PATHTOTASKS.

        Returns:
            list: A list of tasks loaded from the file, or an empty list if the
                file does not exist.
    """
    tasks = []
    try:
        with open(PATHTOTASKS) as f:
            tasks = json.load(f)
    except Exception as e:
        logging.error(e)
        print(LOADTASKSERROR)
    return tasks


def main():
    pass


if __name__ == '__main__':
    main()