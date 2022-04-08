from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

is_coffee_machine_on = True

money_machine = MoneyMachine()
coffee_maker = CoffeeMaker()
menu = Menu()

print("Coffee Machine Loading... \n")

print("Starting Report:")
money_machine.report()
coffee_maker.report()
print("\n")

#Having just "while is_coffee_machine_on:" skips the pre-text? 
while is_coffee_machine_on == True:
    options = menu.get_items()
    order_name = input(f"What drink would you like today? {options}?").lower()
    if order_name == "shutdown":
        print("Coffee Machine is switching off. Goodbye.")
        is_coffee_machine_on = False
    elif order_name == "report":
        money_machine.report()
        coffee_maker.report()
    else:
        drink = menu.find_drink(order_name)
        if coffee_maker.is_resource_sufficient(drink) and money_machine.make_payment(drink.cost):
            coffee_maker.make_coffee(drink)

