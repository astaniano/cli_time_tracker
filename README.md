## Simple CLI time tracker

### In order to use the tracker please do the following:
- create `logs` folder in the same folder that `main.py` is located in
- create `.env` file in the same folder that `main.py` is located in (see `.env.example` for an example)

### Usage:
```bash
# create a new log file
python3 main.py new

# start a new task
python3 main.py run <task name>

# stop the last task
python3 main.py stop

# list all the tasks
# please note this command can only be run if there is no other task currently in progress
# in other words you need to run `python3 main.py stop` before running `ls` command
python3 main.py ls
```

### Optional:
Inside of ~/.bashrc OR ~/.zshrc add the following line:
```
alias t="python3 <path_to_the_folder_where_this_code_resides>/cli_time_tracker/main.py"
```
e.g.:
```
alias t="python3 /Users/<user_name>/programming/cli_time_tracker/main.py"
```
