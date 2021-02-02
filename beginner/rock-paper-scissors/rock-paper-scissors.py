# 0. Calling require modules.
import random

# 1. Create a greeting for your user.
print("Welcome to the Rock, Paper and Scissor game.")

# 2. Create an image for rock, paper and scissors.
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

# 3. Get the image in the list for easier computation.
game_images = [rock, paper, scissors]

# 4. Get the input from the user.
user_input = int(input("What do you want to choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))

# 5. Show the user input as an image.
if 0 <= user_input < 3:
    print(game_images[user_input])
else:
    print("You have enter a wrong input. Please, try again!")
    exit()

# 6. Computer choice randomly
computer_choice = random.randint(0, 2)
print(game_images[computer_choice])

# 7. Making a victory chart.
computer_rock = ["Draw", "User Win", "Computer Win"]
computer_paper = ["Computer Win", "Draw", "User Win"]
computer_scissors = ["User Win", "Computer Win", "Draw"]

victory_chart = [computer_rock, computer_paper, computer_scissors]

# 8. Result of the game.
print(victory_chart[computer_choice][user_input])