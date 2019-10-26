import re
from constants import (
    HELP,
    HELLO,
    INIT,
    LEAVE,
    ADD,
    STATUS,
    HISTORY,
    UNDO,
    CHECKOUT,
    FINALIZE,
    HOWMUCH,
    UNKNOWN
)
from commands import (
    help,
    hello,
    init,
    leave,
    add,
    status,
    history,
    undo,
    checkout,
    finalize,
    howmuch,
    unknown
)


command_list = {
    HELP: help.help_command,
    INIT: init.init_command,
    HELLO: hello.hello_command,
    LEAVE: leave.leave_command,
    STATUS: status.status_command,
    HISTORY: history.history_command,
    UNDO: undo.undo_command,
    ADD: add.add_command,
    CHECKOUT: checkout.checkout_command,
    FINALIZE: finalize.finalize_command,
    HOWMUCH: howmuch.howmuch_command,
    UNKNOWN: unknown.unknown_command
}

def find_command(cmd_str):
    is_command = lambda cmd_id : re.match(cmd_id, cmd_str, re.IGNORECASE)
    result = [cmd_id for cmd_id in command_list if is_command(cmd_id)]
    return result[0] if result else UNKNOWN
