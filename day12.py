

# ============================ Day 12 Lecture Notes:  ============================

################### Scope ####################
#Avoid modifying global scope 
enemies = 1

#Example A 
def increase_enemies():
  # global = Reference a global variable
  print("Global Variable Example:")
  global enemies
  enemies += 1
  print(f"enemies inside function: {enemies}")

increase_enemies()
print(f"enemies outside function: {enemies}")

#Exmple B 
def increase_enemies():
  print("\nReturn Function Example:")
  print(f"enemies inside function: {enemies}")
  return enemies + 1

enemies = increase_enemies()
print(f"enemies outside function: {enemies}\n")
#local scope - exists within functions

def drink_potion():
  potion_strength = 2
  print(potion_strength)

drink_potion()
#cant access potion_strength from outside of the function - it has LOCAL scope - only valid within the drink_potion function 
#print(potion_strength)

#global scope 

player_health = 10

def drink_potion():
  potion_strength = 2
  print(player_health)

drink_potion()

game_level = 3
enemies = ["Skeleton", "Zombie", "Alien"]
if game_level < 5:
  new_enemy = enemies[0]

print(new_enemy)

#if you create a variable within a function, then it is only available within the funtion 

#NameError Vs Syntax Error 