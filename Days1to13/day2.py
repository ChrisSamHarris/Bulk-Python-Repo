# ===== Challenge ==========
#Write a program that adds the digits in a 2 digit number. 
#e.g. if the input was 35, then the output should be 3 + 5 = 8

# 🚨 Don't change the code below 👇
two_digit_number = input("Type a two digit number: ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
print(type(two_digit_number))
new_num0 = int(two_digit_number[0])
new_num1 = int(two_digit_number[1])

final = new_num0 + new_num1
print(final)

### BMI CALCULATOR =====================

# 🚨 Don't change the code below 👇
height = input("enter your height in m: ")
weight = input("enter your weight in kg: ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
height_int = float(height)
weight_int = float(weight)

bmi = (weight_int / (height_int * height_int))
# bmi = (weight_int / (height_int**2))

print(int(bmi))

### How long left calculator =====================

# Create a program using maths and f-Strings that tells us how many days, weeks, months we have left if we live until 90 years old.
# It will take your current age as the input and output a message with our time left in this format:
# You have x days, y weeks, and z months left.

# 🚨 Don't change the code below 👇
age = input("What is your current age?")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
expect = 90 - int(age)
#print(expect)
days = str(expect * 365)
weeks = str(expect * 52)
months =  str(expect * 12)

print(f"You have {days} days, {weeks} weeks, and {months} months left.")


# NOTES =======================

#Data Types
print("Hello"[0])
print("Hello"[4])
print("Hello"[1])

#Integer = Whole Numbers
print(123+345)
print(123_456_789)

#Float = Floating point number
3.14159

#Boolean
True
False

num_char = len(input("What is your name?\n"))
#print(type(num_char))

new_num_char = str(num_char)

print("Your name has " + str(num_char) + " characters.")

# Mathematical operators
3 + 5 
5 - 3
3 * 2
6 / 3 # tends to be a float provided
6 ** 2 #6 to the power of 2 

#PEMDAS/LR - Calculation thats most to the left will be prioritised 
# ()
# **
# * /
# + -

print(3 * 3 + 3 / 3 - 3)
# stage 1 = print((3 * 3) + (3 / 3) - 3)
# stage 1 = print((9 + 1) - 3)
# stage 1 = print(10 - 3)

print(3 * (3 + 3) / 3 - 3)

print(int(8 / 3))
print(round(8 / 3))
print(round(8 / 3, 2))

print("BREAK\n")
print(8 // 3)#converts to an int straight away

result = 4 / 2
result /= 2
print(result)

score = 0 
score += 1

print("your score is " + str(score))

print("BREAK\n")

score1 = 0 
height = 1.8
isWinning= True
#f-string
print(f"your score is {score1}, your height is {height}, your are winning is {isWinning}")
