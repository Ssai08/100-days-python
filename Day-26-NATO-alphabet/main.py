# student_dict = {
#     "student": ["Angela", "James", "Lily"],
#     "score": [56, 76, 98]
# }
#
# #Looping through dictionaries:
# for (key, value) in student_dict.items():
#     #Access key and value
#     pass
#
import pandas
import os

def clear_screen():
    # 'nt' means Windows, otherwise it's Linux/macOS
    os.system('cls' if os.name == 'nt' else 'clear')
    # print("Screen Cleared\n")

clear_screen()
# student_data_frame = pandas.DataFrame(student_dict)
#
# #Loop through rows of a data frame
# for (index, row) in student_data_frame.iterrows():
#     #Access index and row
#     #Access row.student or row.score
#     pass
#
# # Keyword Method with iterrows()
# # {new_key:new_value for (index, row) in df.iterrows()}

# #TODO 1. Create a dictionary in this format:
# # {"A": "Alfa", "B": "Bravo"}
# csv_data = pandas.read_csv("nato_phonetic_alphabet.csv")
# # print(csv_data)
# data_dict = {row.letter:row.code for (index,row) in csv_data.iterrows()}
# letter_list = [_.strip() for _ in data_dict.keys()]
# # print(letter_list)

# def validate_input():
#     user_input = input("Enter a word: ").upper()
#     value_list = [_ for _ in user_input if _ not in letter_list]
#     # print(value_list)
#     if len(value_list):
#         validate_input()
#     else:
#         #TODO 2. Create a list of the phonetic code words from a word that the user inputs.
#         spelling_helper_list = [data_dict[letter] for letter in user_input]
#         print(spelling_helper_list)
    

# def __main__():
#     validate_input()

# if __name__ == "__main__":
#     __main__()



###################################################################
#********************METHOD - 2***********************#
###################################################################


#TODO 1. Create a dictionary in this format:
# {"A": "Alfa", "B": "Bravo"}
csv_data = pandas.read_csv("nato_phonetic_alphabet.csv")
# print(csv_data)
data_dict = {row.letter:row.code for (index,row) in csv_data.iterrows()}
letter_list = [_.strip() for _ in data_dict.keys()]
# print(letter_list)

while True:
    try:
        user_input = input("Enter a word: ").upper()
        #TODO 2. Create a list of the phonetic code words from a word that the user inputs.
        spelling_helper_list = [data_dict[letter] for letter in user_input]
    except KeyError as e:
        print(f"{e} is not a valid letter. Please provide correct input.")
    else:
        print(spelling_helper_list)
        break
    

def __main__():
    pass
if __name__ == "__main__":
    __main__()
