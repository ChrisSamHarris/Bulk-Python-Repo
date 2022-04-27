# ======= python built-in methods arent powerful enough for data analysis ======

# with open("weather_data.csv") as weatherData:
#     data = weatherData.readlines()
#     print(data)


# ======= CSV library can be used for analysis but its arduous ======

# import csv #In-built csv reading and writing library

# with open("weather_data.csv") as weatherData:
#     data = csv.reader(weatherData)
#     temperatures = []
#     for row in data:
#         # print(row)
#         if row[1] != 'temp': #ignores the column label temp
#             temperatures.append(int(row[1]))
#     print(temperatures)

### ===== Pandas ====

from dataclasses import dataclass
import pandas

data = pandas.read_csv("weather_data.csv")
#print(data)
# print(type(data))
# print(data["temp"])


# Table = Data Frame | Column = Series 

data_dict = data.to_dict()
print(data_dict)

temp_list = data["temp"].to_list()

print(round(sum(temp_list) / len(temp_list), 2)) #Average temperature to 2 decimal places 

avg_temp = (data["temp"].mean()) 
print(avg_temp.round(2))

print(data["temp"].max())

#print(data.condition) vs print(data["condition"])
print(data[data.day == "Monday"])

### Retrieve the column with the max temp:
max_temp = data["temp"].max()
print(data[data.temp == max_temp])
# Reduced code: 
print(data[data.temp == data.temp.max()])

#convert mondays temperature to Fahrenheit 
monday = (data[data.day == "Monday"])
print((monday.temp * (9/5)) + 32)

#Create a data frame from Scratch 
data_dict = {
    "students": ["Chris", "Amy", "James"],
    "scores": [76, 56, 65]
}

student_data = pandas.DataFrame(data_dict)
student_data.to_csv("student_data.csv")
print(student_data)