from blind_auction_art import gavel
import os
from time import sleep

not_finished=True
bidder_and_bid={}

def add_bidder(bidder_name, bidder_price):
    bidder_and_bid[bidder_name]=bidder_price

#bidding record will be bidder_and_bid dict
def who_won(bidding_record):
   highest_amount=0
   winner=""
   for bidder in bidding_record:
      bid_amount=bidding_record[bidder]
      if bid_amount > highest_amount:
         highest_amount=bid_amount
         winner=bidder
   print(f"The winner is {winner} with ${highest_amount}!")

print (gavel)
print("Welcome to the blind auction!")

while not_finished:
  user_name = input("What is your name? ")
  while True:
    try:
        user_bid = int(input("What's your bid? "))
    except ValueError:
        print("Sorry, try typing just the numbers")
        continue
    else:
        break  
  add_bidder(user_name, user_bid)

  restart=input("Type 'yes' if there are other bidders.\nOtherwise, type 'no'.\n")
  restart=restart.lower()
  if restart=='yes':
     print("This screen will clear out in a moment.")
     sleep(1)
     os.system('cls')
  if restart=='no':
    not_finished=False

who_won(bidder_and_bid)
