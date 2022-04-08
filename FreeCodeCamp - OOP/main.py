# item1 = 'Phone'
# item1_price = 100
# item1_quantity = 5
# item1_price_total = item1_price * item1_quantity
import csv
#methods = function inside a Class
class Item:
    pay_rate = 0.8 #Class attribute - The pay rate after 20% discount
    all = []
    def __init__(self, name: str, price: float, quantity: int):
        # magic_methods = __init__
        #Run validations to recieved arguements with the assert statement
        assert price >= 0, f"Price {price}, must be greater than or equal to 0!"
        assert quantity >= 0, f"Price {quantity}, must be greater than or equal to 0!"

        # Can provide a default value i.e. 'quantity=0', which can be overwritten during class initialisation
        # self = assing to self object
        self.name = name
        self.price = price
        self.quantity = quantity

        #append item to our stock/ "all" list
        Item.all.append(self)

    def calculate_total_price(self):
        return self.price * self.quantity
        #We have access to all the declared self attributes

    def apply_discount(self):
        self.price = self.price * self.pay_rate #pay_rate needs to be accessed at class or instance level - If we use self.pay_rate it's declared at a instance level / if we use Item.pay_rate it uses the value declared at Class level

    @classmethod
    def instantiate_from_csv(cls):
        #Class method - accessed from the Class level only
        #automatically receives the cls (class) parameter within the brackets()
        with open(r"C:\Users\chris\OneDrive\Documents\Python_code\OOP-FCC\items.csv", "r") as f: #had to put r before the path and then follow with the full string
            reader = csv.DictReader(f) #read our content in the csv file as a list of dictionaries
            items = list(reader)
        #this function relates to Item.instantiate_from_csv() - Class method
        for item in items:
            Item(
                name=item.get('name'),
                price=float(item.get('price')),
                quantity=int(item.get('quantity')),
            )
    @staticmethod
    def is_integer(num):
        #object is never sent as the first argument - see 'num' is not highlighted in purple
        #We will count out the floats that are point .0
        if isinstance(num, float):
            # count out the floats that are point zero
            return num.is_integer()
        elif isinstance(num, int):
            return True
        else:
            False

    def __repr__(self):
        return f"Item('{self.name}', {self.price}. {self.quantity})" #CSV - Comma Seperated values - allows data to be created in table structured format.

#======== Static Methods - Checking our returned values to see if we have any un-used floats i.e. 100.0 ===========
# Should do some work that has a logical connection to a class - i.e. check if a number is an integer or a float
print(Item.is_integer(7))


#======================== Storing and referencing instances - Class Methods  ============
# Item.instantiate_from_csv() # This errors now the classmethod has been developed - assert price >= 0, f"Price {price}, must be greater than or equal to 0! = Problem is that these values from items.csv are passed in through as strings - need to convert via float and int
# print(Item.all)

# item1 = Item("Phone", 100, 1)
# item2 = Item("Laptop", 1000, 3)
# item3 = Item("Cable", 10, 5)
# item4 = Item("Mouse", 50, 5)
# item5 = Item("Keyboard", 75, 5)

# print(Item.all) # Shows the object stored in memory - not user friendly / FIX === use a magic method inside the class (def __repr__)
#
# for item in Item.all:
#     print(item.name)


# dot = attribute of a method i.e. string.upper()
# item1 = Item("Phone", 100, 5)
# item2 = Item("Laptop", 1000, 3)
#
# # Can always add attributes, even outside of init
# item2.has_numpad = False

# print(item1.calculate_total_price())

# ========================== Class Vs Instance Attributes ===========================
#print(item1.pay_rate) # Can still see the class attribute even though we're referencing a specific instance - Python will first look at instance level and then look at class level
# print(Item.__dict__) # Returns all the attributes at Class level
# print(item1.__dict__)# Returns all the attributes at an instance level
# # ==================
# item2.pay_rate = 0.7 # pay_rate will be changed at instance level
# item2.apply_discount()
# print(item2.price) # We're still receiving 800 - still a 20% discount - Need to declare pay_rate as self.pay_rate in the class so the function operates at Instance level


# ===== ======
# item1.apply_discount()
# print(item1.price)
# =======================================================
# item2 = Item()
# item2.name = "Laptop"
# item2.price = 1000
# item2.quantity = 3
# print(item2.calculate_total_price(item2.price, item2.quantity))

# print(item1.quantity)
# print(item2.name)

# print(type(item1))
# print(type(item1.name))
# print(type(item1.price))
# print(type(item1.quantity))