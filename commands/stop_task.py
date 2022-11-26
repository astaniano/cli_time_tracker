from datetime import datetime

from dal import get_data, save_data
from constants import task_finish_key, task_in_progress

def handle_stop():
    all_tasks = get_data()

    if len(all_tasks) < 0:
        print('there are no tasks yet')
        return

    last_task = all_tasks[-1]

    if last_task[task_finish_key] != task_in_progress:
        print('the task is already stopped')
        return
    
    last_task[task_finish_key] = datetime.now().isoformat()

    save_data(all_tasks)
