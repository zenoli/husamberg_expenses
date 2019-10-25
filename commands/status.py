import queries as q
from constants import INVESTMENT_RATE, SEP_DD

def status_command(number, arg_str):
    my_expenses = q.total_flatmate_expenses(number)
    avg_expenses = q.average_expenses()
    balance = q.flatmate_balance(number)
    sign = "-:" if balance > 0 else "+"

    return (
        f"Your total expenses:\t{my_expenses} CHF\n"
        f"Average expenses:\t{avg_expenses} CHF\n"
        f"Amount to pay by the end of semester:\n"
        f"Investement rate:\t{INVESTMENT_RATE} CHF\n"
        f"Balance:\t\t\t{sign}{abs(balance)} CHF\n"
        f"{SEP_DD}"
        f"Total:\t{INVESTMENT_RATE - balance} CHF\n"
    )


