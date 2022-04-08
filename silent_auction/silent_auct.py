from replit import clear
#HINT: You can call clear() to clear the output in the console.
import art
print(art.logo)

auction = {}
end_auction = False

def auction_calc(auction):
  highest_bid = 0
  highest_bidder = ""
  tie = False
  for bidder in auction:
    bid_value = auction[bidder]
    if bid_value > highest_bid:
      highest_bid = bid_value
      highest_bidder = bidder
    elif bid_value == highest_bid:
      print("X")
  if tie == False:
    clear()
    print(f"The highest bidder was {highest_bidder} with a value of £{highest_bid}!")
  elif tie == True:
    clear()
    print(f"The auction is tied! The highest bidders were: X & X with a value of £X")

while end_auction == False:
  name = input("What is the name of the bidder?\n")
  bid = int(input("What value would you like to bid for? \n£"))
  auction[name] = bid
  repeat = input("Would another user like to bid? 'yes' or 'no'\n").lower()
  if repeat == "yes":
    clear()
  elif repeat == "no":
    #print(auction)
    clear()
    end_auction = True
    auction_calc(auction)
  else:
    clear()
    print("You entered something other than 'yes' or 'no', repeating the bid process.")
    