import queries as q
from constants import INVESTMENT_RATE

def status_command(number, arg_str):
    my_expenses = q.total_flatmate_expenses(number)
    avg_expenses = q.average_expenses()
    balance = q.flatmate_balance(number)
    sign = "-:" if balance > 0 else "+"

    return (
        f"Your total expenses:\n"
        f"{my_expenses} CHF\n"
        f"Average expenses (over all flatmates) \n"
        f"{avg_expenses} CHF\n"
        f"Amount to pay by the end of semester:\n"
        f"Investement rate:\t{INVESTMENT_RATE} CHF\n"
        f"Balance:\t{sign}{abs(balance)} CHF\n"
        f"------------------\n"
        f"Total:\t{INVESTMENT_RATE - balance} CHF\n"
    )


