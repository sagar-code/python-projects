import os
import random
from art import logo, vs
from game_data import data


def format_data(account):
    """format the account data into printable format"""
    account_name = account["name"]
    account_description = account["description"]
    account_country = account["country"]

    return f"{account_name}, a {account_description}, from {account_country}"


def check_answer(guess_, a_followers, b_followers):
    """check if the user is right or not"""
    if a_followers > b_followers:
        return guess_ == "a"
    else:
        return guess_ == "b"


# display art
print(logo)

score = 0
game_should_continue = True
account_b = random.choice(data)

# make the game repeatable
while game_should_continue:
    # generate a random account form the game data
    account_a = account_b
    account_b = random.choice(data)

    while account_a == account_b:
        account_b = random.choice(data)

    print(f"Compare A: {format_data(account_a)}.")
    print(vs)
    print(f"Compare B: {format_data(account_b)}.")

    # ask user for a guess
    guess = input("Who has more followers? Type 'A' or 'B': ").lower()

    # check if user is correct:
    # get follower count of each account
    # user if statement if the user is correct or not
    a_follower_count = account_a["follower_count"]
    b_follower_count = account_b["follower_count"]

    is_correct = check_answer(guess, a_follower_count, b_follower_count)

    os.system("clear")
    print(logo)

    # give user feedback on their guess
    if is_correct:
        # score keeping
        score += 1
        print(f"You're right! Current score: {score}")
    else:
        game_should_continue = False
        print(f"Sorry, that's wrong. Final score: {score}")

