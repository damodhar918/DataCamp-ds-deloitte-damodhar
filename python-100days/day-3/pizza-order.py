print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M, or L ")
add_pepperoni = input("Do you want pepperoni? Y or N ")
extra_cheese = input("Do you want extra cheese? Y or N ")

bill = 0
extraPepPr = 3
extraCheesePr = 1
if size == "S":
    bill = 15
    extraPep = 2
elif size == "M":
    bill = 20
else:
    bill = 25

if add_pepperoni == "Y":
    bill += extraPepPr
if extra_cheese == "Y":
    bill += extraCheesePr

print(f"Your final bill is: {bill}")