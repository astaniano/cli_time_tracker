import sys

from commands.start_task import handle_start
from commands.stop_task import handle_stop
from commands.report_task import handle_report
from commands.log_task import handle_log

cli_args = sys.argv

if len(cli_args) < 2:
    raise Exception('pls specify your command')

command = cli_args[1]

if command == 'start':
    handle_start(cli_args)
elif command == 'stop':
    handle_stop()
elif command == 'report':
    handle_report(cli_args)
elif command == 'log':
    handle_log()
else:
    print('unknown command')

