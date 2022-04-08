#Doesnt format correctly - doesnt have logo or clear after answer 

from game_data import data
import random
from art import logo, vs
 
A = random.choice(data)
B = random.choice(data)
 
print(logo)
 
game_over = False
score = 0
 
while not game_over:
    print(f"Please compare which has the higher followers between: {A['name']}, {A['description']}, {A['country']}")
    print(vs)
    print(f"{B['name']}, {B['description']}, {B['country']}")
    choice = input("Please type A or B: ")
    if choice == 'A':
        if A['follower_count'] > B['follower_count']:
            score += 1
            print(f"correct, your score is now {score}")
            A = B
            B = random.choice(data)
        elif A['follower_count'] < B['follower_count']:
            print(f"incorrect, your final score is {score}")
            game_over = True
    elif choice == 'B':
        if B['follower_count'] > A['follower_count']:
            score += 1
            print(f"correct, your score is now {score}")
            A = B
            B = random.choice(data)
        elif B['follower_count'] < A['follower_count']:
            print(f"Incorrect, your score is now {score}")
            game_over = True