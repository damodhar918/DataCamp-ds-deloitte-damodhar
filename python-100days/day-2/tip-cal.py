print("Welcome to the tip calculator.")
total_bill = float(input("What was the total bill? $"))
tip_percentage = float(input("What percentage tip would you like to give? 10, 12, or 15? "))
num_people = int(input("How many people to split the bill? "))
total = total_bill * tip_percentage / 100  + total_bill
result = round(total / num_people,2)
print(f"Each person should pay: ${result}")