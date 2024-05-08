#TODO: Create a letter using starting_letter.txt
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".

#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
#Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
#Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp


with open("./Input/Letters/starting_letter.txt", "r") as start_letter_file:
    source_letter = start_letter_file.readlines()
    print(source_letter)

with open("./Input/Names/invited_names.txt", "r") as name_file:
    names_list = name_file.readlines()
    print(names_list)

for name in names_list:
    absolute_name = name.strip()
    dear_name = source_letter[0].replace("[name]", absolute_name)

    with open(f"./Output/ReadyToSend/letter_for_{absolute_name}.txt", "w") as letter:
        letter.write(dear_name)
        letter.writelines(source_letter[1:])
