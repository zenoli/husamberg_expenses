def generate_init_message(number, name, success):
    if success:
        return (
            f'Welcome to the club {name}!\n'
            f'Your phone number {number} has successfully been registered.\n'
            f'You can deregister by using typing "Leave {number}".'
        )
    else:
        return (
            f'Oops. It seems that the number {number} is already registered...'
        )



def generate_leave_message(number, name, success):
    if success:
        return '''\
        It's so sad that you are leaving our flat {name} :-(...!\
        Your phone number {number} has successfully been removed.\
        The only thing left to do is type 'stop' to leave the chatbot.
        '''.format(number=number, name=name)
    else:
        return '''\
        Oops. It seems that the number {number} is already registered...
        '''.format(number=number)