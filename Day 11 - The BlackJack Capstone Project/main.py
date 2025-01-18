############### Blackjack Project #####################

# Difficulty Normal 😎: Use all Hints below to complete the project.
# Difficulty Hard 🤔: Use only Hints 1, 2, 3 to complete the project.
# Difficulty Extra Hard 😭: Only use Hints 1 & 2 to complete the project.
# Difficulty Expert 🤯: Only use Hint 1 to complete the project.

############### Our Blackjack House Rules #####################

## The deck is unlimited in size.
## There are no jokers.
## The Jack/Queen/King all count as 10.
## The the Ace can count as 11 or 1.
## Use the following list as the deck of cards:
## cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
## The cards in the list have equal probability of being drawn.
## Cards are not removed from the deck as they are drawn.
## The computer is the dealer.

##################### Hints #####################

# Hint 1: Go to this website and try out the Blackjack game:
#   https://games.washingtonpost.com/games/blackjack/
# Then try out the completed Blackjack project here:
#   http://blackjack-final.appbrewery.repl.run

# Hint 2: Read this breakdown of program requirements:
#   http://listmoz.com/view/6h34DJpvJBFVRlZfJvxF
# Then try to create your own flowchart for the program.

# Hint 3: Download and read this flow chart I've created:
#   https://drive.google.com/uc?export=download&id=1rDkiHCrhaf9eX7u7yjM1qwSuyEk-rPnt

# Hint 4: Create a deal_card() function that uses the List below to *return* a random card.
# 11 is the Ace.

# Hint 5: Deal the user and computer 2 cards each using deal_card() and append().
# user_cards = []
# computer_cards = []

# Hint 6: Create a function called calculate_score() that takes a List of cards as input
# and returns the score.
# Look up the sum() function to help you do this.

# Hint 7: Inside calculate_score() check for a blackjack (a hand with only 2 cards: ace + 10) and return 0 instead of
# the actual score. 0 will represent a blackjack in our game.

# Hint 8: Inside calculate_score() check for an 11 (ace). If the score is already over 21, remove the 11 and replace
# it with a 1. You might need to look up append() and remove().

# Hint 9: Call calculate_score(). If the computer or the user has a blackjack (0) or if the user's score is over 21,
# then the game ends.

# Hint 10: If the game has not ended, ask the user if they want to draw another card. If yes, then use the deal_card(
# ) function to add another card to the user_cards List. If no, then the game has ended.

# Hint 11: The score will need to be rechecked with every new card drawn and the checks in Hint 9 need to be repeated
# until the game ends.

# Hint 12: Once the user is done, it's time to let the computer play. The computer should keep drawing cards as long
# as it has a score less than 17.

# Hint 13: Create a function called compare() and pass in the user_score and computer_score. If the computer and user
# both have the same score, then it's a draw. If the computer has a blackjack (0), then the user loses. If the user
# has a blackjack (0), then the user wins. If the user_score is over 21, then the user loses. If the computer_score
# is over 21, then the computer loses. If none of the above, then the player with the highest score wins.

# Hint 14: Ask the user if they want to restart the game. If they answer yes, clear the console and start a new game
# of blackjack and show the logo from art.py.

import random
from art import logo

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
# cards = [11, 10]
user_cards = []
computer_cards = []
play = True
user_score = 0
computer_score = 0

# clear = lambda: os.system('clear')

question = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ").lower()

if question == "y":
    print(logo)
    play
elif question == "n":
    play = False
else:
    print("The input entered is incorrect")


def deal_user_card():
    user_cards.append(random.choice(cards))


def deal_computer_card():
    computer_cards.append(random.choice(cards))


deal_user_card()
deal_user_card()
deal_computer_card()
deal_computer_card()

