from replit import clear
import art

#Calculator functions
def add(n1, n2):
  return n1 + n2
  
def subtract(n1, n2):
  return n1 - n2
  
def multiply(n1, n2):
  return n1 * n2

def divide(n1, n2):
  return n1 / n2

#Print vs return
#return - can be used as an input to another function - can build on the value iteratively

operations = {
  "+": add,
  "-": subtract,
  "*": multiply,
  "/": divide,
  }

def calculator():
  print(art.logo)
  
  num1 = float(input("Whats the first number? : "))
  num2 = float(input("Whats the second number? : "))
  
  for key in operations:
    print(key)
    
  operation_symbol = input("Pick an operation from the line above : ")
  calculation_function = operations[operation_symbol]
  answer = calculation_function(num1, num2)
  
  print(f"{num1} {operation_symbol} {num2} = {answer}.")
  
  progress = True
  while progress == True:
    progress_input = input(f"Type 'y' to continue calculating with {answer}, or type 'n' to start a new calculation. : \n").lower()
    if progress_input == "y":
      num1 = answer
      operation_progress = input("Pick an operation : ")
      num2 = float(input("What's the next number? : "))
      calculation_function = operations[operation_progress]
      progress_answer = calculation_function(num1, num2)
      print(f"{num1} {operation_progress} {num2} = {progress_answer}")
    else:
      progress = False
      clear()
      calculator()

calculator()
#Recursion^ - Starting the function again^ - Referenced to exit the while loop