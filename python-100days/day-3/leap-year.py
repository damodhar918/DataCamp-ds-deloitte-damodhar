year = int(input("Which year you want to check? "))
if year%4 == 0:
    if year%100 == 0:
        leap = False
        if year%400 == 0:
            leap = True
    else:
        leap = True
else:
    leap = False

if leap:
    print(f"{year} is a leap year")
else:
    print(f"{year} is not a leap year")