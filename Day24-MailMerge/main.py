#TODO: Create a letter using starting_letter.txt 
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".
    
#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp

PLACEHOLDER = "[name]"

with open("./Input/Names/invited_names.txt") as names_file: #Default mode == Read
    names = names_file.readlines() # Returns a list containing each line in the file as a list item
    print(names)

with open("./Input/Letters/starting_letter.txt") as letter_file:
    letter_contents = letter_file.read()
    for name in names:
        stripped_name = name.strip() #removes the white space and unnecessary new lines/space and \n between the name and the letter content
        new_letter = letter_contents.replace(PLACEHOLDER, stripped_name)
        #print(new_letter)
        #Now need to generate a new letter with the respective name for who it is addressed - required fstring and write mode to generate the letters
        with open(f"./Output/ReadyToSend/letter_for_{stripped_name}.txt", mode="w") as completed_letter:
            completed_letter.write(new_letter)

string_with_n = "Test String \n        "
ammended_string = string_with_n.strip()
print(ammended_string)

# stringToEdit = "I like bananas, oranges and pineapples"
# editedString = stringToEdit.replace("pineapples", "pears")
# print(editedString)