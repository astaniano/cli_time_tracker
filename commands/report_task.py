import json
from datetime import datetime

from dal import get_data
from constants import task_finish_key, task_in_progress, task_name_key, task_start_key, show_names_only

def handle_report(cli_args):
    all_tasks = get_data()

    if len(all_tasks) < 1:
        print("[]")
        return

    last_task = all_tasks[-1]

    if last_task[task_finish_key] == task_in_progress:
        raise Exception('please stop your task first')

    report = {}
    placeholder_for_a_date = datetime.fromisoformat("2022-11-03T23:16:36.721321")
    total_time_on_all_tasks = placeholder_for_a_date

    for task in all_tasks:
        start_date = datetime.fromisoformat(task[task_start_key])
        end_date = datetime.fromisoformat(task[task_finish_key])
        time_spent_in_current_record = end_date - start_date
        total_time_on_all_tasks = total_time_on_all_tasks + time_spent_in_current_record
                
        task_name = task[task_name_key]

        if task_name in report:
            already_spent_time = report[task_name]
            total_time_on_task = already_spent_time + time_spent_in_current_record
        else:
            total_time_on_task = time_spent_in_current_record
            
        report[task_name] = total_time_on_task

    total_time_on_all_tasks = total_time_on_all_tasks - placeholder_for_a_date

    # check if there are any additional flags
    if len(cli_args) > 2:
        report_flag = cli_args[2]
        if report_flag == show_names_only:
            print()
            for task_name in report:
                print(task_name)
            print()
            return

    # format the default output
    formatted_report = {}

    for key in report:
        formatted_report[key] = f'{report[key]}'

    print(json.dumps(formatted_report, sort_keys=False, indent=2))
    print(f'total_time_spent: {total_time_on_all_tasks}')
