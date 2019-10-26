import os
# Command identifiers:
HELP = 'help'
HELLO = 'hello'
INIT = 'init'
LEAVE = 'leave'
ADD = 'add'
STATUS = 'status'
HISTORY = 'history'
UNDO = 'undo'
UNKNOWN = 'unknown'
HOWMUCH = 'how'
CHECKOUT = 'checkout'
FINALIZE = 'finalize'

# db identifiers:
NAME = 'name'
EXPENSES = 'expenses'
NUMBER = 'number'
PRICE = 'price'
DESCRIPTION = 'description'
TIMESTAMP = 'timestamp'

# db constants
ADMIN = "+41793637649"
CURRENT_DB = ""
DB_PATH = os.path.join(os.getcwd(), "databases")
BILLS_FULL_NAME = os.path.join(os.getcwd(), "bills.json")

# wg kasse
INVESTMENT_RATE = 20.0
BOOKKEEPER = "Céline Bitter"
IBAN = "CH43 0024 5245 6297 78M1 Q"
BANK = "UBS Frick"

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