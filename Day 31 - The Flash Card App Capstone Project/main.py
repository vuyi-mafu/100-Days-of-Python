from tkinter import *
import pandas
import random

BACKGROUND_COLOR = "#B1DDC6"
words_to_learn_dict = {}
random_french_word = None
english_word = None


# ----------------------------------READING DATA FILE-------------------------------------------------
try:
    #   Checks if the CSV file words_to_learn.csv is there
    data = pandas.read_csv("data/words_to_learn.csv")
except FileNotFoundError:
    #   Reads data from french_words.csv file and converts it to a dictionary if words_to_learn.csv isn't found
    #   The French words will be the 'key' with a corresponding 'value' of English
    data = pandas.read_csv("data/french_words.csv")
    data_dict = {row.French: row.English for (index, row) in data.iterrows()}
    # print(data_dict)
else:
    #   If words_to_learn.csv is there, convert its contents to a dictionary
    #   The French words will be the 'key' with a corresponding 'value' of English
    data_dict = {row.French: row.English for (index, row) in data.iterrows()}


#   ------------------------------RANDOM FRENCH WORD-------------------------------------------------


def random_word():
    """Function that generates a random word French word and displays it on the front card"""
    #   Declaring global variables to use within this and other functions
    global flash_card_front, timer, random_french_word, english_word
    #   Cancels the timer and resets it
    window.after_cancel(timer)
    #   Gets a random 'key' from data_dict which is a random French word
    random_french_word = random.choice(list(data_dict.keys()))
    #   Gets the corresponding 'value' of the French word which is the English word
    english_word = data_dict[random_french_word]
    #   Edits the canvas text to display the French word. Flips the card to display the English word after 3seconds
    #   using the Flip function
    canvas.itemconfig(canvas_image, image=flash_card_front)
    canvas.itemconfig(word, text=random_french_word, fill="black")
    canvas.itemconfig(title, text="French", fill="black")
    timer = window.after(3000, flip_card, english_word)


#   ------------------------------WHEN USER KNOWS THE WORD----------------------------------------

def knows_word():
    """This function is called when the user clicks on the check_button. It is called when a user
    knows the word displayed"""
    #   Deletes the 'key' and 'value' from the data_dict. This is the French and English word that the user knows
    del data_dict[random_french_word]
    #   Creates a new DataFrame 'words_to_learn' from the edited data_dict and converts it to a CSV file
    words_to_learn = pandas.DataFrame(list(data_dict.items()), columns=["French", "English"])
    words_to_learn.to_csv("data/words_to_learn.csv")
    #   Calls random_word() function to get a new card
    random_word()


#   ------------------------------FLIP CARD-------------------------------------------------
def flip_card(eng_word):
    """Function to flip the card to the english translation"""
    #   Changes the canvas image to the flash_card_back image
    canvas.itemconfig(canvas_image, image=flash_card_back)
    #   Gets the input english_word as eng_word
    canvas.itemconfig(word, text=eng_word, fill="white")
    canvas.itemconfig(title, text="English", fill="white")


#   ------------------------------USER INTERFACE-------------------------------------------------

window = Tk()
window.title("Flash Card Project")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)
timer = window.after(3000, flip_card)

#   Declaring flash card canvas and its properties
canvas = Canvas(width=800, height=526)

flash_card_front = PhotoImage(file="images/card_front.png")
flash_card_back = PhotoImage(file="images/card_back.png")

canvas_image = canvas.create_image(400, 263, image=flash_card_front)
canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0)

title = canvas.create_text(400, 150, text="", font=("Arial", 40, "italic"))
word = canvas.create_text(400, 263, text="", font=("Arial", 60, "bold"))

canvas.grid(columnspan=2)

#   Buttons
check_image = PhotoImage(file="images/right.png")
check_button = Button(image=check_image, bg=BACKGROUND_COLOR, highlightthickness=0, command=knows_word)
check_button.grid(row=1, column=1)

cross_image = PhotoImage(file="images/wrong.png")
cross_button = Button(image=cross_image, bg=BACKGROUND_COLOR, highlightthickness=0, command=random_word)
cross_button.grid(row=1, column=0)
#   Generate a random card when the program is initially started
random_word()

window.mainloop()
