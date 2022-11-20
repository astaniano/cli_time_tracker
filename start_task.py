import sys
import json
from datetime import datetime

from dal import get_data, save_data
from constants import task_in_progress, task_name_key, task_start_key, task_finish_key

def handle_start():
    if len(sys.argv) < 3:
        raise Exception('please supply the name for the task')

    all_tasks = get_data()

    if len(all_tasks) > 0:
        last_task = all_tasks[-1]
        if last_task[task_finish_key] == task_in_progress:
            raise Exception('please stop previous task before starting the next')

    task_name_from_cli = sys.argv[2]
    
    all_tasks.append({
        task_name_key: task_name_from_cli,
        task_start_key: datetime.now().isoformat(),
        task_finish_key: task_in_progress
    })

    save_data(all_tasks)

