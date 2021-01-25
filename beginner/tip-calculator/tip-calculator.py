# 1. Create a greeting for your program.
print("Welcome to the tip calculator.")

# 2. Ask for the total bill amount excluded tip.
bill_amount = input("What was the  total bill? $")

# 3. Ask for the percentage tip you like to give.
tip_percentage = input("What percentage of tip would you like to give? 10, 12, or 15? ")

# 4. Ask for the number of people to split the bill.
number_of_people = input("How many people to split the bill? ")

# 5. Calculate the amount that each people should pay.
tip_amount = (int(tip_percentage) / 100) * float(bill_amount)
total_amount = float(bill_amount) + tip_amount
split_bill = total_amount / int(number_of_people)

# 6. Show the result to the user.
print("Each person should pay: ${:.2f}".format(split_bill))