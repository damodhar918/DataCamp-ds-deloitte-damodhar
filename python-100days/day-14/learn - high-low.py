from re import A
from art import logo, vs
from game_data import data
import random
# from os import system, name
from IPython.display import clear_output
import os
clear = lambda : os.system('cls') # or clear for Linux


def pickProfile(data):
    """
    Purpose: data
    """
    value = random.choice(data)
    data.remove(value)
    return [value, data]

def getProfileString(profile, side):
    """
    Purpose: 
    """
    return f"Compare {side}: {profile['name']}, a {profile['description']}, from {profile['country']}"


def declearResults(score):
    clear_output(wait=True)
    clear()
        

def game(data):
    """ Purpose: Run game """
    target = len(data)
    sideA,data = pickProfile(data)
    score=0
    while True: 
        declearResults(score)
        scoreInfo = ''
        if score == target:
            print(f"{logo}\nYour score is 100%")
            break
        elif score :   
            scoreInfo = f"You're Right! Current score: {score}\n"
        sideB,data = pickProfile(data)
        print(f"{logo}\n{scoreInfo}{getProfileString(sideA, 'A')}\n{vs}\n{getProfileString(sideB, 'B')}") 
        ip = input().lower()
        while  ip  not in ['a', 'b']:
            print(f"Please provide valid input A or B")
            ip = input().lower()
        if sideA['follower_count'] >= sideB['follower_count']:
            if ip == 'a':
                score += 1
                sideA = sideB
            else:
                declearResults(score)
                print(f"{logo}\nSorry, that's wrong. Final score: {score}")
            
                break
        else:
            if ip == 'b':
                score += 1
                sideA = sideB
            else:
                declearResults(score)
                print(f"{logo}\nSorry, that's wrong. Final score: {score}")
                
                break
game(data)