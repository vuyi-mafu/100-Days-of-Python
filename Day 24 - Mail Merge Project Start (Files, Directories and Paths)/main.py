formatted_invited_names = []
names_for_letter = []
details_dict = {}

#  Reads the names of invited guests from 'invited_names.txt' and put them in a list ('Aang'\n)
with open("Input/Names/invited_names.txt") as data:
    invited_names = data.readlines()

#  Edit invited names to a basic string format - removes the \n from the string and appends to list
for name in invited_names:
    name = name.strip()
    formatted_invited_names.append(name)

#  Reads all the lines from 'starting_letter.txt' and puts them in a list contents
with open("Input/Letters/starting_letter.txt") as data:
    contents = data.readlines()

#  Loops through the 'formatted_invited_names' list. Appends every item onto the first line from
#  'contents' list (Dear [name]). Appends everything into a list
for formatted_name in formatted_invited_names:
    first_line_to_replace = contents[0]
    name_to_replace = first_line_to_replace.replace("[name]", formatted_name)
    names_for_letter.append(name_to_replace)

index = 0
for name in names_for_letter:
    contents.pop(0)
    contents.insert(0, name)
    details_dict[formatted_invited_names[index]] = contents
    with open(f"Output/ReadyToSend/letter_for_{formatted_invited_names[index]}.txt", mode="w") as data:
        data.writelines(details_dict[formatted_invited_names[index]])
    index += 1
