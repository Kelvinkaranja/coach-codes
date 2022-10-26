'''
99 bottles is a group song originating from USA and Canada in the mid 20th Century that is often sung by
Boy Scouts, Girl Guides, Camps and many other recreational and social groups. 
Its simplistic and repetitive nature led to its virality and it is currently sung in many parts of the world in current times. 
Here is a lyric generator for the song.

'''


def ninety_nine_bottles_song():
    #set the number of lyric repetitions
    number = 99

    #loop around the song until the last bottle is off the wall
    while number > 0:
        if number == 1:
            print('1 bottle of beer on the wall, 1 bottle of beer.')
            print('Take one down, pass it around, no bottles of beer on the wall...')
            break
        else:
            print('{} bottles of beer on the wall, {} bottles of beer.'.format(
                number, number))
            print('Take one down, pass it around, {} bottles of beer on the wall...'.format(
                number-1))
            number -= 1
ninety_nine_bottles_song()
