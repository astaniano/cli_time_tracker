import json
import os

def create_file_if_not_exist():
    if not os.path.exists(get_absolute_path_to_log_file()):
        create_new_log_file()


def create_new_log_file():
    content = '[]'
    with open(get_absolute_path_to_log_file(), 'w') as file:
        file.write(content)


def get_relative_path_to_log_file():
   return os.environ['RELATIVE_PATH_TO_LOG_FILE'] 


def get_absolute_path_to_log_file():
   tracker_folder_path = os.environ['ABSOLUTE_PATH_TO_CLI_TRACKER_FOLDER'] 
   log_file_path = os.environ['RELATIVE_PATH_TO_LOG_FILE'] 

   return os.path.join(tracker_folder_path, log_file_path)
 

def get_data():
    file_path = get_absolute_path_to_log_file()
    with open(file_path, 'r') as opened_file:
        all_tasks = json.load(opened_file)

    return all_tasks


def save_data(updated_all_tasks):
    all_tasks_as_json = json.dumps(updated_all_tasks, indent=2)

    file_path = get_absolute_path_to_log_file()
    with open(file_path, 'w') as opened_write_file:
        opened_write_file.write(all_tasks_as_json)

