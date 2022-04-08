class Pet:
    def __init__(self, name, age):
        self.name = name
        self.age = age 
    
    def show(self):
        print(f"I am {self.name}, and I am {self.age} years old.")

    def speak(self):
        print("I dont know what to say.")

#With the (pet) brackets the class inherits the properties from the Pet Class 
#duplicate methods - The lower level class will take priority i.e. speak
class Cat(Pet):
    def __init__(self, name, age, color):
        super().__init__(name, age)
        #super = reference the super class - the upper class in the Pet class
        #take the defined properties from the Pet Class
        self.color = color
    
    def show(self):
        print(f"I am {self.name}, I am {self.age} years old and I am {self.color}.")

    def speak(self):
        print("Meow")

class Dog(Pet):
    def speak(self):
        print("Bark")

class Fish(Pet):
    pass

p = Pet("Tim", 19)
p.show()
p.speak()

c = Cat("Bill", 34, "Brown")
c.show()
c.speak()

d = Dog("Jill", 25)
d.show()
d.speak()

f = Fish("Toby", 2)
f.show()
f.speak()