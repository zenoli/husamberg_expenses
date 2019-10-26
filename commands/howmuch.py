import queries as q
from constants import (
    INVESTMENT_RATE, 
    SEP_DD, 
    IBAN,
    BANK,
    BOOKKEEPER
)
import bills

def howmuch_command(number, arg_str):
    if bills.bills:
        return (
            f"Please transfer {bills.bills[number]:.2f} CHF to\n"
            f"Recipient: {BOOKKEEPER}\n"
            f"Bank: {BANK}\n"
            f"IBAN: {IBAN}"
        )
    else:
        return f"Bills are not ready yet!"