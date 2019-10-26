import json
import os
from datetime import date
from constants import (
    NAME, 
    EXPENSES, 
    CURRENT_DB,
    DB_PATH,
    PRICE,
    DESCRIPTION,
    TIMESTAMP,
    BILLS_FULL_NAME
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


def add_expense(number, price, description):
    if number in db:
        db[number][EXPENSES].append({
            PRICE: price,
            DESCRIPTION: description,
            TIMESTAMP: date.today().strftime("%d/%m/%Y")
        })
        save()
        return True
    else:
        return False


def undo_last_log(number):
    if len(db[number][EXPENSES]) > 0:
        entry = db[number][EXPENSES].pop()
        save()
        return entry
    else:
        return None



def save():
    db_filename = f"{current_db}.json"
    db_full_name = os.path.join(DB_PATH, db_filename)
    with open(db_full_name,"w") as f:
        json.dump(db,f)



def checkout_db(db_name):
    global db
    global current_db
    current_db = db_name
    db = load(db_name)
    if not db: #If db does not exist, create new one
        db = dict()
        save()
        return False
    else:
        return True
        

def load(db_name):
    db_filename = f"{db_name}.json"
    db_full_name = os.path.join(DB_PATH, db_filename)
    if os.path.isfile(db_full_name):
        with open(db_full_name) as json_file:
            db = json.load(json_file)
            return db
    else:
        return None


def init():
    global db
    global current_db
    current_db = "HS19"
    checkout_db(current_db)

init()