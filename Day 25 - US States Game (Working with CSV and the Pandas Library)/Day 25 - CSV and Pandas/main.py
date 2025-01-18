# with open("./weather_data.csv") as file:
#     weather = file.readlines()
# print(weather)

# import csv
#
# with open("weather_data.csv") as file:
#     weather_data = csv.reader(file)
#     temperatures = []
#     for row in weather_data:
#         if row[1] != "temp":
#             temperatures.append(int(row[1]))
#     print(temperatures)

import pandas

data = pandas.read_csv("weather_data.csv")
# print(data)
# print(data["temp"])

# Get data in Columns
# print(data["condition"])
# print(data.condition)


# Get data in Rows

# print(data[data.day == "Monday"])
# print(data[data.temp == data["temp"].max()])

monday = data[data.day == "Monday"]
print(monday.temp[0])

# monday_temp = (monday.temp[0] * 9/5) + 32
# print(monday_temp)

# data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data_20241023.csv")

# Colors: Gray Cinnamon Black
#
# number_of_grey_squirrels = len(data[data["Primary Fur Color"] == "Gray"])
#
# number_of_red_squirrels = len(data[data["Primary Fur Color"] == "Cinnamon"])
#
# number_of_black_squirrels = len(data[data["Primary Fur Color"] == "Black"])
#
# dict_colors = {
#     "Fur Color": ["grey", "red", "black"],
#     "Count": [len(data[data["Primary Fur Color"] == "Gray"]), len(data[data["Primary Fur Color"] == "Cinnamon"]),
#               len(data[data["Primary Fur Color"] == "Black"])],
# }
#
# colors = pandas.DataFrame(dict_colors)
# colors.to_csv("squirrels_count.csv")












