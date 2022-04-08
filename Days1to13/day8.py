# ============================ Challenge 1: Paint Area Calculator ============================
import math
user_height = int(input("Height of wall: "))
user_width = int(input("Width of wall: "))
coverage = 5

def required_paint(height, width):
    amount = int(math.ceil((height * width) / coverage))
    print(f"You'll need {amount} cans of paint")

required_paint(user_height, user_width)

# ============================ Challenge 2: Prime number checker  ============================
def prime_checker(number):
    is_prime = True
    for i in range(2, number):
        if number % i == 0:
            is_prime = False
    if is_prime == True:
        print("Is a prime number.")
    else:
        print("Is not a prime number.")

n = int(input("Check this number: "))
prime_checker(number=n)

# ============================ Day 8 Lecture Notes:  ============================
# Review: 
# Create a function called greet(). 
# Write 3 print statements inside the function.
# Call the greet() function and run your code.

def greet_range():
  for num in range(0, 3):
    print("Ello'")

def greet():
  print("Ello'")
  print("Ello'")
  print("Ello'")

#Function that allows for input 
# =====
#function_title(parameter):
  #define

# =====
#function_title(arguement)
# def greet_name(name):
#   print(f"Hello {name}!")

# greet_name("Billie")

#Functions with more than one input
def greet_with(name, location):
  print(f"Hello {name}.")
  print(f"What is the weather like in {location}?")
#Positional Arguement
greet_with("Chris", "Manchester")

#keyword arguement
greet_with(location="Manchester", name="Chris")