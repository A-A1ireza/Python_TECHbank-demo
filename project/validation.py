from random import randint
from time import sleep
from os import system
import datetime as dt
import re


data = []


def unique_checker(object: str, SC_object: vars, index) -> bool:  # SC = snake case
    dup = None
    for user in data:
        if SC_object == user[index]:
            dup = True

    if dup:
        system("cls")
        print(f"Sorry {object} is not unique, try again...")
        return False
    else:
        return True


def account_number_validation():
    # Ostad ba AVALIN search to goolge khondm k shomare hesab bein 12 ta 16 raqame. baraye manm 12 raqame
    while True:
        account_number = str(randint(100000000000, 999999999999))
        dup = None
        for user in data:
            if account_number == user[0]:
                dup = True

        if dup:
            continue
        else:
            return account_number


def name_validation(name: str) -> vars:
    while True:
        name_ = input(f"Please enter your {name}: ")
        if name_.isalpha():
            system("cls")
            return name_
        else:
            system("cls")
            print(f"Sorry your {name} is not valid, Please try again...")


def age_validation():
    birth = []
    while True:
        year = input("Please enter your YEAR of birth: ")
        if (
            year.isdigit()
            and len(year) == 4
            and int(year) <= (dt.datetime.now(dt.UTC).year)
        ):
            age = dt.datetime.now(dt.UTC).year - int(year)
            if 18 <= (age) <= 130:
                birth.append(year)
                system("cls")
                break
            else:
                raise NameError(
                    "Sorry you are (not old enough/too old) for having an account...!"
                )
        else:
            system("cls")
            print("Sorry your year of birth is not valid please try again...")
            continue

    while True:
        month = input("Please enter your MONTH of birth: ")
        if month.isdigit() and (1 <= int(month) <= 12):
            birth.append(month)
            system("cls")
            break
        else:
            system("cls")
            print("Month is not valid please try again...")
            continue

    while True:
        day = input("Please enter your DAY of birth: ")
        system("cls")
        if day.isdigit() and int(day) != 0:
            if 1 <= int(month) <= 6:
                if 1 <= int(day) <= 31:
                    birth.append(day)
                    birth.append(age)
                    break
                else:
                    print(
                        "Sorry day of birth must be between 1-31, please try again..."
                    )
                    continue
            else:
                if 1 <= int(day) <= 30:
                    birth.append(day)
                    birth.append(age)
                    break
                else:
                    print(
                        "Sorry day of birth must be between 1-30, please try again..."
                    )
                    continue
        else:
            print("Sorry day is not valid, please try again...")
            continue

    return birth  # last index == user age


def phone_number_validation():
    while True:
        phone_number = input("Please enter your phone number: ")
        system("cls")
        if (
            phone_number.isdigit()
            and len(phone_number) == 11
            and phone_number[:2] == "09"
        ):
            if unique_checker("phone number", phone_number, -4):
                system("cls")
                return phone_number
        else:
            system("cls")
            print("Sorry phone number is not valid, Please try again...")
            continue


def national_code_validation():
    while True:
        national_code = input("Please enter your national code: ")
        if national_code.isdigit() and len(national_code) == 10:
            if unique_checker("national code", national_code, -3):
                system("cls")
                return national_code

        else:
            system("cls")
            print("Sorry national code is not valid, Please try again...")


def email_validation():
    while True:
        email = input("Please enter your email: ")
        pattern = r"^[a-zA-Z0-9_](\.?[a-zA-Z0-9])+@[a-zA-Z0-9-]+\.[a-zA-Z.]{2,18}$"
        # Ostad bekhoda amozesh Regex didm va khodm neveshtm
        # source: Ali Bigdeli(YT) python pro course E(21-24)
        if re.fullmatch(pattern, email):
            if unique_checker("email", email, -2):
                system("cls")
                return email
            else:
                continue
        else:
            system("cls")
            print("Sorry email is not valid, Please try again.")
            continue


def balance_validation():
    while True:
        balance = input("Please deposit money(at least 10$): ")
        if balance.isdigit() and int(balance) >= 10:
            system("cls")
            return int(balance)
        else:
            system("cls")
            print("Deposit at least 10$ please...")


