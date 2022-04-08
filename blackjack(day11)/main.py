############### Blackjack Project #####################

#Difficulty Normal 😎: Use all Hints below to complete the project.
#Difficulty Hard 🤔: Use only Hints 1, 2, 3 to complete the project.
#Difficulty Extra Hard 😭: Only use Hints 1 & 2 to complete the project.
#Difficulty Expert 🤯: Only use Hint 1 to complete the project.

############### Our Blackjack House Rules #####################

## The deck is unlimited in size. 
## There are no jokers. 
## The Jack/Queen/King all count as 10.
## The the Ace can count as 11 or 1.
## The cards in the list have equal probability of being drawn.
## Cards are not removed from the deck as they are drawn.
## The computer is the dealer.

##################### Hints #####################
import random
import art
from replit import clear 
#Hint 1: http://blackjack-final.appbrewery.repl.run

#Hint 3: Download and read this flow chart I've created: 
#   https://drive.google.com/uc?export=download&id=1rDkiHCrhaf9eX7u7yjM1qwSuyEk-rPnt

#Hint 4: Create a deal_card() function that uses the List below to *return* a random card.
#11 is the Ace.
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

def blackjack():
  print(art.logo)
  print("\nWelcome to Blackjack! \n")
  
  def deal_card():
    """Deals a blackjack card to both the user and the dealer"""
    card = random.choice(cards)
    return card
  
  #Hint 6: Create a function called calculate_score() that takes a List of cards as input 
  #and returns the score. 
  #Look up the sum() function to help you do this.
  #Hint 7: Inside calculate_score() check for a blackjack (a hand with only 2 cards: ace + 10) and return 0 instead of the actual score. 0 will represent a blackjack in our game.
  def calculate_score(cards):
    """Take a list of cards and return the blackjack score, calculated from the cards"""
    if sum(cards) == 21 and len(cards) == 2:
      return 0 
  #Hint 8: Inside calculate_score() check for an 11 (ace). If the score is already over 21, remove the 11 and replace it with a 1. You might need to look up append() and remove().
    if 11 in cards and sum(cards) > 21:
      cards.remove(11)
      cards.append(1)
    score = sum(cards)
    return score
    
  #Hint 5: Deal the user and computer 2 cards each using deal_card() and append().
  user_cards = []
  dealer_cards = []
  is_game_over = False
  
  for i in range(2):
    user_cards.append(deal_card())
    dealer_cards.append(deal_card())
  
  #Hint 9: Call calculate_score(). If the computer or the user has a blackjack (0) or if the user's score is over 21, then the game ends.
  user_score = calculate_score(user_cards)
  dealer_score = calculate_score(dealer_cards)
  
  print(f"Your cards: {user_cards}, current score: {user_score}")
  print(f"Dealers first card: {dealer_cards[0]}\n")
  
  #Hint 10: If the game has not ended, ask the user if they want to draw another card. If yes, then use the deal_card() function to add another card to the user_cards List. If no, then the game has ended.
  while is_game_over == False:
    if user_score == 0:
      is_game_over = True
      print(f"You won Blackjack with 21!")
    elif dealer_score == 0:
      is_game_over = True
      print(f"The dealer won blackjack with 21! You lose!")
    elif user_score > 21:
      is_game_over = True
      #print(f"You exceeded 21! You lose!")
    else:
      carry_on = input("Do you want to draw another card. Type 'Y' for yes and 'N' for no.\n").lower()
      if carry_on == 'y':
        user_cards.append(deal_card())
        user_score = calculate_score(user_cards)
        print(f"Your cards: {user_cards}, current score : {user_score}")      
      elif carry_on == 'n':
        is_game_over = True
  
  while dealer_score < 17:
    dealer_cards.append(deal_card())
    dealer_score = calculate_score(dealer_cards)
  
  def compare(usr, dlr):
    """Compares the blackjack scores of both the user and dealer in relation to 21. This function determines whether the user has lost, drawn or won."""
    if usr == dlr:
      print(f"You both have the score {usr}. Its a Draw!")
    elif dlr == 0:
      print("The Dealer has Blackjack! You lose!")
    elif usr == 0:
      print("You have Blackjack! You win!")
    elif usr > 21:
      print("You have gone bust! You Lose!")
    elif dlr > 21:
      print("The Dealer has gone bust! You Win!")
    else:
      if usr > dlr:
        print(f"Your final hand is  {usr}, whereas the dealer has a final hand of {dlr}. You Win!")
      else:
        print(f"Your final hand is  {usr}, whereas the dealer has a final hand of {dlr}. You Lose!")
      
  compare(usr = user_score, dlr = dealer_score)
  restart = input("\n \nDo you want to restart the game? Type 'Y' for Yes and 'N' for No. \n").upper()

  if restart == 'Y':
    clear()
    blackjack()
  elif restart == 'N':
    clear()
    print("Goodbye!")
  

blackjack()   
  
#Hint 11: The score will need to be rechecked with every new card drawn and the checks in Hint 9 need to be repeated until the game ends.
      
#Hint 12: Once the user is done, it's time to let the computer play. The computer should keep drawing cards as long as it has a score less than 17.

#Hint 13: Create a function called compare() and pass in the user_score and computer_score. If the computer and user both have the same score, then it's a draw. If the computer has a blackjack (0), then the user loses. If the user has a blackjack (0), then the user wins. If the user_score is over 21, then the user loses. If the computer_score is over 21, then the computer loses. If none of the above, then the player with the highest score wins.

#Hint 14: Ask the user if they want to restart the game. If they answer yes, clear the console and start a new game of blackjack and show the logo from art.py.

