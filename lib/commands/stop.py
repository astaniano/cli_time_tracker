from datetime import datetime

from ..dal import get_data, save_data
from ..constants import task_finish_key, task_in_progress

def handle_stop():
    all_tasks = get_data()

    if len(all_tasks) < 0:
        raise Exception('there are no tasks yet')

    last_task = all_tasks[-1]

    if last_task[task_finish_key] != task_in_progress:
        raise Exception('the task is already stopped')
    
    last_task[task_finish_key] = datetime.now().isoformat()

    save_data(all_tasks)

    print('the task has been stopped')
