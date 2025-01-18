from art import logo
import random

print(logo)
print("Welcome to the Number Guessing Game!")
random_number = random.randint(1, 100)
print("I'm thinking of a number between 1 and 100")
difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()
# print(random_number)


def easy():
    lives = 10
    while lives > 0:
        print(f"You have {lives} attempts remaining to guess the number")
        guessed_number = int(input("Make a guess: "))

        def compare():
            if (random_number > guessed_number) and lives == 1:
                print("Too low")
            elif (random_number < guessed_number) and lives == 1:
                print("Too high")
            elif random_number > guessed_number:
                print("Too low")
                print("Guess again")
            elif random_number < guessed_number:
                print("Too high")
                print("Guess again")
        compare()

        if guessed_number == random_number:
            print(f"You got it! The number is {random_number}")
            lives = 0
        else:
            lives -= 1
            if lives == 0:
                print(f"You have {lives} guesses remaining, you lose!")


def hard():
    lives = 5
    while lives > 0:
        print(f"You have {lives} attempts remaining to guess the number")
        guessed_number = int(input("Make a guess: "))

        def compare():
            if (random_number > guessed_number) and lives == 1:
                print("Too low")
            elif (random_number < guessed_number) and lives == 1:
                print("Too high")
            elif random_number > guessed_number:
                print("Too low")
                print("Guess again")
            elif random_number < guessed_number:
                print("Too high")
                print("Guess again")
        compare()

        if guessed_number == random_number:
            print(f"You got it! The number is {random_number}")
            lives = 0
        else:
            lives -= 1
            if lives == 0:
                print(f"You have {lives} guesses remaining, you lose!")


if difficulty == "easy":
    easy()
elif difficulty == "hard":
    hard()