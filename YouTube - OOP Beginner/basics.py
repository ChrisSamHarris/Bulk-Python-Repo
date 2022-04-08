#https://www.youtube.com/watch?v=JeznW_7DlB0&ab_channel=TechWithTim

def hello():
    print("hello")

#OBJECTS
print("\n==========OBJECTS=========")
#Whenever you create something in python, you are creating an object that is an instance of a specific class
x = 1
print(type(x))
print(type("Hello"))
print(type(hello))

#METHODS
print("\n=========METHODS=========")
string = 'hello'
# dot operator = method acting on a specific object
print(string.lower())

#Class
print("\n=========CLASS=========")
class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        #method will be called whenever a new instance is created

    def add_one(self, x):
        return x + 1

    def bark(self):
    #bark = method = Method is a function that goes inside a class
        print("bark")

    def get_name(self):
        return self.name

    def get_age(self):
        return self.age
    
    def set_age(self, age):
        self.age = age

d = Dog("Timmy", 3)
print(d.name)
d.set_age(12)
print(d.get_name())
print(d.get_age())
print("\n")

d2 = Dog("Bill", 8)
print(d2.name)
print(d2.get_name())
print(d2.get_age())
print("-")

d.bark()
print(d.add_one(99))
print("\n")

print(type(d))

print("\n=========MULTIPLE CLASSES=========")
class Student:
    def __init__(self, name, age, grade):
        self.name = name
        self.age = age
        self.grade = grade #0-100
    
    def get_grade(self):
        return self.grade
    
class Course:
    def __init__(self, name, max_students):
        self.name = name
        self.max_students = max_students
        self.students = []
        self.is_active = False

    def add_student(self, student):
        if len(self.students) < self.max_students:
            self.students.append(student)
            return True
        return False

    def get_average_grade(self):
        value = 0
        for student in self.students:
            value += student.get_grade()
        return value / len(self.students)

s1 = Student("Tim", 19, 95)
s2 = Student("Bill", 18, 75)
s3 = Student("Jill", 20, 58)

course = Course("Science", 2)
course.add_student(s1)
course.add_student(s2)

print(course.students[0].name)
print(course.add_student(s3)) #Will return false as this exceeds the max students of 2
print(course.get_average_grade())
#print(course.students()) #This doesnt work without, unsure as to why?


