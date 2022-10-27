from random import randint
def guess():
    guess = 0
    a = randint(1, 1000)
    while guess != a:
        guess = input('Guess a number between 1 and 1000: ')
        if guess.isdigit() == False or int(guess) > 1000:
            print('Please choose a number between 1-1000 dammit')
        elif int(guess) > a:
            print('Oops! Guessed too high!')
        elif int(guess) < a:
            print('Oops! Guessed too low')
        else:
            print("YOU WIN!!!")
            break
guess()
