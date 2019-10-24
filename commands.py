from command_ids import *


def help_command():
    return "Hi! Of course I can give you some help!!"

def init_command(name):
    return f'Hi {name}! Nice to meet you!'

def log_command(number, amount, description):
    return

def undo_command(number):
    return

def unknown_command():
    return "Command unknown..."

commands = {
    HELP: help_command,
    INIT: init_command,
    UNDO: undo_command,
    LOG : log_command,
    UNKNOWN : unknown_command
}