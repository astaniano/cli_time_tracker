This is a simple CLI time tracker

In order to use the tracker please first create .env file (see .env.example)
Create a new json file with the same location and name that was specified in .env file
Then inside of ~/.bashrc OR ~/.zshrc add the following line:
alias tr="python3 <path_to_the_folder_where_this_code_resides>/tracker/main.py"

To start a new task use the following command:
tr run <name_of_the_task>

To stop a new task use:
tr stop

To list all the commands use (please note we can list all the tasks when there are no currently running tasks):
tr ls
