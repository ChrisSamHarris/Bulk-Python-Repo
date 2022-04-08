import random 
# ============================ Challenge 1: Heads or Tails ============================
random_float = random.random()
#random_side = random.randint(0, 1)
random_heads_tails = random_float * 2

print(random_heads_tails)
if random_heads_tails >= 1: 
    print("Heads")
else: 
    print("Tails")
# ============================ Challenge 2: Banker Roulette  ============================
# Split string method
names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(", ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
# ---- Option A ----
total_num_items = (len(names))
# generate random numbers between 0 and number of items in the list (index at 0)
random_choice = random.randint(0, total_num_items - 1)
person_who_will_pay = names[random_choice]
print(f"{person_who_will_pay} is going to buy the meal today!")

# ----- Option B -----
random_name = random.choice(names)
print(f"{random_name} is going to buy the meal today!")

# ============================ Challenge 3: Treasure Map  ============================
# 🚨 Don't change the code below 👇
row1 = ["⬜️","⬜️","⬜️"]
row2 = ["⬜️","⬜️","⬜️"]
row3 = ["⬜️","⬜️","⬜️"]
map = [row1, row2, row3]
print(f"{row1}\n{row2}\n{row3}")
position = input("Where do you want to put the treasure? ")
# 🚨 Don't change the code above 👆

#Write your code below this row 👇
horizontal = int(position[0])
vertical = int(position[1])

selected_row = (map[vertical - 1])
selected_row[horizontal - 1] = "X"
# map[vertical - 1][horizontal - 1] = "X"

# 🚨 Don't change the code below 👇
print(f"{row1}\n{row2}\n{row3}")

# ============================ Day 4 Lecture Notes:  ============================
import random

random_integer = random.randint(100, 200)
print(random_integer)

random_float = random.random()
print(random_float)

#random float between 0 & 5: 
random_0to5 = random_float * 5 

#lists
england_cities = ["London", "Manchester", "Newcastle"]

england_cities[2] = "Sunderland"

england_cities.append("Leeds")
england_cities.extend(["Derby","Lancaster"])

num_of_cities = (len(england_cities))

print(england_cities[-1])

scottish_cities = ["Glasgow", "Edingburgh", "Inverness"]

eng_scot_cities = [england_cities, scottish_cities]
print(eng_scot_cities)
print(eng_scot_cities[1][2])