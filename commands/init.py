import db

def success_msg(number, name):
    return (
        f"Welcome to the club {name}!\n"
        f"Your phone number {number} has successfully been registered.\n"
        f"You can now start adding your expenses to the system.\n"
        f"Let's try with an example (you can undo it afterwards):\n"
        f"Type the following to announce that you bought milk:\n"
        f"Add milk: 1.95chf"
    )


def fail_msg(number):
    return (
        f"FAIL:The number {number} is already registered..."
    )


def argument_error_msg():
    return (
        f"FAIL: No name provided.\n"
        f"Please type 'Init [NAME]' where [NAME] is to be replaced by your actual name.\n"
        f"Example: 'Init Emil"
    )

def parse_name(arg_str):
    if (not arg_str) or (not arg_str.strip()):
        return None
    else:
        return arg_str.strip()

def init_command(number, arg_str):
    name = arg_str
    if not name:
        return argument_error_msg()
    success = db.add_flatmate(number, name)
    if success:
        return success_msg(number, name)
    else:
        return fail_msg(number)