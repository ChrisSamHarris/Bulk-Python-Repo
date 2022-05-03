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

