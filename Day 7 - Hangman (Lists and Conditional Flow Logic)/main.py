import random
logo = ''' _                                             
| |                                            
| |__   __ _ _ __   __ _ _ __ ___   __ _ _ __  
| '_ \ / _` | '_ \ / _` | '_ ` _ \ / _` | '_ \ 
| | | | (_| | | | | (_| | | | | | | (_| | | | |
|_| |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                    __/ |                      
                   |___/                       
'''

# word_list = ["ardvark", "baboon", "camel"]
word_list = [
    'abruptly', 'absurd', 'abyss', 'affix', 'askew', 'avenue', 'awkward', 'axiom', 'azure',
    'bagpipes', 'bandwagon',
    'banjo',
    'bayou',
    'beekeeper',
    'bikini',
    'blitz',
    'blizzard',
    'boggle',
    'bookworm',
    'boxcar',
    'boxful',
    'buckaroo',
    'buffalo',
    'buffoon',
    'buxom',
    'buzzard',
    'buzzing',
    'buzzwords',
    'caliph',
    'cobweb',
    'cockiness',
    'croquet',
    'crypt',
    'curacao',
    'cycle',
    'daiquiri',
    'dirndl',
    'disavow',
    'dizzying',
    'duplex',
    'dwarves',
    'embezzle',
    'equip',
    'espionage',
    'euouae',
    'exodus',
    'faking',
    'fishhook',
    'fixable',
    'fjord',
    'flapjack',
    'flopping',
    'fluffiness',
    'flyby',
    'foxglove',
    'frazzled',
    'frizzled',
    'fuchsia',
    'funny',
    'gabby',
    'galaxy',
    'galvanize',
    'gazebo',
    'giaour',
    'gizmo',
    'glowworm',
    'glyph',
    'gnarly',
    'gnostic',
    'gossip',
    'grogginess',
    'haiku',
    'haphazard',
    'hyphen',
    'iatrogenic',
    'icebox',
    'injury',
    'ivory',
    'ivy',
    'jackpot',
    'jaundice',
    'jawbreaker',
    'jaywalk',
    'jazziest',
    'jazzy',
    'jelly',
    'jigsaw',
    'jinx',
    'jiujitsu',
    'jockey',
    'jogging',
    'joking',
    'jovial',
    'joyful',
    'juicy',
    'jukebox',
    'jumbo',
    'kayak',
    'kazoo',
    'keyhole',
    'khaki',
    'kilobyte',
    'kiosk',
    'kitsch',
    'kiwifruit',
    'klutz',
    'knapsack',
    'larynx',
    'lengths',
    'lucky',
    'luxury',
    'lymph',
    'marquis',
    'matrix',
    'megahertz',
    'microwave',
    'mnemonic',
    'mystify',
    'naphtha',
    'nightclub',
    'nowadays',
    'numbskull',
    'nymph',
    'onyx',
    'ovary',
    'oxidize',
    'oxygen',
    'pajama',
    'peekaboo',
    'phlegm',
    'pixel',
    'pizazz',
    'pneumonia',
    'polka',
    'pshaw',
    'psyche',
    'puppy',
    'puzzling',
    'quartz',
    'queue',
    'quips',
    'quixotic',
    'quiz',
    'quizzes',
    'quorum',
    'razzmatazz',
    'rhubarb',
    'rhythm',
    'rickshaw',
    'schnapps',
    'scratch',
    'shiv',
    'snazzy',
    'sphinx',
    'spritz',
    'squawk',
    'staff',
    'strength',
    'strengths',
    'stretch',
    'stronghold',
    'stymied',
    'subway',
    'swivel',
    'syndrome',
    'thriftless',
    'thumbscrew',
    'topaz',
    'transcript',
    'transgress',
    'transplant',
    'triphthong',
    'twelfth',
    'twelfths',
    'unknown',
    'unworthy',
    'unzip',
    'uptown',
    'vaporize',
    'vixen',
    'vodka',
    'voodoo',
    'vortex',
    'voyeurism',
    'walkway',
    'waltz',
    'wave',
    'wavy',
    'waxy',
    'wellspring',
    'wheezy',
    'whiskey',
    'whizzing',
    'whomever',
    'wimpy',
    'witchcraft',
    'wizard',
    'woozy',
    'wristwatch',
    'wyvern',
    'xylophone',
    'yachtsman',
    'yippee',
    'yoked',
    'youthful',
    'yummy',
    'zephyr',
    'zigzag',
    'zigzagging',
    'zilch',
    'zipper',
    'zodiac',
    'zombie',
]

print(logo)

stages = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']

# Todo_1: Randomly choose a word from the word_list and assign it to a variable called chosen_word

# Todo_2: Ask the user to guess a letter and assign their answer to a variable called guess. Make guess lowercase

# Tod0_3: Check if the letter the user guessed (guess) is one of the letters in the chosen_word

# Todo_4: Create an empty List called Display. For each letter in the chosen-word, add a "_" to 'display'
# So if the chosen_word was "apple", display should be ["_", "_", "_", "_", "_"] with 5"_" representing
# each letter

# Todo_5: Loop through each position in the chosen_word. if the letter at the position matches "guess"
# then reveal that letter in the display at the position

# Todo_5: Print "display" and you should see the guessed letter in the correct position and every other letter
# replaced with "_"

# hint: don't worry about getting the user to guess the next letter.

# Todo_6: Use a while loop to let the user guess again. The loop should only stop once the user has guessed all the
# letters in the chosen_word and "display" has no more blanks("_") then you can the user they have won

# Todo_7: create a variable called 'lives' to keep track of the number of lives left. Set 'lives' to equal 6
# if guess is not a letter in the chosen_word, then reduce 'lives' by 1.
# if 'lives' goes down to 0, then the game should stop, and it should print "You lose"
# print the ASCII art from 'stages' that corresponds to the current number of 'lives' the user has remaining


chosen_word = word_list[random.randint(0, len(word_list) - 1)]

# Debugging word
# print(f"Your chosen word is {chosen_word}")

display = []

for char in range(0, len(chosen_word)):
    display.append("_")
print(display)

display_index = 0
end_game = False
lives = 6

# while display_index <= (len(display)-1):
while not end_game:
    guess = input("Guess a letter: ")
    guess = guess.lower()
    word_index = 0

    for char in range(0, len(chosen_word)):
        if guess == chosen_word[word_index]:
            display.pop(word_index)
            display.insert(word_index, guess)
            # word_index += 1
            display_index += 1
        word_index += 1

    if guess not in chosen_word:
        print(f"You guessed the letter '{guess}' that's not in the word. You lose a life.")
        lives -= 1

    print(display)
    print(f"Number of lives left: {lives}")
    print(stages[lives])

    if lives == 0:
        print("Game Over. You lose!")
        print(f"The word was '{chosen_word}'")
        end_game = True

    if "_" not in display:
        print("Game over. You win!")
        end_game = True
