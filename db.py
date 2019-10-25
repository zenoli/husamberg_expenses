import json
import os
from datetime import date
from constants import (
    NAME, 
    EXPENSES, 
    DB_NAME,
    DB_FULL_NAME,
    PRICE,
    DESCRIPTION,
    TIMESTAMP
)


def add_flatmate(number, name):
    if number in db:
        return False
    else:
        db[number] = {NAME: name, EXPENSES: []}
        save()
        return True

def remove_flatmate(number):
    if number in db:
        name = db[number][NAME]
        db.pop(number)
        save()
        return name
    else:
        return None


def log_entry(number, price, description):
    db[number][EXPENSES].append({
        PRICE: price,
        DESCRIPTION: description,
        TIMESTAMP: date.today().strftime("%d/%m/%Y")
    })
    save()


def undo_last_log(number):
    if len(db[number][EXPENSES]) > 0:
        entry = db[number][EXPENSES].pop()
        save()
        return entry
    else:
        return None



def save():
    with open(DB_FULL_NAME,"w") as f:
        json.dump(db,f)



def init():
    global db
    if os.path.isfile(DB_FULL_NAME):
        with open(DB_FULL_NAME) as json_file:
            db = json.load(json_file)
    else:
        db = dict()
        save()


init()