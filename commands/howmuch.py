import queries as q
from constants import INVESTMENT_RATE, SEP_DD, IBAN
from bills import bills

def howmuch_command(number, arg_str):

    return (
        f"Please transfer {bills[number]:.2f} CHF to\n"
        f"IBAN: {IBAN}"
    )