# register
# - first name, last name, password, email
# - generate user account number


# login
# - account number & password


# bank operations

# Initializing the system
import auth
import random
import validation
import database
import bank_operations
from getpass import getpass


def init():
    print("Welcome to bankPHP")

    account_holder = int(input("Do you have an account with us: 1 (yes) 2 (no) \n"))

    if account_holder == 1:
        auth.login()

    elif account_holder == 2:
        auth.register()

    else:
        print("You have selected an invalid option. Please try again.")
        init()


# def set_current_balance(user_details, balance):
#     user_details[4] = balance


# def get_current_balance(user_details):
#     return user_details[4]


init()