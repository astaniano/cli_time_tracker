import json
import os

def get_path_to_log_file():
   tracker_folder_path = os.environ['ABSOLUTE_PATH_TO_CLI_TRACKER_FOLDER'] 
   log_file_path = os.environ['PATH_TO_LOG_FILE'] 

   return os.path.join(tracker_folder_path, log_file_path)
 

def get_data():
    file_path = get_path_to_log_file()
    with open(file_path, 'r') as opened_file:
        all_tasks = json.load(opened_file)

    return all_tasks
        

def save_data(updated_all_tasks):
    all_tasks_as_json = json.dumps(updated_all_tasks, indent=2)

    file_path = get_path_to_log_file()
    with open(file_path, 'w') as opened_write_file:
        opened_write_file.write(all_tasks_as_json)

