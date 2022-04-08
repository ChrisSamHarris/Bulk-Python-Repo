#Take a big project and break the project down into smaller problems on a 1by1 basis
import random
from replit import clear
from game_data import data
from art import logo, vs

#======= MetaData =======
def format_data(account):
  '''Format the account data into a printable format.'''
  account_name = account['name']
  account_desc = account['description']
  account_country = account['country']
  return f"{account_name}, a {account_desc}, from {account_country}"

def check_answer(guess, a_followers, b_followers):
  '''Take the user guess and follower counts and returns if the user got the answer correct.'''
  if a_followers > b_followers:
    #Return true or false, is the user wrong or right?
    return guess == "A"
  else:
    return guess == "B"


# ======== Main Code ======
#Display logo
print(logo)
score = 0
game_should_continue = True
#Make account as position B become the next account at Position A if its the correct answer 
# As this is executed outside of the while loop - Within the loop the value of 'account_b' persists in-memory and as the loop repeats it is assigned to account_a (account_a = account_b) and then a new value is assigned to 'account_b'
account_b = random.choice(data)

#Make game repeatable
while game_should_continue == True:
  
  #Generate a random perosona(account) fo game data
  account_a = account_b
  account_b = random.choice(data)
  if account_a == account_b:
    account_b = random.choice(data)
  
  #format the account data into a printable format
  # print(f"{account_a['name']}, a {account_a['description']}, from {account_a['country']}")
  print(f"Compare A: {format_data(account_a)}.")
  print(vs)
  print(f"Against B: {format_data(account_b)}.")
  
  #Ask user for a guess
  guess = input("Who has more followers? Type 'A' or 'B'.").upper()
  
  #Check if the user is correct
  ##Getfollower count of each account
  a_follower_count = account_a['follower_count']
  b_follower_count = account_b['follower_count']
  
  is_correct = check_answer(guess, a_follower_count, b_follower_count)

  #Clear the screen inbetween rounds 
  clear()
  print(logo)
  
  ##Use if statement to check if user is correct
  #Give user feedback on their guess  
  if is_correct:
    score += 1 
    print(f"You're right. Current Score: {score}.")
  else:
    game_should_continue = False
    clear()
    print(f"You're wrong. Your Final Score: {score}.")
  
  #Score keeping
  
  
