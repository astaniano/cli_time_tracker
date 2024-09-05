import os
from ..dal import get_path_to_log_file

def handle_new():
    path_to_log_file = get_path_to_log_file()

    if os.path.exists(path_to_log_file):
        raise Exception(f"The file '{path_to_log_file}' already exists.")

    content = '[]'
    with open(path_to_log_file, 'w') as file:
        file.write(content)