def inserting_user_info():
    account_number = account_number_validation()
    first_name = name_validation("first name")
    last_name = name_validation("last name")
    date_of_birth_and_age = age_validation()
    phone_number = phone_number_validation()
    national_code = national_code_validation()
    email = email_validation()
    balance = balance_validation()

    return [
        account_number,
        first_name,
        last_name,
        date_of_birth_and_age,
        phone_number,
        national_code,
        email,
        balance,
    ]


def user_Loc_finder(SC_object: vars, index) -> bool:  # SC = snake case
    for user in data:
        if SC_object == user[index]:
            return user


def valid_user(text: str, len_count: int, index: int, p_check: bool):
    while True:
        key = input(f"Please enter the {text}: ")
        if key.isdigit() and len(key) == len_count:
            if p_check:
                if key[:2] == "09":
                    system("cls")
                    user = user_Loc_finder(key, index)
                    return user

            system("cls")
            user = user_Loc_finder(key, index)
            if user == None:
                print("Sorry the option is not valid, Please try again...")
                continue
            return user
        else:
            system("cls")
            print("Sorry the option is not valid, Please try again...")


def user_finding(text: str, no_receiver: bool):
    if input(f"Do you {text}: [yes/etc] ") == "yes":
        system("cls")
        while True:
            if no_receiver:
                option = input(
                    "Please select one of these options: \n\n"
                    "1. Account Number [1 or A]\n"
                    "2. National Code [2 or N]\n"
                    "3. Phone Number [3 or P]\n"
                    "4. Quit [4 or Q]\n\n"
                    "Option: "
                )
                system("cls")
            else:
                option = input(
                    "Please select one of these options: \n\n"
                    ""
                    "1. Account Number(receiver) [1 or A]\n"
                    "4. Quit [4 or Q]\n\n"
                    "Option: "
                )
                system("cls")

            match option:
                case option if option in ["1", "A", "a"]:
                    user = valid_user("account number", 12, 0, False)
                    return user

                case option if option in ["2", "N", "n"] and no_receiver:
                    user = valid_user("national code", 10, -3, False)
                    return user

                case option if option in ["3", "P", "p"] and no_receiver:
                    user = valid_user("phone number", 11, -4, True)
                    return user

                case option if option in ["4", "Q", "q"]:
                    return False

                case _:
                    system("cls")
                    print("Sorry the option is not valid, Please try again...")

    else:
        system("cls")
        return False


def balance_workshop(user: list, user1: list | None,  user2: list| None,  user_text: str, Withdrawal: bool, transfer1: bool, transfer2: bool):

    while True:
        key = input(
            f"Welcome dear {user[1]} {user[2]}\nHow much do you want to {user_text}: "
        )
        system("cls")
        if key.isdigit() and key != 0:
            if Withdrawal:
                user1[-1] = int(user1[-1])
                if int(key) <= user1[-1]:
                    user1[-1] -= int(key)
                    print(
                        f"Operation done...!\nDear {user1[1]} {user1[2]}, Now your balance is {user1[-1]}$"
                    )
                    sleep(5)
                    system("cls")
                    if not transfer1:
                        break
                else:
                    system("cls")
                    print(
                        f"Your request is more than more balance, Please try again... (Balance: {user1[-1]}$)"
                    )
                    sleep(3)
                    system("cls")
                    continue

            user2[-1] = int(user2[-1])
            user2[-1] += int(key)
            if not transfer2:
                return print(
                    f"Dear {user2[1]} {user2[2]}, Now your balance is {user2[-1]}$"
                ), sleep(5), system("cls")

            break
        else:
            system("cls")
            print("Sorry balance is not valid, try again...")


def edit(user, user_index, user_text, editing_option):
    if (
        input(f"{editing_option} is your new {user_text}\nAre you sure? [yes/etc] ")
        == "yes"
    ):
        user[user_index] = editing_option
        system("cls")
        return user
    else:
        system("cls")
        return False


