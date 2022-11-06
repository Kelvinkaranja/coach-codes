'''
This is a simple guessing game where the computer randomly generates a number between 1 and 1000.
the player is then asked to guess the number until the guess is the same as the random number.

'''


from random import randint
def guess():
    #set initial guess state and generate a random digit.
    guess = 0
    a = randint(1, 1000)
    
    #create a loop asking for a guess until answer is found.
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
