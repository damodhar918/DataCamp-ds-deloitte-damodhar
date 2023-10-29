print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")

TRUE = "true"
LOVE = "love"
count1 = 0
count2 = 0
for letter in TRUE:
    count1 += name1.lower().count(letter) + name2.lower().count(letter)
for letter in LOVE:
    count2 += name2.lower().count(letter) + name1.lower().count(letter)

score = count1*10+count2

if score < 10 or score > 90:
    message = ", you go together like coke and mentos."
elif 40 <= score <=50:
    message = ", you are alright together."
else:
    message = "."

print(f"Your score is {score}{message}")
