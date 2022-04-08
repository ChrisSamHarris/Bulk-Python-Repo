from item import Item

class Phone(Item): #brackets clarify what class you inherit from (in this case Item is a parent class and Phone is a child class)
    def __init__(self, name: str, price: float, quantity: int, broken_phones=0):
        #call to super function to have full access to all attributes / methods from parent class (Item)
        super().__init__(
            name, price, quantity
        )
        assert broken_phones >= 0, f"Broken Phones {broken_phones}, must be greater than or equal to 0!"
        self.broken_phones = broken_phones
        #Phone.all.append(self) - not required thanks to the super-function
