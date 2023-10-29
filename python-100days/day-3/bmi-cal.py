height = input("enter your height in m: ")
weigth = input("enter your weight in kg: ")

bmi = int(float(weigth) / float(height) ** 2)

if bmi <= 18.5:
    inter = "underweight"
elif bmi <= 25:
    inter = "normalweight"
elif bmi <= 30:
    inter = "overweight"
elif bmi <= 35:
    inter = "obese"
else:
    inter = "clinically obese"
print(f"Your BMI is {bmi}, you are {inter}")