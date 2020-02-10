import db
import queries as q
import json
import os
from datetime import date
from constants import (
    BILLS_FULL_NAME, INVESTMENT_RATE
)


def load():
    if os.path.isfile(BILLS_FULL_NAME):
        with open(BILLS_FULL_NAME) as json_file:
            return json.load(json_file)


def finalize():
    global bills

    expenses = { number : q.total_flatmate_expenses(number) for number in db.db }
    bills = { 
        "expenses" : expenses,
        "avg_expenses" : q.average_expenses(),
        "internet" : q.internet_per_semester(),
        "investment" : INVESTMENT_RATE
     }
    with open(BILLS_FULL_NAME,"w") as f:
        json.dump(bills,f)
        return True


def init():
    global bills
    bills = load()

init()