while play:
    blackjack = 0


    def calculate_score(user_cards, computer_cards):
        user_total = sum(user_cards)
        computer_total = sum(computer_cards)

        if 11 in user_cards and user_total == 21:
            return blackjack

        if 11 in computer_cards and computer_total == 21:
            return blackjack

        if 11 in user_cards and user_total > 21:
            user_cards.remove(11)
            user_cards.append(1)

        if 11 in computer_cards and computer_total > 21:
            computer_cards.remove(11)
            computer_cards.append(1)

        user_total = sum(user_cards)
        computer_total = sum(computer_cards)

        return user_total


    def compare(user_total, computer_total):
        if user_total == computer_total:
            print("You and the Computer have drawn!")
        elif (11 in user_cards and user_total == 21) and user_total != computer_total:
            print("You have won!")
        elif (11 in computer_cards and computer_total == 21) and computer_total != user_total:
            print("You lose. Computer Wins!")
        elif (11 in computer_cards and computer_total == 21) and (11 in user_cards and user_total == 21):
            print("You and the Computer have drawn!")
        elif user_total > 21:
            print("You lose, Computer Wins!")
        elif computer_total > 21:
            print("You win!")
        else:
            highest = max(user_total, computer_total)
            if highest == user_total:
                print("You Win!")
            else:
                print("You lose, Computer Wins")


    if calculate_score(user_cards, computer_cards) > 21:
        print(
            f"    Your cards: {user_cards}, current score: {calculate_score(user_cards, computer_cards)}")
        print(f"    Computer's first card: {computer_cards[0]}")
        print(f"    Your final hand is: {user_cards}, final score: {calculate_score(user_cards, computer_cards)}")
        print(f"    Computer's final hand is: {computer_cards}, final score: {sum(computer_cards)}")
        compare(user_total=calculate_score(user_cards, computer_cards), computer_total=sum(computer_cards))
        new_game = input("Do you want to play another game of Blackjack? Type 'y' or 'n': ").lower()
        if new_game == "y":
            play = True
            user_cards = []
            computer_cards = []
            deal_user_card()
            deal_user_card()
            deal_computer_card()
            deal_computer_card()
            user_score = 0
            computer_score = 0
        elif new_game == "n":
            play = False

    elif calculate_score(user_cards, computer_cards) == blackjack:
        print(
            f"    Your cards: {user_cards}, current score: {calculate_score(user_cards, computer_cards)}")
        print(f"    Computer's first card: {computer_cards[0]}")
        print(f"    Your final hand is: {user_cards}, final score: BlackJack!")
        print(f"    Computer's final hand is: {computer_cards}, final score: {sum(computer_cards)}")
        print("You Win!")
        new_game = input("Do you want to play another game of Blackjack? Type 'y' or 'n': ").lower()
        if new_game == "y":
            play = True
            user_cards = []
            computer_cards = []
            deal_user_card()
            deal_user_card()
            deal_computer_card()
            deal_computer_card()
            user_score = 0
            computer_score = 0
        elif new_game == "n":
            play = False

    elif 11 in computer_cards and sum(computer_cards) == 21:
        print(
            f"    Your cards: {user_cards}, current score: {calculate_score(user_cards, computer_cards)}")
        print(f"    Computer's first card: {computer_cards[0]}")
        print(f"    Your final hand is: {user_cards}, final score: BlackJack!")
        print(f"    Computer's final hand is: {computer_cards}, final score: BlackJack!")
        print("You lose, Computer Wins!")
        new_game = input("Do you want to play another game of Blackjack? Type 'y' or 'n': ").lower()
        if new_game == "y":
            play = True
            user_cards = []
            computer_cards = []
            deal_user_card()
            deal_user_card()
            deal_computer_card()
            deal_computer_card()
            user_score = 0
            computer_score = 0
        elif new_game == "n":
            play = False

    elif sum(user_cards) == 21:
        print(
            f"    Your cards: {user_cards}, current score: {calculate_score(user_cards, computer_cards)}")
        print(f"    Computer's first card: {computer_cards[0]}")
        print(f"    Your final hand is: {user_cards}, final score: {calculate_score(user_cards, computer_cards)}")
        print(f"    Computer's final hand is: {computer_cards}, final score: {sum(computer_cards)}")
        compare(user_total=calculate_score(user_cards, computer_cards), computer_total=sum(computer_cards))
        new_game = input("Do you want to play another game of Blackjack? Type 'y' or 'n': ").lower()
        if new_game == "y":
            play = True
            user_cards = []
            computer_cards = []
            deal_user_card()
            deal_user_card()
            deal_computer_card()
            deal_computer_card()
            user_score = 0
            computer_score = 0
        elif new_game == "n":
            play = False

    elif calculate_score(user_cards, computer_cards) < 21:
        print(
            f"    Your cards: {user_cards}, current score: {calculate_score(user_cards, computer_cards)}")
        print(f"    Computer's first card: {computer_cards[0]}")
        another = input("Do you want another card? Type 'y' or 'n': ").lower()
        if another == "y":
            deal_user_card()
        elif another == "n":
            while sum(computer_cards) < 17:
                deal_computer_card()
            print(
                f"    Your final hand is: {user_cards}, final score is: {calculate_score(user_cards, computer_cards)}")
            print(f"    Computer's final hand is: {computer_cards}, final score: {sum(computer_cards)}")
            compare(user_total=calculate_score(user_cards, computer_cards), computer_total=sum(computer_cards))
            new_game = input("Do you want to play another game of Blackjack? Type 'y' or 'n': ").lower()
            if new_game == "y":
                play = True
                user_cards = []
                computer_cards = []
                deal_user_card()
                deal_user_card()
                deal_computer_card()
                deal_computer_card()
                user_score = 0
                computer_score = 0
            elif new_game == "n":
                play = False


