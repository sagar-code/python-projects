# 1. Create a greeting for your program.
print("Welcome to the BMI calculator.")

# 2. Ask for the height and weight in meter and kg respectively.
height = float(input("Enter your height in m: "))
weight = float(input("Enter your weight in kg: "))

# 3. Calculate the bmi.
bmi = round(weight / (height ** 2))

# 4. Shows the result.
if bmi < 18.5:
    print(f"Your bmi is {bmi}, you are\033[1m underweight\033[0m.")
elif bmi < 25:
    print(f"Your bmi is {bmi}, you have a\033[1m normal weight\033[0m.")
elif bmi < 30:
    print(f"Your bmi is {bmi}, you are slightly\033[1m overweight\033[0m.")
elif bmi < 35:
    print(f"Your bmi is {bmi}, you are\033[1m obese\033[0m.")
else:
    print(f"Your bmi is {bmi}, you are\033[1m clinically obese\033[0m.")