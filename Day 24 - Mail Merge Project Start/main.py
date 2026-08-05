#TODO: Create a letter using starting_letter.txt 
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".

#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
#Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
#Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp

with open("D:/100 Days of Python/Day 24 - Mail Merge Project Start/Input/Letters/starting_letter.txt",mode="r") as main_file:
    content = main_file.read()
    # print(content)

with open("Input/Names/invited_names.txt") as main_file:
    name_list = main_file.readlines()
    new_name_list = list()
    for name in name_list:
        name = name.replace("\n","")
        new_name_list.append(name)
        with open (f"Output/ReadyToSend/letter_for_{name}.txt",mode="w") as file:
            file.write(content.replace("[name]",name.strip()))


