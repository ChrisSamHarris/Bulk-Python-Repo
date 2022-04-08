import csv

class Item:
    pay_rate = 0.8
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
        return f"{self.__class__.__name__}('{self.name}', {self.price}. {self.quantity})" #CSV - Comma Seperated values - allows data to be created in table structured format.

class Phone(Item): #brackets clarify what class you inherit from (in this case Item is a parent class and Phone is a child class)
    def __init__(self, name: str, price: float, quantity: int, broken_phones=0):
        #call to super function to have full access to all attributes / methods from parent class (Item)
        super().__init__(
            name, price, quantity
        )
        assert broken_phones >= 0, f"Broken Phones {broken_phones}, must be greater than or equal to 0!"
        self.broken_phones = broken_phones
        #Phone.all.append(self) - not requuired thanks to the super-function


phone1 = Phone("jscPhonev10", 500, 5, 1)
print(phone1.calculate_total_price())
phone2 = Phone("jscPhonev20", 700, 5, 1)

print(Item.all)
print(Phone.all)