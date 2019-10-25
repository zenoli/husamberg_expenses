separator = f"==========\n"

def help_command(number, arg_str):
    return (
        f"Simply type one of the following commands:\n"
        f"==========\n"
        f"Log [PRICE], [DESCRIPTION].\n"
        f"Log your groceries to the system.\n"
        f"Example:\n"
        f"Log salz: 2.95chf\n"
        f"==========\n"
        f"Undo\n"
        f"Undos your last 'Log' command\n"
        f"(in case you did a mistake)\n"
        f"==========\n"
        f"Status\n"
        f"Gives you a summary of your current expenses and your balance\n"
    )