# The class is about nested if and else statements.

# Using the same example as the last class. If the person is more than 18 years pay 12 dollars, 
# if less than 18 years is 7 dollars.

print("Welcome to the rollercoaster !!")

height = int(input("What is your height in cm ?: "))

if height >= 120:
    print("You can ride the rollercoaster!")
    age = int(input("What is your age ?: "))
    if age < 12:
        print("Please pay $5")
    elif age <= 18:
        print("Please pay $7")
    else:
        print("Please pay $12")
else:
    print("Sorry, you have to grow taller before you can ride")

# Now your boss wants one more condition. The people below than 12 years pay $5.
# So to complete that condition, you need use the elif condition. You can use many elif.