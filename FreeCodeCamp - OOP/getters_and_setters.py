# Section 5 - Getters & Setters
# Both the Item and Phone class have been stored in seperate files

from item import Item
from phone import Phone

# Item.instantiate_from_csv()
# print(Item.all)

item1 = Item("PropertyTest", 750, 7)
#item1.name = "MyNewName" - The property class will restrict the code from running correctly unless a setter is determined
item1.name = "OtherItem"
print(item1.name)

# We can create read-only attributes to ensure only one opportunity to set the name of our item - ENCAPSULATION
# Create those by using a property value decarator within our functions - below snippet originally typed in item.py
# @property
#     def read_only_name(self):
#         return "AAA"



