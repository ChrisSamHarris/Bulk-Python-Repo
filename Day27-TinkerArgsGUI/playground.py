#Args - any number, value of arguements - good for data analysis - Tuple type - number of arguements in a function can vary
#positional arguements - collect arguements into a tuple - REMEMBER: Args is a tuple so it will print the parenthesis 
print("\n####### *ARGS ######")
def add(*args):
    print(args[-1])
    value = 0
    for arg in args:
        value += arg
    print(type(args))
    return value

print(add(12, 60, 100, 33, 29))

#kwargs - Keyword arguements, starts with double asterisk ** - 
print("\n####### **KWARGS ######")
def calculate(n, **kwargs):
    print(type(kwargs))
    print(kwargs)
    # for key, value in kwargs.items():
    #     print(key)
    #     print(value)
    n += kwargs["add"]
    n *= kwargs["multiply"]
    print(n)

calculate(2, add=3, multiply=5)

class Car:
    def __init__(self, **kw):
        self.make = kw["make"] 
        self.model = kw.get("model") #.get() will stop the script from erroring out whem we dont provide a specific value - it will infact return 'None' - See my_second_car.model
        self.colour = kw.get("colour")
        self.seats = kw.get("seats")

my_car = Car(make="Porsche", model="911 Targa4 GTS")
print(my_car.model)
my_second_car = Car(make="Volkswagen")
print(my_second_car.model)