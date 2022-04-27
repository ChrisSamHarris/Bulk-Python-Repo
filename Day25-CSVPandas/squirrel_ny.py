import pandas as pd

# || Table = Data Frame | Column = Series ||

data = pd.read_csv("2018_cp_sd.csv")

#3 squirrel colours - get a count for the number of squirrels and create a new data frame  | Gray, Black or Cinnamon
red_squirrels = data[data["Primary Fur Color"] == "Cinnamon"]
red_squirrel_count = len(red_squirrels)
print(f"The total number of black squirrels is: {red_squirrel_count}")

# print(red_squirrels.count())
grey_squirrels = data[data["Primary Fur Color"] == "Gray"]
grey_squirrel_count = len(grey_squirrels)
print(f"The total number of black squirrels is: {grey_squirrel_count}")

black_squirrels = data[data["Primary Fur Color"] == "Black"]
black_squirrel_count = len(black_squirrels)
print(f"The total number of black squirrels is: {black_squirrel_count}")

data_dict = {
    "Fur Colour": ["Gray", "Cinnamon", "Black"],
    "Count" : [grey_squirrel_count, red_squirrel_count, black_squirrel_count]
}

print(data_dict)

DataFrame = pd.DataFrame(data_dict)
DataFrame.to_csv("sq_numbers.csv")

