# ============================ Challenge 1:  ============================
#https://reeborg.ca/reeborg.html?lang=en&mode=python&menu=worlds%2Fmenus%2Freeborg_intro_en.json&name=Maze&url=worlds%2Ftutorial_en%2Fmaze1.json
#hurdle 1 
#hurdle 2
#hurdle 3
#maze
def turn_around():
    turn_left()
    turn_left()
    
def turn_right():
    turn_left()
    turn_left()
    turn_left()

def draw_sq():
    turn_left()
    move()
    turn_right()
    move()
    turn_right()
    move()
    turn_right()
    move()
    
def jump():
    turn_left()
    move()
    turn_right()
    move()
    turn_right()
    move()
    turn_left()
    
while at_goal() != True:
    if front_is_clear() == True:
        move()
    elif wall_in_front() == True:
        jump()
    

#while not at_goal():
#jump()

#for i in range(6):
#    jump()

#Hurdles 4 - Reeborgs world 
def turn_right():
    turn_left()
    turn_left()
    turn_left()

#Solution for Hurdles with Variable Heights 

while not at_goal():
    if front_is_clear():
        move()
        if right_is_clear():
            turn_right()
    elif wall_in_front():
        turn_left()