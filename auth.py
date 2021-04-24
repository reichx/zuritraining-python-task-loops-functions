import database
import validation
import bank_operations
from getpass import getpass

def login():
    print("********* Login ***********")

    account_number_from_user = input("Enter your account number to login: \n")

    is_valid_account_number = validation.account_number_validation(account_number_from_user)

    if is_valid_account_number:
        password = getpass("Enter your password: \n")

        user = database.authenticated_user(account_number_from_user, password);

        if user:
            bank_operations.services(user)

        print('Invalid account or password')
        login()

    else:
        print("Account Number Invalid: check that you have up to 10 digits and only integers")
        init()


def register():
    print("****** Register *******")

    email = input("What is your email address? \n")
    first_name = input("What is your first name? \n")
    last_name = input("What is your last name? \n")
    password = getpass("Create a password for yourself \n")

    account_number = bank_operations.generate_account_number()

    is_user_created = database.create(account_number, first_name, last_name, email, password)

    if is_user_created:

        print("Your Account Has Been Created")
        print(" == ==== ====== ===== ===")
        print("Your account number is: %d" % account_number)
        print("Make sure you keep it safe")
        print(" == ==== ====== ===== ===")

        login()

    else:
        print("Something went wrong, please try again")
        register()


def logout():
    login()