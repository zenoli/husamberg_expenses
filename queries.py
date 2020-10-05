import db
from constants import (
    DESCRIPTION,
    EXPENSES,
    PRICE,
    TIMESTAMP,
    NAME,
    NUMBER,
    INVESTMENT_RATE,
    INTERNET_MONTH,
    NUM_FLATMATES
)


def total_flatmate_expenses(number):
    prices = (log[PRICE] for log in db.db[number][EXPENSES])
    return sum(prices)


def num_flatmates():
    return NUM_FLATMATES


def total_expenses():
    expenses_list = (total_flatmate_expenses(number) for number in db.db)
    return sum(expenses_list)


def average_expenses():
    return total_expenses() / num_flatmates()


def flatmate_balance(number):
    return total_flatmate_expenses(number) - average_expenses()


def internet_per_semester():
    return 6 * INTERNET_MONTH / num_flatmates()


def expenses_list(number):
    return db.db[number][EXPENSES]


def bill(number):
    balance = flatmate_balance(number)
    internet = internet_per_semester()
    return internet + INVESTMENT_RATE - balance
