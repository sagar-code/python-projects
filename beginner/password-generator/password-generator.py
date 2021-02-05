import random

# 0. Variable assigning for the password
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

# 1. Create a greeting for your program.
print("Welcome to the PyPassword Generator!")

# 2. Take the input from the user.
nr_letters= int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input("How many symbols would you like?\n"))
nr_numbers = int(input("How many numbers would you like?\n"))

# 3. Logic for the password generator.
password = []

for char in range(1, nr_letters+1):
    password.extend(random.choice(letters))

for sym in range(1, nr_symbols+1):
    password.extend(random.choice(symbols))

for num in range(1, nr_numbers+1):
    password.extend(random.choice(numbers))

# 4. Shuffle the  password.
random.shuffle(password)

# 5. Print the password in string.
final_password = ''.join(password)
print(f"Your password is: {final_password}")