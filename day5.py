# ============================ Challenge 1: Average Height ============================
# 🚨 Don't change the code below 👇
student_heights = input("Input a list of student heights ").split()
for n in range(0, len(student_heights)):
  student_heights[n] = int(student_heights[n])
# 🚨 Don't change the code above 👆

#Write your code below this row 👇
total_height = 0 
list_count = 0

for height in student_heights:
    total_height += height 
    list_count += 1

print(round(total_height / list_count))

# ============================ Challenge 2: High Score ============================
# 🚨 Don't change the code below 👇
student_scores = input("Input a list of student scores ").split()
for n in range(0, len(student_scores)):
  student_scores[n] = int(student_scores[n])
print(student_scores)
# 🚨 Don't change the code above 👆

#Write your code below this row 👇
highest_score = 0 

for score in student_scores:
    if score > highest_score:
        highest_score = score

print(f"The highest score in the class is: {highest_score}")

# ============================ Challenge 3: Adding Even Numbers ============================
#Write your code below this row 👇
total_even = 0
#for number in range(2, 101, 2):
for number in range(1, 101):
    if number % 2 == 0:
        total_even += number

print(total_even)

# ============================ Challenge 4: FizzBuzz  ============================
#Write your code below this row 👇
for number in range(1, 101):
    #if number % 3 == 0 and number % 5 ==0:
    if number % 15 == 0:
        print("FizzBuzz")
    elif number % 5 == 0:
        print("Buzz")
    elif number % 3 == 0:
        print("Fizz")
    else:
        print(number)


# ============================ Day 5 Lecture Notes:  ============================

#Loops
fruits = ["Apple", "Peach", "Pear"]

for fruit in fruits: 
  print(fruit)
  print(fruit + " Pie")

#Range Function
total = 0

for number in range(2, 101, 2):
  #doesnt include the last digit
  print(number)

for number in range(1, 101):
  total += number
print(total)