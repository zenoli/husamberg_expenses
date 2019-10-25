import queries as q
from constants import (
    DESCRIPTION,
    PRICE,
    SEP_DD,
    expenses_string
)

def history_command(number, arg_str):
    expenses = q.expenses_list(number)[-10:]
    strings = (
        f"{exp[DESCRIPTION]}:\t{exp[PRICE]:.2f} CHF\n"
        for exp in expenses
    )
    string_list = ''.join(strings)
    return (
        f"History (Max 10 elements)\n"
        f"{SEP_DD}"
        f"{string_list}"
    )

