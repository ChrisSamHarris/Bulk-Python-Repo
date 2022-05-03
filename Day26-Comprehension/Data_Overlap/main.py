with open("file1.txt") as file1: 
    file_1_data = file1.readlines()

with open("file2.txt") as file2: 
    file_2_data = file2.readlines()

result = [int(item) for item in file_1_data if item in file_2_data]
print(result)
