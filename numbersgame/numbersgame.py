#Number Guessing Game Objectives:
import art
import random
from replit import clear

EASY_DIFFICULTY = 10
HARD_DIFFICULTY = 5 

def set_difficulty():
  player_difficulty = input("Choose a difficulty. Type 'easy' or 'hard':  ").lower()
  if player_difficulty == 'easy':
    return EASY_DIFFICULTY
  elif player_difficulty == 'hard':
    return HARD_DIFFICULTY

def check_answer(guess, chosen_num, num_of_lives):
  if guess > chosen_num:
    print("Too high.")
    return num_of_lives - 1 
  elif guess < chosen_num:
    print("Too low. \nGuess again.")
    return num_of_lives - 1
  elif guess == chosen_num:
    print(f"Correct! You found the right number {chosen_num}!")

def numbers_game():
  print(art.logo)
  numbers = []
  
  print("Welcome to 'Numbers Game'")
  print("Im thinking of a number between 1 and 100.")
  
  #Long
  for num in range(1, 101):
    numbers.append(num)
  chosen_num = random.choice(numbers)
  #Short OR chosen_num = random.randint(1, 101)
  print(chosen_num)

  
  num_of_lives = set_difficulty()
  guess = 0 
  while guess != chosen_num:
    print(f"You have {num_of_lives} attempts remaining to guess the number.")
    
    guess = int(input("Make a guess: "))
    num_of_lives = check_answer(guess, chosen_num, num_of_lives)
    
    if num_of_lives == 0:
      print("You've run out of lives, you lose.")
      #return - Exits from the programme (no repeat)
    elif guess != chosen_num:
      print("Guess again.")
    
  repeat = input("\n\nWould you like to play again? Type 'Y' for yes or 'N' for no.").lower()
  if repeat == 'y':
    clear()
    numbers_game()

numbers_game()
# Include an ASCII art logo.
# Allow the player to submit a guess for a number between 1 and 100.
# Check user's guess against actual answer. Print "Too high." or "Too low." depending on the user's answer. 
# If they got the answer correct, show the actual answer to the player.
# Track the number of turns remaining.
# If they run out of turns, provide feedback to the player. 
# Include two different difficulty levels (e.g., 10 guesses in easy mode, only 5 guesses in hard mode).

