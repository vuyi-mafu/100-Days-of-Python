#   FileNotFound
# with open("a_data") as file:
#     file.read()

#   KeyError
# a_dictionary = {"key": "value"}
# value = a_dictionary["non-existent-key"]

#   IndexError
# fruit_list = ["Apple", "Banana", "Pear"]
# fruit = fruit_list[4]

#   TypeError
# text = "abc"
# print(text + 5)

# try: ------- Something that might cause an exception
#
# except: ---- Do this if there was an exception
#
# else: ------ Do this if there were NO exceptions
#
# finally: --- Do this no matter what happens
#   raise TypeError("This is an error that I made up")

# raise allows you to raise an error and crashes the code

# height = float(input("Height: "))
# weight = int(input("Weight: "))

# if height > 3:
#     raise ValueError("The human height should not be over 3 metres")
#
# bmi = weight / height ** 2
# print(bmi)

