import os
from art import logo

print(logo)

bids = {}
bidding_finished = False


def highest_bidder(bids_):
    result = max(bids_, key=lambda x: bids_[x])
    return result


while not bidding_finished:
    name = input("What is your name: \n")
    price = int(input("What is your bid? \n$"))

    bids[name] = price

    should_continue = input("Are there any bidders? Type 'yes' or 'no'.")
    if should_continue == "no":
        bidding_finished = True
    elif should_continue == "yes":
        pass


winner = highest_bidder(bids)
print(f"The winner is {winner} with a bidding price of {bids[winner]}.")


