import auth
import random
import database
import validation

def services(user):
    print("Welcome %s %s " % (user[0], user[1]))

    selected_option = int(input("What would you like to do? (1) deposit (2) withdrawal (3) Logout (4) Exit \n"))

    if selected_option == 1:
        deposit()

    elif selected_option == 2:
        withdraw()

    elif selected_option == 3:
        auth.logout()

    elif selected_option == 4:
        exit()

    else:
        print("Invalid option selected")
        services(user)


def withdraw():
    # get current balance
    # get amount to withdraw
    # check if current balance > withdraw balance
    # deduct withdrawn amount form current balance
    # display current balance
    current_user_account_number = int(input("Enter your account number: \n"))
    
    is_account_valid = validation.account_number_validation(current_user_account_number)
    if is_account_valid:
        current_user = str.split(database.read(current_user_account_number), ',')
        print("Your current account balance is " + "NGN" + current_user[4] + ".00")
    
        withdrawal_amount = int(input("Enter the amount you want to withdraw: \n"))
        if withdrawal_amount <= int(current_user[4]):
            new_balance = int(current_user[4]) - withdrawal_amount
            print("Please take your cash.")
            # update user account balance
            # database.update(current_user_account_number, 4)
            print("Your new account balance is " + "NGN" + str(new_balance) + ".00 \n")
            print("Thank you for banking with us \n")
            exit()

        else:
            print("Insufficient account balance. Please try again")
            auth.login()
    else:
        print("Invalid account number. Please try again")
        auth.login()


def deposit():
    # get current balance
    # get amount to deposit
    # add deposited amount to current balance
    # display current balance
    current_user_account_number = int(input("Enter your account number: \n"))
    is_account_valid = validation.account_number_validation(current_user_account_number)
    if is_account_valid:
        current_user = str.split(database.read(current_user_account_number), ',')
        print("Your current account balance is " + "NGN" + current_user[4] + ".00")
        
        deposit_amount = int(input("Enter the amount you want to deposit: \n"))
        new_balance = int(current_user[4]) + deposit_amount
        # update user account balance
        # database.update(current_user_account_number, 4)
        print("Your new account balance is " + "NGN" + str(new_balance) + ".00 \n")
        print("Thank you for banking with us \n")
        exit()
    else:
        print("Invalid account number. Please try again")
        auth.login()


def generate_account_number():
    return random.randrange(1111111111, 9999999999)