import json
from datetime import datetime

from dal import get_data, save_data
from constants import task_finish_key, task_in_progress, task_name_key, task_start_key

def handle_report():
    all_tasks = get_data()

    if len(all_tasks) < 1:
        print("[]")

    last_task = all_tasks[-1]

    if last_task[task_finish_key] == task_in_progress:
        raise Exception('please stop your task first')

    report = {}

    for task in all_tasks:
        start_date = datetime.fromisoformat(task[task_start_key])
        end_date = datetime.fromisoformat(task[task_finish_key])
        time_spent_in_current_record = end_date - start_date
                
        task_name = task[task_name_key]

        if task_name in report:
            already_spent_time = report[task_name]
            total_time_on_task = already_spent_time + time_spent_in_current_record
        else:
            total_time_on_task = time_spent_in_current_record
            
        report[task_name] = total_time_on_task

    formatted_report = {}

    for key in report:
        formatted_report[key] = f'{report[key]}'

    print(json.dumps(formatted_report, sort_keys=False, indent=2))

