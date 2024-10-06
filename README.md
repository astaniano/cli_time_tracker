## Simple CLI time tracker

### In order to use the tracker please do the following:
- create `logs` folder in the same folder that `main.py` is located in
- create `.env` file in the same folder that `main.py` is located in (see `.env.example` for an example)

### Usage:
Create a new log file (based on the name specified in the RELATIVE_PATH_TO_LOG_FILE env var)
```bash
python3 main.py new
```

Start a new task
```bash
python3 main.py run task_name
```

Stop the last task
```bash
python3 main.py stop
```

list all the tasks  
please note this command can only be run if there is no other task currently in progress  
in other words you need to run `python3 main.py stop` before running `ls` command
```bash
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
