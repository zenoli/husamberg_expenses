import json
import os

db = dict()


def add_flatmate(number, name):
    if number in db:
        return False
    else:
        db[number] = {'name': name, 'expenses': []}
        return True

def remove_flatmate(number):
    if number in db:
        name = db[number]['name']
        db.pop(number)
        return name
    else:
        return False

def load():
    if os.path.isfile(os.path.join(os.getcwd(), 'db.json')):
        with open('db.json') as json_file:
            global db
            db = json.load(json_file)


def save():
    with open("db.json","w") as f:
        json.dump(db,f)