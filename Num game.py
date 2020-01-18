import random
import os
cls = lambda: os.system('cls')

def guess():
    global user
    user = input("Enter a number between 1 and 9: ")

    if user.isdigit() == False:
        print("Wrong input")
        user = guess()
    else:
        if int(user) not in range(1, 10):
            print("Wrong number")
            user = guess()
    return user


count = 1


def game():
    global count
    user_num = int(guess())

    print("Your guess is", user_num)
    num = random.randint(1, 9)
    print("Computer's choice is", num)

    if user_num == num:
        print("You guessed correcly!")
    if user_num > num:
        print("Your number is too big")
    if user_num < num:
        print("Your number is too small")

    if input("Do you want to play another game? yes/no: ") == "yes":
        count = count + 1
        cls()
        game()

    else:
        print("Game over. You took", count, "tries")


game()