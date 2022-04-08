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
        self.__name = name
        self.__price = price
        self.quantity = quantity

        #append item to our stock/ "all" list
        Item.all.append(self)

    @property
    def price(self):
        return self.__price

    def apply_discount(self):
        self.__price = self.__price * self.pay_rate #pay_rate needs to be accessed at class or instance level - If we use self.pay_rate it's declared at a instance level / if we use Item.pay_rate it uses the value declared at Class level

    def apply_increment(self, increment_value):
        self.__price = self.__price + (increment_value * self.__price)

    @property # Give control of what you would like to do when you get a property
    # Property Decorator = Read-Only Attribute - Property is almost a rule for the class - in order to stop a clash we need to use an underscore in both the property and __init
    def name(self):
        return self.__name

    @name.setter # Setter give control to set an attribute
    def name(self, value):
        if len(value) > 10:
            raise Exception(f"The name '{value}'is too long.")
        else:
            self.__name = value

    def calculate_total_price(self):
        return self.__price * self.quantity
        #We have access to all the declared self attributes


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
        return f"{self.__class__.__name__}('{self.name}', {self.__price}. {self.quantity})" #CSV - Comma Seperated values - allows data to be created in table structured format.

    def __connect(self, smpt_server):
        pass

    def __prepare_em_bod(self):
        return f"""Hello Someone. 
        We have {self.name}, {self.quantity} times. 
        Regards, Chris Harris"""

    def __send(self):
        pass

    def send_email(self):
        self.__connect(smpt_server="random")
        self.__prepare_em_bod()
        self.__send()
        return

