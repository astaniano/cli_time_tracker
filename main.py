import sys

from start_task import handle_start
from stop_task import handle_stop
from report_task import handle_report
from log_task import handle_log

if len(sys.argv) < 2:
    raise Exception('pls specify your command')
command = sys.argv[1]

if command == 'start':
    handle_start()
elif command == 'stop':
    handle_stop()
elif command == 'report':
    handle_report()
elif command == 'log':
    handle_log()
else:
    print('unknown command')

