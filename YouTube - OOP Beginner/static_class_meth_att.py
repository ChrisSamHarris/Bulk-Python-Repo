class Person:
    number_of_people = 0

    def __init__(self, name):
        self.name = name
        #Person.number_of_people +=1
        Person.add_person()

    #Class methods, dont reference seld, they reference class
    @classmethod
    def num_of_people_(cls):
        return cls.number_of_people

    @classmethod
    def add_person(cls):
        cls.number_of_people += 1

#Referencing class / Person
p1 = Person("Tim")
print(Person.number_of_people)
p2 = Person("Jill")
print(Person.number_of_people)


# Person.number_of_people = 8
# #As p2 doesnt have a number_of_people attribute, it retrieves the value of the class
# print(p2.number_of_people)

#Referencing Class method - Dont need access to an instance to call it 
print(Person.num_of_people_())

#===== Static Methods ======

class Math:

    @staticmethod
    #dont change anything - acts as a function defined within a class
    def add5(x):
        return x + 5

    @staticmethod
    def pr():
        print("Printing....")

print(Math.add5(995))
Math.pr()
