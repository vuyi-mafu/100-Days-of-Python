from art import logo
from art import vs
from game_data import data
import random

first_details = data[random.randint(0, len(data) - 1)]
second_details = data[random.randint(0, len(data) - 1)]
while first_details == second_details:
    second_details = data[random.randint(0, len(data) - 1)]

# print(first_details)
# print(second_details)


game_on = True
score = 0


def start_game():
    if first_details != second_details:
        name1 = first_details['name']
        description1 = first_details['description']
        country1 = first_details['country']
        name2 = second_details['name']
        description2 = second_details['description']
        country2 = second_details['country']
        # print(logo)
        print(f"Compare A: {name1}, a {description1}, from {country1}")
        print(vs)
        print(f"Against B: {name2}, a {description2}, from {country2}")


while game_on:
    print(logo)
    if score > 0:
        print(f"You're right! Current score is: {score}")
    start_game()
    decision = input("Who has more followers? Type 'A' or 'B': ").lower()
    first_follower_count = first_details['follower_count']
    second_follower_count = second_details['follower_count']

    if decision == "a" and (first_follower_count > second_follower_count):
        score += 1
        # print(f"You're right! Current score is: {score}")
        for sub in first_details:
            if sub in second_details:
                first_details[sub] = second_details[sub]
        # print(first_details)
    elif decision == "b" and (second_follower_count > first_follower_count):
        score += 1
        # print(f"You're right! Current score is: {score}")
        for sub in first_details:
            if sub in second_details:
                first_details[sub] = second_details[sub]
    elif decision == "a" and (first_follower_count < second_follower_count):
        print(f"You lose. Your final score is: {score}")
        game_on = False
    elif decision == "b" and (second_follower_count < first_follower_count):
        print(f"You lose. Your final score is: {score}")
        game_on = False
    second_details = data[random.randint(0, len(data) - 1)]
