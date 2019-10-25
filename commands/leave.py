import db

def success_msg(number, name): 
    return (
        f"It's so sad that you are leaving our flat {name} :-(...!\n"
        f"Your phone number {number} has successfully been removed.\n"
        f"The only thing left to do is type 'stop' to leave the chatbot."
    )


def fail_msg(number):
    return (
        f"It looks like you are already deregistered. \n"
        f"The only thing left to do is type 'stop' to leave the chatbot."
    )


def wrong_number_msg(number, typed_number):
    return (
        f"FAIL: Wrong number. You typed:\n"
        f"'{typed_number}\n"
        f"instead of: \n"
        f"{number}\n"
        f"Please try again."
    )



def leave_command(number, arg_str):
    typed_number = arg_str
    if number != typed_number:
        return wrong_number_msg(number, typed_number)
    
    name = db.remove_flatmate(number)
    if name:
        return success_msg(number, name)
    else:
        return fail_msg(number)