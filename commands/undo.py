import db
from constants import PRICE, DESCRIPTION


def success_msg(price, description):
    return (
        f"Undo successful!\n"
        f"{description}: {price} CHF.\n"
        f"got removed."
    )


def fail_msg():
    return (
        f"There is nothing to undo.\n"
        f"Your list of expenses is empty."
    )

def undo_command(number, arg_str):
    removed_entry = db.undo_last_log(number)
    if removed_entry:
        return success_msg(removed_entry[PRICE], removed_entry[DESCRIPTION])
    else:
        return fail_msg()