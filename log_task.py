import json

from dal import get_data

def handle_log():
    all_tasks = get_data()

    print(json.dumps(all_tasks, indent=2))
