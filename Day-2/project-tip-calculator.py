# This is a project-tip-calculator. The mission of this code is for everyone pay their part.

print("Welcome to the tip calculator")
bill_total = float(input("What was the total bill?: "))
tip_porcentage = int(input("What percentage tip would you like to give? 10, 12, or 15?: "))
many_people = int(input("How many people to slipt the bill?: "))


if tip_porcentage == 12:
    total = (bill_total / many_people) * 1.12
    print(f"Each person should pay: {round(total,2)}")

elif tip_porcentage == 10:
    total = (bill_total / many_people) * 1.10
    print(f"Each person should pay: {round(total,2)}")

elif tip_porcentage == 15:
    total = (bill_total / many_people) * 1.15
    print(f"Each person should pay: {round(total,2)}")
