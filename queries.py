from db import db
from constants import (
    DESCRIPTION,
    EXPENSES,
    PRICE,
    TIMESTAMP,
    NAME,
    NUMBER,
    INVESTMENT_RATE
)


def total_flatmate_expenses(number):
    prices = (log[PRICE] for log in db[number][EXPENSES])
    return sum(prices)


def num_flatmates():
    return len(db)


def total_expenses():
    expenses_list = (total_flatmate_expenses(number) for number in db)
    return sum(expenses_list)


def average_expenses():
    return total_expenses() / num_flatmates()


def flatmate_balance(number):
    return total_flatmate_expenses(number) - average_expenses()


def expenses_list(number):
    return db[number][EXPENSES]


def bill(number):
    balance = flatmate_balance(number)
    return INVESTMENT_RATE - balance
