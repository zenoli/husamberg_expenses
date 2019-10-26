import db
import queries as q
import json
import os
from datetime import date
from constants import (
    BILLS_FULL_NAME
)


def load():
    if os.path.isfile(BILLS_FULL_NAME):
        with open(BILLS_FULL_NAME) as json_file:
            return json.load(json_file)


def finalize():
    global bills
    bills = { number : q.bill(number) for number in db.db }
    with open(BILLS_FULL_NAME,"w") as f:
        json.dump(bills,f)
        return True


def init():
    global bills
    bills = {}

init()

