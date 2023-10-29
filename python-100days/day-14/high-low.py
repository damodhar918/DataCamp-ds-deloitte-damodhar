from art import logo, vs
from game_data import data
import random
# from os import system, name


def select_item(data):
    value = random.choice(data)
    data.remove(value)
    return [value, data]


def sideToString(side_variable, side):
    return f"Compare {side}: {side_variable['name']}, a {side_variable['description']}, from {side_variable['country']}"


def clear():
    if name == "nt":
        _ = system("cls")
    else:
        _ = system("clear")
    print(logo)


def compare(sideA, sideB):
    if sideA['follower_count'] >= sideB['follower_count']:
        return True
    else:
        return False


def game(data):
    print(logo)
    sideA, data = select_item(data)
    score = 0
    result = False
    while len(data) > 0:
        sideB, data = select_item(data)
        message = f"{sideToString(sideA,'A')}\n{vs}\n{sideToString(sideB,'B')}"
        print(message)
        anwser = (input("Who has more followers? Type 'A' or 'B': ")).lower()
        if anwser == "a":
            result = compare(sideA, sideB)
            sideA = sideB
        elif anwser == "b":
            result = compare(sideB, sideA)
        else:
            result = False

        if result == False:
            break
        else:
            score += 1
            clear()
            print(f"You're Right! Current score: {score}")

    if result == False:
        clear()
        print(f"Sorry, that's wrong. Final score: {score}")
    else:
        clear()
        print(f"Congrats, you got them all correct! Final score: {score}")


game(data)
