
from art import secret_logo
import os


def clear():
    # CLEAR THE SCREEN
    os.system('cls')
 

def find_highest_bidders(bidders_record):
    highest_bid = 0
    winner = ""
    for bidder in bidders_record:
        bid_amount = bidders_record[bidder]
        if bid_amount > highest_bid:
            highest_bid = bid_amount
            winner = bidder
    print(f"The winner is {winner} with a bid of ${highest_bid}")


print(secret_logo)
print("Welcome to the secret auction program.")
bids = {}

bidding_finished = False

while not bidding_finished:
    name = input("What is your name?: ")
    price = int(input("What's your bid?: $"))
    bids[name] = price
    should_continue = input(
        "Are there any other bidders? Type 'yes' or 'no'.\n")
    if should_continue == 'no':
        bidding_finished = True
        clear()
        find_highest_bidders(bidders_record=bids)
        print(bids)
    elif should_continue == 'yes':
        clear()
