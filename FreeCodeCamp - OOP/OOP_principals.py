# Section 6 - OOP Principles
# Both the Item and Phone class have been stored in seperate files
# ===========
# 4 Key Principles for designing large programmes
# ==========
# Encapsulation - Restricting the direct access to some of our attributes within our programme
# Example = item.apply_increment & property price
# ==========
# Abstraction - Only shows the necessary attributes and hides unnecessary information - hiding unnecessary details from users
# Double underscores to hide functions that should only be accessed from within the class
# ==========
# Inheritance - Mechanism that allows us to re-use code across our classes i.e. Phone class
# ==========
# Polymorphism - Use of a single type entity to represent different types in different scenarios
# Refers to many forms - different scenarios when we call the exact safe entity


#================================== Encapsulation ==================================
from item import Item
from phone import Phone

item1 = Item("PropertyTest", 750, 7)
# Exception i.e. price >= 0 only applies on first creation

#item1.price = -900
item1.apply_increment(0.2)

print(item1.price)

#================================== Abstraction ==================================
item2 = Item("AbsItem", 750, 6)

item2.send_email()
#item1.connect() # Should be private methods that the users dont access - as they dont need too achieved via adding the double underscore
#Double underscore means the functions can only be called from WITHIN the class


#================================== Inheritence ==================================
item3 = Phone('CSHPhone', 1000, 1)
item3.apply_increment(0.2)
print(item3.price)
# Re-using code across all classes, these functions are taken from the Item class

#================================== Polymorphism ==================================
print("\nPolymorphism")

class Keyboard(Item): #brackets clarify what class you inherit from (in this case Item is a parent class and Phone is a child class)
    pay_rate = 0.7 #turn this off and on to see how this affects the parent through inheritance
    def __init__(self, name: str, price: float, quantity: int):
        #call to super function to have full access to all attributes / methods from parent class (Item)
        super().__init__(
            name, price, quantity
        )

print(len(item3.name))
some_list = ['some', 'name']
print(len(some_list))
print(len(some_list[0]))
# len is an example of polymorphism - one instance counts the length of a string, then a list etc.
item4 = Keyboard('OSCKeyboard', 50, 1)

item4.apply_discount() #example of polymorphism
print(item4.price)
