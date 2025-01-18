from art import logo

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
            'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
print(logo)

game_on = True
while game_on is True:

    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    shift = shift % 26

    def caesar(plain_text, shift_amount, direction_value):
        caesar_text = ""
        cipher_text = False

        for char in plain_text:
            if char in alphabet:
                if direction_value == "encode":
                    index = alphabet.index(char)
                    new_position = index + shift_amount
                    caesar_text += alphabet[new_position]
                    cipher_text = True
                elif direction_value == "decode":
                    index = alphabet.index(char)
                    new_position = index - shift_amount
                    caesar_text += alphabet[new_position]
            elif char not in alphabet:
                caesar_text += char

        if cipher_text:
            print(f"Your encoded text is: {caesar_text}")
        elif not cipher_text:
            print(f"Your decoded text is: {caesar_text}")

    caesar(plain_text=text, shift_amount=shift, direction_value=direction)
    continue_game = input("Do you want to restart cipher? Type 'yes' or 'no'\n").lower()
    if continue_game == "no":
        game_on = False
        print("Goodbye!")
    elif continue_game == "yes":
        game_on = True

#TODO-1: Import and print the logo from art.py when the program starts.

#TODO-2: What if the user enters a shift that is greater than the number of letters in the alphabet?
#Try running the program and entering a shift number of 45.
#Add some code so that the program continues to work even if the user enters a shift number greater than 26.
#Hint: Think about how you can use the modulus (%).
# TODO-3: What happens if the user enters a number/symbol/space?
# Can you fix the code to keep the number/symbol/space when the text is encoded/decoded?
# e.g. start_text = "meet me at 3"
# end_text = "•••• •• •• 3"
#TODO-4: Can you figure out a way to ask the user if they want to restart the cipher program?
#e.g. Type 'yes' if you want to go again. Otherwise type 'no'.
#If they type 'yes' then ask them for the direction/text/shift again and call the caesar() function again?
#Hint: Try creating a while loop that continues to execute the program if the user types 'yes'.
