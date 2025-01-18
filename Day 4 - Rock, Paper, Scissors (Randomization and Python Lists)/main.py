# Go to https://replit.com/@appbrewery/rock-paper-scissors-start?v=1
import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

#Write your code below this line 👇

options = [rock, paper, scissors]

choice1 = input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n")
choice1 = int(choice1)
wrong_input = "Invalid choice! You lose!"
if choice1 == 0:
    print(options[0])
elif choice1 == 1:
    print(options[1])
elif choice1 == 2:
    print(options[2])
else:
    print(wrong_input)

print("Computer chose:")

options_length = (len(options) - 1)
comp_choice = (options[random.randint(0, options_length)])
print(comp_choice)

if choice1 == 0 and comp_choice == scissors:
    print("You win!")
elif choice1 == 0 and comp_choice == paper:
    print("You lose!")
elif choice1 == 1 and comp_choice == rock:
    print("You win!")
elif choice1 == 1 and comp_choice == scissors:
    print("You lose!")
elif choice1 == 2 and comp_choice == paper:
    print("You win!")
elif choice1 == 2 and comp_choice == rock:
    print("You lose!")
elif (choice1 == 0 and comp_choice == rock) or (choice1 == 1 and comp_choice == paper) or (choice1 == 2 and comp_choice == scissors):
    print("Draw")
