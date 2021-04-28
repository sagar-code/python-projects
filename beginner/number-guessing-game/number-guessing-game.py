import random
from art import logo

EASY_LEVEL_TURN = 10
HARD_LEVEL_TURN = 5


def check_difficult():
    difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ")
    if difficulty == "hard":
        return HARD_LEVEL_TURN
    else:
        return EASY_LEVEL_TURN


# function to check user's guess against actual answer
def check_answer(answer_number, guess_number, turns):
    """check answer against guess and return the number of turns remaining"""
    if guess_number > answer_number:
        print("Too high.")
        return turns - 1
    elif guess_number < answer_number:
        print("Too low.")
        return turns - 1
    else:
        print(f"You got it! The answer was {answer_number}")


# let user guess the numbers
def game():
    print(logo)
    print("I'm thinking of a number between 1 and 100.")

    random_number = random.randint(1, 100)
    print(f"Psst, the correct answer is {random_number}")

    turns = check_difficult()
    guess = 0
    while guess != random_number:
        guess = int(input("Make a guess: "))

        turns = check_answer(random_number, guess, turns)

        if turns == 0:
            print("You run out of guesses. You lose")
            return
        elif guess != random_number:
            print(f"You have {turns} attempts remaining to guess the number.")
            print("Guess again")


game()


