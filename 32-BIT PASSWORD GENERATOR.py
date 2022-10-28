'''
A powerful 32-bit password generator designed for safety,
optimal password strength and unbeatable security.
Includes lowercase and uppercase letters, numbers,
special characters and symbols.
'''

#initialize Random
import random


def password_generator(length=4):

    #define initial variables, values and data types

    entry_types = ['lower', 'upper', 'numbers', 'symbols']

    lower_case = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm'
                  'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

    upper_case = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M',
                  'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

    number_char = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

    symbols_char = ['!', '@', '#', '$', '%',
                    '^', '&', '*', '_', '-', '+', '.', ',']

    ref_dict = {'lower': lower_case, 'upper': upper_case,
                'numbers': number_char, 'symbols': symbols_char}

    user_password = ''

    password_length = 32

    #create a loop to generate the password
    while password_length > 0:

        #shuffle through the character types and the choose a random character type
        random.shuffle(entry_types)
        layer_one = random.choice(entry_types)

        #reference the data in the character types through the dictionary
        reference = ref_dict[layer_one]

        #shuffle the characters in the character type chosen and select a random character.
        random.shuffle(reference)
        layer_two = random.choice(reference)

        #add the character to the password
        user_password += layer_two

        #continue loop until password is fully generated
        password_length -= 1

    return user_password

password_generator()
