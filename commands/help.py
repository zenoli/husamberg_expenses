from constants import SEP_DD

def help_command(number, arg_str):
    return (
        f"Simply type one of the following commands:\n"
        f"{SEP_DD}"
        f"Add [DESCRIPTION]: [PRICE].\n"
        f"Add your groceries to the system.\n"
        f"Example:\n"
        f"Add salz: 2.95chf\n"
        f"{SEP_DD}"
        f"Undo\n"
        f"Undos your last 'Add' command.\n"
        f"(in case you did a mistake)\n"
        f"{SEP_DD}"
        f"Status\n"
        f"Gives you a summary of your current expenses and your balance.\n"
        f"{SEP_DD}"
        f"History\n"
        f"Displays the 10 most recent items.\n"
    )