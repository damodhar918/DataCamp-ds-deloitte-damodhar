age = int(input("What is your current age?"))
timeLeft = 90 - age
timeLeftWeek = timeLeft * 52
timeLeftDay = timeLeft * 365
timeLeftHour = timeLeftDay * 24
timeLeftMonth = timeLeft * 12

print(f"You have {timeLeftHour} hours / {timeLeftDay} days / {timeLeftWeek} weeks / {timeLeftMonth} months left")
