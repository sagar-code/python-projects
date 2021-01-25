# 1. Create a greeting for your program.
print("Welcome to the leap year checker.")

# 2. Ask for the year to check.
year = int(input("Which year do you want to check? "))

# 3. Program to check leap year or not.
if year % 4 == 0:
    if year % 100 == 0:
        if year % 400 == 0:
            print("Leap year.")
        else:
            print("Not leap year.")
    else:
        print("Leap year.")
else:
    print("Not leap year.")