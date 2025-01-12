import sys
import os 

from lib.parse_env_vars import load_env_vars
from lib.commands.run import handle_run
from lib.commands.stop import handle_stop
from lib.commands.ls import handle_ls
from lib.commands.log import handle_log
from lib.commands.path import handle_path

path_to_current_dir = os.path.dirname(os.path.abspath(__file__))
path_to_env_file = os.path.join(path_to_current_dir, '.env')
load_env_vars(path_to_env_file)

cli_args = sys.argv

if len(cli_args) < 2:
    raise Exception('pls specify your command')

command = cli_args[1]

if command == 'run':
    handle_run(cli_args)
elif command == 'stop':
    handle_stop()
elif command == 'ls':
    handle_ls(cli_args)
elif command == 'log':
    handle_log()
elif command == 'path':
    handle_path()
else:
    raise Exception('Unknown command')
