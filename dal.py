import json
import os

file_path = os.environ['ABSOLUTE_PATH_TO_LOG_FILE']

def get_data():
    with open(file_path, 'r') as openfile:
        all_tasks = json.load(openfile)

    return all_tasks
        

def save_data(updated_all_tasks):
    all_tasks_as_json = json.dumps(updated_all_tasks, indent=2)

    with open(file_path, 'w') as opened_write_file:
        opened_write_file.write(all_tasks_as_json)

