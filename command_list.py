import re
from constants import (
    HELP,
    INIT,
    LEAVE,
    LOG,
    STATUS,
    HISTORY,
    UNDO,
    UNKNOWN
)
from commands import (
    help,
    init,
    leave,
    log,
    status,
    history,
    undo,
    unknown
)


command_list = {
    HELP: help.help_command,
    INIT: init.init_command,
    LEAVE: leave.leave_command,
    STATUS: status.status_command,
    HISTORY: history.history_command,
    UNDO: undo.undo_command,
    LOG: log.log_command,
    UNKNOWN: unknown.unknown_command
}

def find_command(cmd_str):
    is_command = lambda cmd_id : re.match(cmd_id, cmd_str, re.IGNORECASE)
    result = [cmd_id for cmd_id in command_list if is_command(cmd_id)]
    return result[0] if result else UNKNOWN
