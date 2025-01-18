import turtle
import pandas

#   Initialize Screen and add image
screen = turtle.Screen()
screen.title("U.S States Game")
image = "blank_states_img.gif"

screen.addshape(image)
turtle.shape(image)
turtle.penup()

#   Turns off the screen animation
screen.tracer(0)

game_on = True
states_dict_list = {}
states_list = []
index = 0
score = 0

#   Read CSV and store in variable
states_data = pandas.read_csv("50_states.csv")
# states_data.to_list()

#   Gets all state names from state column and stores them in a list
for state in states_data.state:
    states_list.append(state)

#   Gets the state name and corresponding x, y coordinates and stores them in a dictionary
#   'state' is the key, 'x, y' coordinates as tuple value
for state in states_data.state:
    row = states_data[states_data.state == state]
    states_dict_list[state] = row.x[index], row.y[index]
    index += 1

while game_on:

    user_input = screen.textinput(f"{score}/50 states correct", "What's another state name?").title()

#   Checks the user input in the states list. Writes the state on the image and adds a point
#   if it exists.
    if user_input in states_list:
        turtle.goto(states_dict_list[user_input])
        turtle.write(user_input, align='center', move=False)
        states_list.remove(user_input)
        score += 1

    if score == 50:
        game_on = False

    if user_input == "Exit":
        break

#   states_list will now contain the missed states
#   This list will now be converted to a DataFrame
missed_states = pandas.DataFrame(states_list, columns=["state"])
missed_states.to_csv("missed_states.csv")
