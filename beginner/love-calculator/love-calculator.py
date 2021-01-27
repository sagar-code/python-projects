# 1. Create a greeting for your program.
print("Welcome to the love calculator!")

# 2. Get the name form the user.
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")

# 3. Combine the name and convert it into lowercase.
combined_name = name1 + name2
lower_case_name = combined_name.lower()

# 4. Count the number of item from lower_case_name in true.
t = lower_case_name.count("t")
r = lower_case_name.count("r")
u = lower_case_name.count("u")
e = lower_case_name.count("e")

true = t + r + u + e

# 5. Count the number of item from lower_case_name in love.
l = lower_case_name.count("l")
o = lower_case_name.count("o")
v = lower_case_name.count("v")
e = lower_case_name.count("e")

love = l + o + v + e

# 6. Get the love score.
love_score = int(str(true) + str(love))

# 7. Get the conditions.
if (love_score < 10) or (love_score > 90):
    print(f"Your love score is {love_score}, you go together like coke and mentos.")

elif (love_score >= 40) and (love_score <= 50):
    print(f"Your score is {love_score}, you are alright together.")
else:
    print(f"Your score is {love_score}.")
