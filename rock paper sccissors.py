def rpc():
    #DEFINE VARIABLES
    user = ''
    from random import choice
    t = [('r', 'ROCK'), ('p', 'PAPER'), ('s', 'SCISSORS')]
    #ITERATE THROUGH THE TUPLIST
    for a, b in t:
        #ASK FOR INPUT
        while user not in a:
            user = input('COURTESY OF KEVTECH' +
                         '\n\nCHOOSE R FOR ROCK, P FOR PAPER OR S FOR SCISCORS: ')
            guess = user.lower()
            c = choice(a)
            if (guess == 'r' and c == 's') or (guess == 'p' and c == 'r') or (guess == "s" and c == "p"):
                print(f'YOU WIN!! Robot chose {b}')
            elif (guess == "r" and c == 'p') or (guess == 'p' and c == 's') or (guess == 's' and c == 'r'):
                print(f'You Lost!! Robot chose {b}')
            elif guess == c:
                print(f'It is a tie.You both chose {b}')
            else:
                print('WRONG INPUT. TRY AGAIN')
            continue

rpc()
