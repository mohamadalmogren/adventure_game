import time
import random


def print_pause(msg_to_print):
    print(msg_to_print)
    time.sleep(2)


def intro(option):
    print_pause("you dont know where are you?\n"
                "you are in 2077, and there are no techniques\n")
    print_pause("and we are the human live under the ground\n")
    print_pause("take this gun ,but it is weak.\n")
    print_pause("because there is a" + option + "is killing us")
    print_pause("in the right there is house of human king.\n"
                "but he is die before 5 years and no one"
                " join his house\n")
    print_pause("To your left is a gate to go outside.\n")


def house(item, option):
    if "labtop" in item:
        print_pause("\nYou join the human king before.")
        print_pause("\nand you take the The treasure.")
        print_pause("\nYou walk back to the underground.\n")
    else:
        print_pause("\nYou join the hunman king house.")
        print_pause("\nIt turns out there is big treasure.")
        print_pause("It is the powerful labtop and it has program\n"
                    "that is destroy all the robots in your area")
        print_pause("\nis is HOPE OF HUMANITY!!")
        print_pause("\nYou discard your gun and take "
                    "the labtop with you.")
        print_pause("\nYou walk back out to the underground.")
        item.append("labtop")
    underground(item, option)


def outside(item, option):
    print_pause("\nYou go outside and see the sun rise.")
    print_pause("\nbut you see" + option + " becareful."
                "you dont want to kill by " + option + ".")
    print_pause("\nops the " + option + "'s see you!")
    print_pause("\nThe " + option + " attacks you!\n")
    if "labtop" not in item:
        print_pause("you dont ready to fight the " + option +
                    "but you have your weak gun.\n")
    while True:
        choice2 = input("Would you like to (1) fight or (2) "
                        "run away?")
        if choice2 == "1":
            if "labtop" in item:
                print_pause("\nopen your labtop and run the programm\n"
                            "before" + option + " kill you")
                print_pause("\nthe program is runing you need to "
                            "dodge the" + option + " to have some "
                            "time!\n")
                print_pause("good job the programm is running now!\n"
                            "lock the" + option + "is turn off")
                print_pause("\ntake the head of" + option +
                            "and back to the underground.\n")
                print_pause("\ngood job you win!!\n"
                            "you bring the hope to the humans")
            else:
                print_pause("\nYou do your best...")
                print_pause("but your gun is week for the "
                            + option + ".")
                print_pause("\nYou have been defeated!\n")
            play_again()
            break
        if choice2 == "2":
            print_pause("\nYou run back into the underground. "
                        "\nLuckily, you don't seem to have been "
                        "followed.\n")
            underground(item, option)
            break


def underground(item, option):
    print_pause("Enter 1 to go outside!.")
    print_pause("Enter 2 to join human king house.")
    print_pause("the choice is yours")
    while True:
        choice = input("(Please enter 1 or 2.)\n")
        if choice == "1":
            outside(item, option)
            break
        elif choice == "2":
            house(item, option)
            break


def play_again():
    again = input("Would you like to play again? (y/n)").lower()
    if again == "y":
        print_pause("\n\n\nvery good! launching the game ...\n\n\n")
        play_game()
    elif again == "n":
        print_pause("\n\n\nThanks for playing! See you next time.\n\n\n")
    else:
        play_again()


def play_game():
    item = []
    option = random.choice([" king's robot ", " queen's robot ",
                            " prince robot ", " princess robot "])
    intro(option)
    underground(item, option)


play_game()
