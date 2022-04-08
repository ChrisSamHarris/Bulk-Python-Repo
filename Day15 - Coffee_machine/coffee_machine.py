# Goals:
# TODO: Insert Coffee Emoji into script
# TODO: Resource ammendments - Reflect resource changes to resources list, inclusive of money, water, coffee and milk

MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

money = {
    "quarter": 0.25,
    "dime": 0.10,
    "nickel": 0.05,
    "penny": 0.01,
}

print(5 * money["quarter"])
print(MENU["espresso"]["cost"])
profit = 0
coffee_machine_on = True

def report():
    '''Checks the current resources within the machine inclusive of water, milk, coffee and money'''
    for item in resources:
        if item == 'water' or item == 'milk':
            print(f"{item.title()}: {resources[item]}ml")
        elif item == 'coffee':
            print(f"{item.title()}: {resources[item]}g")
    print(f"Money: ${profit}")

def resource_check(req):
    '''Returns True when order can be made, False if resources are insufficient. Checks that the coffee machine is capable of making the requested drink.'''
    for item in req:
        if req[item] >= resources[item]:
            print(f"Sorry there is not enough {item}.")
            return False
    return True

def money_calc(q, d, n, p):
    '''Determines the total amount of money inputted into the machine.'''
    quarters = q * money["quarter"]
    dimes = d * money["dime"]
    nickels = n * money["nickel"]
    pennys = p * money["penny"]
    return quarters + dimes + nickels + pennys

def brew_coffee(drink_name, order_ingredients):
    '''Deduct the required ingredients from the resources/ report.'''
    for item in order_ingredients:
        resources[item] -= order_ingredients[item]

while coffee_machine_on == True:
    def get_coffee():
        request = input("   What would you like? Espresso, Cappuccino or Latte? ").lower()

        if request == 'shutdown':
            global coffee_machine_on
            coffee_machine_on = False

        elif request != 'report':
            drink = MENU[request]
            if resource_check(drink["ingredients"]):
                print("Please insert coins.")
                coins_q = int(input("How many quarters?"))
                coins_d = int(input("How many dimes?"))
                coins_n = int(input("How many nickles?"))
                coins_p = int(input("How many pennies?"))
                inputted_money = money_calc(q=coins_q, d=coins_d, n=coins_n, p=coins_p)
                #could use round to keep the money to 2 decimal places?
                if inputted_money >= MENU[request]["cost"]:
                    global profit #reference a global variable prior to making ammendments to it
                    profit += MENU[request]["cost"]
                    brew_coffee(request, drink["ingredients"])
                    returned_change = round(inputted_money - MENU[request]["cost"], 2) #rounds the change to 2 decimal places
                    print(f"Here is your ${returned_change} change.")
                    print(f"Here is your {request} ☕️. Enjoy!")
                elif inputted_money < MENU[request]["cost"]:
                    print("Sorry, that's not enough money. Refund issued.")

        elif request == 'report':
            report()

    get_coffee()



