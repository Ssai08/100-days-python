# # # with open("weather_data.csv") as file:
# # #     raw_data = file.readlines()
# # #     data = [i.strip() for i in raw_data]
# # # print(data)
# #
# # # import csv
# # # with open("weather_data.csv") as file:
# # #     csv_data = csv.reader(file)
# # #     temperature = []
# # #     for data in csv_data:
# # #         print(data)
# # #         if data[1] != 'temp':
# # #             temperature.append(int(data[1]))
# # #
# # # print(temperature)
# #
# # import pandas
# #
# # # data = pandas.read_csv("weather_data.csv")
# # # print(type(data))
# # # print(data["temp"])
# #
# # # data_dict = data.to_dict()
# # # print(data_dict)
# #
# # # #
# # # data_list = data["temp"].to_list()
# # # print(data_list)
# # #
# # # #
# # # print(data["temp"].mean())
# # # print(data["temp"].max())
# #
# #
# # #get data of a row
# # # print(data[data.day == "Monday"])
# # # print(data[data.temp == data.temp.max()])
# #
# # # Print condition of the day having maximum temperature
# # # print(data.condition[data.temp == data.temp.max()])
# # #
# # # #Print the temperature of monday in Fahrenheit
# # # monday = data[data.day == "Monday"]
# # # temp = monday.temp
# # # temp_f = (temp *(9/5))+32
# # # print(temp_f)
# # # # OR
# # # print((data.temp[data.day == "Monday"])*(9/5)+32)
# #
# # #Create dataframe from scratch
# #
# # data_dict = {
# #     "students" : ["sai","ram","hari"],
# # "age" : [52,45,74]
# # }
# #
# # data = pandas.DataFrame(data_dict)
# # print(data)
# # data.to_csv("new_data.csv")
#
#
# import pandas as pd
#
# squirrel = pd.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data_20250822.csv")
#
# # print(squirrel.columns)
# # print(squirrel["Primary Fur Color"])
# squirrel_type = list(squirrel["Primary Fur Color"].dropna().unique())
# count = list(squirrel["Primary Fur Color"].value_counts(dropna = True))
# counts = squirrel["Primary Fur Color"].value_counts(dropna = True)
#
# # # Way 1:
# # new_df = pd.DataFrame(counts)
# #
# # print(new_df)
# # new_df.to_csv("new_df")
#
# # Way 2:
#
# data_dict = {
#     "type": squirrel_type,
#     "count": count
# }
# new_df = pd.DataFrame(data_dict)
#
# print(new_df)
# new_df.to_csv("new_df")
#
#
#



# import random
#
# names = ["Alice", "Brian", "Catherine", "David", "Emily", "Frank"]
#
# student_scores = {student:random.randint(1,100) for student in names}
# passed_students = {name:value for (name,value) in student_scores.items() if value > 60}
#
# print(student_scores)
# print(passed_students)

# Looping through a pandas data frame

import pandas as pd

student = {
    "Name": ["Alice", "Brian", "Catherine", "David", "Emily", "Frank"],
    "Score": [85, 92, 78, 90, 88, 76]
}

df = pd.DataFrame(student)
print(df)

for (idx,row) in df.iterrows():
    print(idx)
    print(row)