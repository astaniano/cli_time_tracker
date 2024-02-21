import sys

from parse_env_vars import load_env_vars
load_env_vars()

from commands.start_task import handle_start
from commands.stop_task import handle_stop
from commands.report_task import handle_report
from commands.log_task import handle_log

cli_args = sys.argv

if len(cli_args) < 2:
    raise Exception('pls specify your command')

command = cli_args[1]

if command == 'str':
    handle_start(cli_args)
elif command == 'stp':
    handle_stop()
elif command == 'ls':
    handle_report(cli_args)
elif command == 'log':
    handle_log()
else:
    raise Exception('Unknown command')
