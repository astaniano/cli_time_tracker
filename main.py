import sys
import os 

from lib.parse_env_vars import load_env_vars
from lib.commands.new import handle_new
from lib.commands.start import handle_start
from lib.commands.stop import handle_stop
from lib.commands.report import handle_report
from lib.commands.log import handle_log

path_to_current_dir = os.path.dirname(os.path.abspath(__file__))
path_to_env_file = os.path.join(path_to_current_dir, '.env')
load_env_vars(path_to_env_file)

cli_args = sys.argv

if len(cli_args) < 2:
    raise Exception('pls specify your command')

command = cli_args[1]

if command == 'new':
    handle_new()
elif command == 'run':
    handle_start(cli_args)
elif command == 'stop':
    handle_stop()
elif command == 'ls':
    handle_report(cli_args)
elif command == 'log':
    handle_log()
else:
    raise Exception('Unknown command')
