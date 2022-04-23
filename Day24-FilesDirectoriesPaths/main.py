#EOD objectives - Working with local file systems and utilising local directories, improving the pre-existing SnakeGame
#Project to automate letter-writing, personalising parts of the file i.e. Letters addressed to different names

with open("my_file.txt", mode="a") as file:
    file.write("\nNew text.")

# with open("my_file.txt", mode="a") as file:
#     for i in range (1 ,11):
#         file.write("\nNew text.")

# open modes :
# r = DEFAULT Read
# w = write - overwrite current text - if theres no text file, it WILL be created 
# a = append 


# file = open("my_file.txt", mode="w")
# contents = file.read()
# print(contents)

# file.close() # Takes up PC resource if the file isn't closed i.e. Tabs on a computer


# with open("myfile.txt") as file: 
    # contents = file.read()
    # print(contents)
