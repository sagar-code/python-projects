import random
import os
from art import logo


# Give two card to the user and computer
def deal_card():
    """Return a random card from the deck"""
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card = random.choice(cards)
    return card


# check who win the game
def compare(user_scores, computer_scores):
    if user_scores == computer_scores:
        return "Draw 😮"
    elif computer_scores == 0:
        return "Lose, opponent has a Blackjack 😲"
    elif user_scores == 0:
        return "Win with a Blackjack 🤠"
    elif user_scores > 21:
        return "You went over. You lose 😞"
    elif computer_scores > 21:
        return "Opponent went over. You win 🙂"
    elif user_scores > computer_scores:
        return "You win 🙂"
    else:
        return "You lose ☹"


def play_game():

    print(logo)

    user_cards = []
    computer_cards = []
    is_game_over = False

    for _ in range(2):
        user_cards.append(deal_card())
        computer_cards.append(deal_card())

    # function to take list of card and return a score
    def calculate_score(cards: list) -> int:
        # test for blackjack and return 0 if its blackjack
        if sum(cards) == 21 and len(cards) == 2:
            return 0
        # if score is greater than 21 and it contain 11 the replace it with 1
        if 11 in cards and sum(cards) > 21:
            cards.remove(11)
            cards.append(1)

        return sum(cards)

    while not is_game_over:
        user_score = calculate_score(user_cards)
        computer_score = calculate_score(computer_cards)

        print(f"Your cards: {user_cards}, current score: {user_score}")
        print(f"Computer's first cards: {computer_cards[0]}")

        # check if user has blackjack or if user's score > 21, then game ends
        if user_score == 0 or computer_score == 0 or user_score > 21:
            is_game_over = True
        else:
            # check if the game is over or not and ask the user to pass or play
            user_should_deal = input("Type 'y' to get another card, type 'n' to pass: ")
            if user_should_deal == "y":
                user_cards.append(deal_card())
            else:
                is_game_over = True

    # if the user is done, it's time for computer to play. Computer should draw a card until the score is greater
    # the 17
    while computer_score != 0 and computer_score < 17:
        computer_cards.append(deal_card())
        computer_score = calculate_score(computer_cards)

    print(f"Your final hand: {user_cards}, final score: {user_score}")
    print(f"Computer's final hand: {computer_cards}, final score: {computer_score}")
    print(compare(user_score, computer_score))


# ask the user if they want to play game again or not
while input("Do you want to play a game again? Type 'y' or 'n': ") == 'y':
    os.system('clear')
    play_game()