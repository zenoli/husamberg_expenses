import json
import os
from constants import (
    NAME, 
    EXPENSES, 
    DB_NAME,
    DB_FULL_NAME)

db = dict()


def add_flatmate(number, name):
    if number in db:
        return False
    else:
        db[number] = {NAME: name, EXPENSES: []}
        return True

def remove_flatmate(number):
    if number in db:
        name = db[number][NAME]
        db.pop(number)
        return name
    else:
        return False

def load():
    if os.path.isfile(DB_FULL_NAME):
        with open(DB_FULL_NAME) as json_file:
            global db
            db = json.load(json_file)


def save():
    with open(DB_FULL_NAME,"w") as f:
        json.dump(db,f)