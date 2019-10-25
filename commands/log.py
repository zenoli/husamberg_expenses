import re

def no_argument_msg():
    return (
        f"FAIL: No arguments provided.\n"
        f"A valid example would be:\n"
        f"Log salz: 2.95chf\n"
    )

def wrong_argument_msg():
    return (
        f"FAIL: Wrong argument.\n"
        f"A valid example would be:\n"
        f"Log salz: 2.95chf\n"
    )


def success_msg(price, description):
    return (
        f"Successfully logged {price} CHF\n"
    )

def parse_arg(arg_str):
    if not arg_str:
        return
    else:
        return


def log_command(number, arg_str):
    if not arg_str:
        return no_argument_msg()
    args = arg_str.split(":")
    if len(args) != 2:
        return wrong_argument_msg()
    else:
        price_str = re.match(r'\d+([.|,]\d{1,2})?', args[1].strip()).group(0)
        price = float(price_str.replace(",", "."))
        description = args[0].strip()
        return success_msg(price, description)
