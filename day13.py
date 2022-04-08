############DEBUGGING#####################

# # Describe Problem
def my_function():
  for i in range(1, 21):
    #error was incorrect as the original range was (1, 20) - Range doesnt include the latest number so increased to 21
    if i == 20:
      print("You got it\n")
my_function()

# # Reproduce the Bug
from random import randint
dice_imgs = ["❶", "❷", "❸", "❹", "❺", "❻"]
dice_num = randint(0, 5)
#Index was incorrect - original value = randint(1, 6) - This is out of range as the list index is 0, 5
print(dice_imgs[dice_num])

# # Play Computer
year = int(input("What's your year of birth?\n"))
if year > 1980 and year <= 1994:
  #There was no = for 1994 so it return no value - no bucket to catch 
  print("You are a millenial.")
elif year > 1994:
  print("You are a Gen Z.\n")

# # Fix the Errors
age = int(input("How old are you?\n"))
if age >= 18:
  print(f"You can drive at age {age}.\n")

# #Print is Your Friend
pages = 0
word_per_page = 0
pages = int(input("Number of pages: "))
word_per_page = int(input("Number of words per page: "))

total_words = pages * word_per_page
print(f"{total_words}")

# #Use a Debugger
def mutate(a_list):
  b_list = []
  for item in a_list:
    new_item = item * 2
    b_list.append(new_item)
  print(b_list)

mutate([1,2,3,5,8,13])

# debugger tool to use  = python tutor 