import json
import logging


LOADTASKSERROR = "Could not load old list of tasks. Created an empty list."
PATHTOTASKS = './tasks.json'


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