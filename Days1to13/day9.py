# ============================ Challenge 1: Student Grades ============================
student_scores = {
  "Harry": 81,
  "Ron": 78,
  "Hermione": 99, 
  "Draco": 74,
  "Neville": 62,
}
# 🚨 Don't change the code above 👆

#TODO-1: Create an empty dictionary called student_grades.
student_grades = {}

#TODO-2: Write your code below to add the grades to student_grades.👇

for student in student_scores:
    score = student_scores[student]
    if score > 90:
        student_grades[student] = "Outstanding"
    elif score > 80:
        student_grades[student] = "Exceeds Expectations"
    elif score > 70:
        student_grades[student] = "Acceptable"
    else:
        student_grades[student] = "Fail"


# 🚨 Don't change the code below 👇
print(student_grades)

# ============================ Challenge 2: Appending new data to a dictionary  ============================
travel_log = [
{
  "country": "France",
  "visits": 12,
  "cities": ["Paris", "Lille", "Dijon"]
},
{
  "country": "Germany",
  "visits": 5,
  "cities": ["Berlin", "Hamburg", "Stuttgart"]
},
]
#🚨 Do NOT change the code above

#TODO: Write the function that will allow new countries
#to be added to the travel_log. 👇
# country = input("What is the name of the country you visited?")
# visit_num = input(int("How many times have you visisted this country?"))
# cities = []
# cities = cities.append(input("What cities did you visit within this country?"))

def add_new_country(country, visit_num, cities):
    new_log = {
        "country": country,
        "visits": visit_num,
        "cities": cities,
    }
    travel_log.append(new_log)

#🚨 Do not change the code below
add_new_country("Russia", 2, ["Moscow", "Saint Petersburg"])
print(travel_log)

# ============================ Day 9 Lecture Notes:  ============================
programming_dictionary = {
  "Bug": "An error in a program that prevents the program from running as expected.", 
  "Function": "A piece of code that you can easily call over and over again.",
}
#Retrieving items from a dictionary.
print(programming_dictionary["Bug"])

#Adding new items to dictionary.
programming_dictionary["Loop"] = "The action of doing something repeatedly."
#print(programming_dictionary)

#Create an empty Dict
empty_dict = {}

#Wipe an existing Dict
#programming_dictionary = {}

#Edit an item in a dict
programming_dictionary["Bug"] = "A moth in your computer."

#print(programming_dictionary)

for key in programming_dictionary:
  print(key)
  print(programming_dictionary[key])
  print("\n")

new_dict_test = {}
for key in programming_dictionary:
  new_dict_test[key] = "This is a test to assign new values to a dictionary"

print(new_dict_test)

#Nesting
capitals = {
  "France": "Paris",
  "Germany": "Berlin",
}

#Nesting list in dictionary
travel_log = {
  "France": ["Paris", "Lille", "Dijon"],
  "Germany": ["Berlin", "Hamburg", "Stuttgart"],
}

#Nesting a dictionary in a dictionary 
travel_log_visits = {
  "France": {"cities_visisted":["Paris", "Lille", "Dijon"], "total_visits": 12},
  "Germany": {"cities_visited": ["Berlin", "Hamburg", "Stuttgart"], "total_visits": 5},
}

#Nesting a dictionar in a list
travel_log_visits = [
    {"country": "France",
     "cities_visisted":["Paris", "Lille", "Dijon"],
     "total_visits": 12
    },
    {"country": "Germany",
     "cities_visited": ["Berlin", "Hamburg", "Stuttgart"],
     "total_visits": 5
    },
  ]
