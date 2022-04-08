print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.") 

#https://www.draw.io/?lightbox=1&highlight=0000ff&edit=_blank&layers=1&nav=1&title=Treasure%20Island%20Conditional.drawio#Uhttps%3A%2F%2Fdrive.google.com%2Fuc%3Fid%3D1oDe4ehjWZipYRsVfeAx2HyB7LCQ8_Fvi%26export%3Ddownload

#Write your code below this line 👇
#ascii art 
left_right = input('''You'\re coming to the end of your journey, a road splits left and right.\nWhich path do you take? Type "left" or "right"''').lower()
print(left_right)

if left_right == "left":
  swim_boat = input('You reach the end of the road and are greeted by a lake, you have the choice of attempting to swim or waiting for a boat. \nDo you swim or wait? Type "swim" or "wait". ').lower()
  if swim_boat == "wait":
    door = input('You successfully make it across the water. \nAfter crossing some land you find a castle, of which has three doors. \nYou can pick one door and one alone, do you choose "Red", "Yellow" or "Blue"? ').lower()
    if door == "red":
      print("You are burned by ifre. Game Over.")
    elif door == "yellow":
      print("You find the treasure and Win the Game!")
    elif door == "blue":
      print("You are killed by a stray cat. Game Over.")
    else: 
      print("Wrong Answer. Game Over.")
  else:
    print("You drown. Game Over.")
elif left_right == "right":
  print("You fall into a hole and die. Game Over.")
else: 
  print("Wrong Answer. Game Over.")