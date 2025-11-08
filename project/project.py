import csv
from os import system
from time import sleep
import validation as val


print("wlcome to TECH_bank...!\n")


with open("data.csv") as file:
    myfile = csv.reader(file)
    for line in myfile:
        val.data.append(line)
    for i in val.data:
        val.data.remove([])

while True:
    menu = input(
        "Options: \n\n"
        ""
        "1. Create an account => [1 or C]\n"
        "2. View bank account balance => [2 or V]\n"
        "3. Deposit to your bank account => [3 or D]\n"
        "4. Withdrawal from your bank account => [4 or W]\n"
        "5. Edit your account information => [5 or E]\n"
        "6. Transfer to another account => [6 or T]\n"
        "7. Save and Quit => [7 or Q or S]\n\n"
        ""
        "Please select an option: "
    )
    system("cls")
    match menu:

        case menu if menu in ["1", "c", "C"]:

            while True:
                if input("Do you want to create an account...? [yes/etc]: ") == "yes":
                    system("cls")
                    user = val.inserting_user_info()
                    print("Please note down your account number: ", user[0])
                    sleep(5)
                    val.data.append(user)
                    continue
                else:
                    system("cls")
                    break

        case menu if menu in ["2", "v", "V"]:
            user = val.user_finding("check your balance", True)
            if user:
                print(f"Dear {user[1]} {user[2]} your balance is {user[-1]}$")
                sleep(5)
                system("cls")
            else:
                continue

        case menu if menu in ["3", "D", "d"]:
            user = val.user_finding("want to deposit...?", True)
            if user:
                val.balance_workshop(user, None, user, "deposit", False, False, False)
            else:
                continue

        case menu if menu in ["4", "w", "W"]:
            user = val.user_finding("want to Withdrawal...?", True)

            if user:
                if user[-1] != 0:   
                    val.balance_workshop(user, user, None, "withdrawal", True, False, False)
                else:
                    print("Sorry your balance is 0$ and you can't Withdrawal...")
                    sleep(5)
                    system("cls")
                    continue
            else:
                continue

        case menu if menu in ["5", "e", "E"]:
            user = val.user_finding("want to edit", True)
            while True:
                if user:
                    for i in user:
                        print(i)

                    option = input(
                        "\nwhich option do you want to edit...\n\n"
                        "1. First name [1 or F]\n"
                        "2. Last name [2 or L]\n"
                        "3. Phone number [3 or P]\n"
                        "4. Email [4 or E]\n"
                        "5. Quit [4 or Q]\n\n"
                        ""
                        "option: "
                    )
                    system("cls")
                    match option:

                        case option if option in ["1", "F", "f"]:

                            while True:
                                edit_option = val.name_validation("First name")
                                new_user = val.edit(user, 1, "First name", edit_option)
                                if new_user:
                                    break
                                else:
                                    continue

                        case option if option in ["2", "L", "l"]:

                            while True:
                                edit_option = val.name_validation("Last name")
                                new_user = val.edit(user, 2, "Last name", edit_option)
                                if new_user:
                                    break
                                else:
                                    continue

                        case option if option in ["3", "P", "p"]:

                            while True:
                                edit_option = val.phone_number_validation()
                                new_user = val.edit(user, -4, "phone number", edit_option)
                                if new_user:
                                    break
                                else:
                                    continue

                        case option if option in ["4", "E", "e"]:

                            while True:
                                edit_option = val.email_validation()
                                new_user = val.edit(user, -2, "email", edit_option)
                                if new_user:
                                    break
                                else:
                                    continue

                        case option if option in ["5", "Q", "q"]:
                            system("cls")
                            break

                        case _:
                            print("Sorry option is not valid, try again...")
                else:
                    break

        case menu if menu in ["6", "t", "T"]:
            user1 = val.user_finding("want to Transfer...?", True)
            if user1:
                if user1[-1] != 0:
                    user2 = val.user_finding("still want to Transfer...?", False)
                    if user1 != user2:
                        if user2:
                            val.balance_workshop(user1, user1, user2, "transfer", True, True, True)
                        else:
                            continue

                    else:
                        print("Sorry the Transfer option is only for transfering money to another account...")
                        sleep(5)
                        system("cls")
                        continue
                else:
                    print("Sorry your balance is 0$ and you can't transfer...")
                    sleep(5)
                    system("cls")
                    continue            
            else:
                continue

        case menu if menu in ["7", "s", "S", "q", "Q"]:
            with open(r"data.csv", "w") as file:
                w = csv.writer(file)
                for item in val.data:
                    w.writerow(item)
            system("cls")
            break

        case _:
            system("cls")
            print("Sorry option is not valid, Please try again...")


print("Thanks for selecting us...!")
