import pandas

#   new_list = [new_item for item in list]
#   new_list = [new_item for item in list if test]

#   new_dict = {new_key:new_value for item in list}

#   new_dict = {new_key:new_value for (key,value) in dict.items()}

#   new_dict = {new_key:new_value for (key,value) in dict.items() if test}

student_dict = {
    "student": ["Angela", "James", "Lily"],
    "score": [56, 76, 98]
}

#   Looping through dictionaries:
# for (key, value) in student_dict.items():
#     print(value)

student_data_frame = pandas.DataFrame(student_dict)
# print(student_data_frame)

#   Loop through a data frame
# for (key, value) in student_data_frame.items():
#     print(value)

#   Loop through rows of a data frame
for (index, row) in student_data_frame.iterrows():
    print(row.student)


