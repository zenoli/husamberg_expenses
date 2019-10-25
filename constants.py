import os
# Command identifiers:
HELP = 'help'
INIT = 'init'
LEAVE = 'leave'
LOG = 'log'
STATUS = 'status'
HISTORY = 'history'
UNDO = 'undo'
UNKNOWN = 'unknown'

# db identifiers:
NAME = 'name'
EXPENSES = 'expenses'
NUMBER = 'number'
PRICE = 'price'
DESCRIPTION = 'description'
TIMESTAMP = 'timestamp'

# db constants
DB_NAME = 'db.json'
DB_PATH = os.path.join(os.getcwd())
DB_FULL_NAME = os.path.join(DB_PATH, DB_NAME)

# wg kasse
INVESTMENT_RATE = 20.0

# utils
SEP_DD = "=" * 25 + "\n"
SEP_D =  "-" * 25 + "\n"
