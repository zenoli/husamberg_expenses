import queries as q
from constants import INVESTMENT_RATE, SEP_DD, IBAN
from bills import bills

def howmuch_command(number, arg_str):
    if bills:
        return (
            f"Please transfer {bills[number]:.2f} CHF to\n"
            f"IBAN: {IBAN}"
        )
    else:
        return f"Bills are not ready yet!"