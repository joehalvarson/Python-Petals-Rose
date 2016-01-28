import sys, drSettings
from diceroll import *

drSettings.init()

## The instructions
print('You have %s correct plays.' %drSettings.wins)
print('''The name of the game is "Petals Around the Rose"\n
RULES:
1. The name of the game is significant.
2. Every answer is zero or an even number.
3. There is one correct answer for every throw of the dice.\n''')
##Technically accepts any input that isn't Q/q to start, Q/q quits
play = input('Press Enter to Play, Q to Quit.')
while play.lower() != 'q':
    ##Calls the dice function with number of dice required
    diceRoll(6)
    ##This stores the total of the Petals Around the Rose (and spoils the game)
    total = 0
    gameDice = drSettings.dicenums
    for d in range(len(gameDice)):
        if gameDice[d] == 3:
            total += 2
        elif gameDice[d] == 5:
            total += 4
        else:
            continue
    guess = input('What is your guess?')
    ##Words can't be used
    if int(total) == int(guess):
        print('You got that one!')
        fh = open('drSettings.py', 'w')
        fh.write(wins += 1)
        fh.close()
        print('You have won a total of %s times!' %drSettings.wins)
        play = input('Press enter to play again, Q to quit!')
    else:
        print('That wasn\'t right. The correct total is %s.' %total)
        drSettings.wins -= 1
        print('You have won a total of %s times!' %drSettings.wins)
        play = input('Press enter to play again, Q to quit!')
else:
    sys.exit(0)
