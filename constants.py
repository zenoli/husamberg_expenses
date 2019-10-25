import os
# Command identifiers:
HELP = 'help'
INIT = 'init'
LEAVE = 'leave'
ADD = 'add'
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
SEP_LENGTH = 25
SEP_DD = "=" * SEP_LENGTH + "\n"
SEP_D =  "-" * 25 + "\n"

def align_strings(str1, str2):
    l1 = len(str1)
    l2 = len(str2)
    n = 50 - l1 - l2
    if n < 0:
        return str1 + ' ' + str2
    else:
        return str1 + (' ' * n) + str2

def expenses_string(description, price):
    str1 = f"{description}:"
    str2 = f"{price:.2f} CHF"
    return align_strings(str1, str2)