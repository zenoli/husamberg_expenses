import os
# Command identifiers:
HELP = 'help'
INIT = 'init'
LEAVE = 'leave'
LOG = 'log'
STATUS = 'status'
UNDO = 'undo'
UNKNOWN = 'unknown'

# db identifiers:
NAME = 'name'
EXPENSES = 'expenses'
NUMBER = 'number'

# db constants
DB_NAME = 'db.json'
DB_PATH = os.path.join(os.getcwd())
DB_FULL_NAME = os.path.join(DB_PATH, DB_NAME)