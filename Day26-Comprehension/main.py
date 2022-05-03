import random
import pandas

#List and dictionary comprehension, unqiue to Python and cuts down on the amount of code required 

#Aims to create a word to NATO letter conversion tool 

# ====== List Comprehension: new_list = [new_item for item in list] =====

# >>> list_charis = [char for char in name]
# >>> print(list_charis)
# name = "Chris"

# >>> new_range = [num*2 for num in range(1, 5)]
# >>> print(new_range)
# [2, 4, 6, 8]


# ===== Conditional list comprehension: new_list = [new_item for item in list if test]======

# >>> names = ["Alex", "Christopher", "Beth", "Dave", "Caroline", "Eleanor", "Freddie"]
# >>> short_names = [name for name in names if len(name) < 5]
# >>> print(short_names)
# ['Alex', 'Beth', 'Dave']

# >>> caps_name = [name.upper() for name in names if len(name) >= 5]
# >>> print(caps_name)
# ['CHRISTOPHER', 'CAROLINE', 'ELEANOR', 'FREDDIE']

# Coding Excercise One: Squaring Numbers 
numbers = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]

squared_numbers = [num*num for num in numbers]
print(squared_numbers)

#Coding Excercise Two: Even number filter
numbers = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]

result = [num for num in numbers if num%2 == 0]
print(result)

# =========== Dictionary Comprehension ===========
#new_dict = {new_key:new_value for item in list}
#new_dict2 = {new_key:new_value for (key, value) in dict.items()}
#new_dict3 = {new_key:new_value for (key, value) in dict.items() if test}

names = ['Chris', 'Alex', 'Stephen', 'Caroline', 'Dave']
student_score = {student:random.randint(1, 100) for student in names}
print(student_score)

passed_students = {student:score for (student, score) in student_score.items() if score >= 60} #unsure as to why the .items() is required after the dictinary is provided 
print(passed_students)

#Excercise 1 : Character count in a sentence. 
sentence = "What is the Airspeed Velocity of an Unladen Swallow?"

result = {word:len(word) for word in sentence.strip("?").split()}
print(result)

#Excercise 2 : Weathr conversion C to F 
weather_c = {
    "Monday": 12,
    "Tuesday": 14,
    "Wednesday": 15,
    "Thursday": 14,
    "Friday": 21,
    "Saturday": 22,
    "Sunday": 24,
}
weather_f = {day:(temp * 9/5 + 32) for (day, temp) in weather_c.items()}
print(weather_f)

#Pandas 
stu_dict = { 
    "Name" : ["Chris", "Will", "Ollie"], 
    "Score" : [82, 80, 51] 
    }

stu_dataframe = pandas.DataFrame(stu_dict)
for (index, row) in stu_dataframe.iterrows():
    print(row)
    print(row.Score)
    if row.Name == "Chris":
        print(f"\n***Chris' Score Is: {row.Score}***\n")
