import re
import db
from constants import expenses_string

def no_argument_msg():
    return (
        f"FAIL: No arguments provided.\n"
        f"A valid example would be:\n"
        f"Add salz: 2.95chf\n"
    )

def wrong_argument_msg():
    return (
        f"FAIL: Wrong argument.\n"
        f"A valid example would be:\n"
        f"Add salz: 2.95chf\n"
    )


def not_registered_msg(number):
    return (
        f"You are not registered yet.\n"
        f"Type 'Init [NAME]' where [NAME] is to be replaced by your actual name.\n"
        f"Example: 'Init Emil"
    )


def success_msg(price, description):
    return (
        f"Successfully added:\n"
        f"{description}:\t\t{price:.2f} CHF\n"
        f"Type 'Undo' if you made a mistake."
    )

def parese_whitespace(arg_str):
    if not arg_str:
        return
    else:
        return


def add_command(number, arg_str):
    if not arg_str:
        return no_argument_msg()
    args = arg_str.split(":")
    if len(args) != 2:
        args = arg_str.split()
        if len(args) != 2:
            return wrong_argument_msg()
    match = re.match(r'\d+([.|,]\d{1,2})?', args[1].strip())
    if match:
        price = float(match.group(0).replace(",", "."))
        description = args[0].strip()
        success = db.add_expense(number, price, description)
        if success:
            return success_msg(price, description)
        else:
            return not_registered_msg(number)
    else:
        return wrong_argument_msg()
