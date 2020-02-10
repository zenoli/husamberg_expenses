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
        my_expenses = bills.bills["expenses"][number]
        avg_expenses = bills.bills["avg_expenses"]
        balance = my_expenses - avg_expenses
        internet = bills.bills["internet"]
        investment = bills.bills["investment"]
        sign = "+" if balance >= 0 else "-"
        sign_neg = "-" if balance >= 0 else "+"
        
        total = internet + investment - balance
        return (
            f"Please transfer {total:.2f} CHF to\n"
            f"Recipient: {BOOKKEEPER}\n"
            f"Bank: {BANK}\n"
            f"IBAN: {IBAN}"
            f"\n"
            f"Receipt:\n"
            f"Your total expenses:\t{my_expenses:.2f} CHF\n"
            f"Average expenses:\t{avg_expenses:.2f} CHF\n"
            f"Balance:\t\t\t{sign}{abs(balance):.2f} CHF\n"
            f"Amount to transfer is calculated as:\n"
            f"'Investment Rate' + 'Internet' - 'Balance':"
            f"Investement rate:\t{investment:.2f} CHF\n"
            f"Internet:\t+{internet:.2f} CHF\n"
            f"Balance:\t{sign_neg}{abs(balance):.2f} CHF\n"
            f"{SEP_DD}"
            f"Total:\t{INVESTMENT_RATE + internet - balance:.2f} CHF"
        )
    else:
        return f"Bills are not ready yet!"