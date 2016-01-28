import random, drSettings
##Function to create a less than 100 number of six-sided dice
def diceRoll(n):
##The dice ASCII images are stored. Would like to figure out a programmatic
##way to build the dice allowing for dice with higher N sides
    dice = {
        1: [
            '|---|\n'
            '| o |\n'
            '|___|\n',
        ],
        2: [
            '|o--|\n'
            '|   |\n'
            '|__o|\n',
        ],
        3: [
            '|o--|\n'
            '| o |\n'
            '|__o|\n',
        ],
        4: [
            '|o-o|\n'
            '|   |\n'
            '|o_o|\n',
        ],
        5: [
            '|o-o|\n'
            '| o |\n'
            '|o_o|\n',
        ],
        6: [
            '|o-o|\n'
            '|o o|\n'
            '|o_o|\n',
        ]
    }
    ##This randmoly generates 6 numbers from 1 to 6
    while len(drSettings.dicenums) < n:
        randdie = random.randrange(1,7)
        drSettings.dicenums.append(randdie)
    ##Array to store the ASCII dice images based on the randomly rolled number
    dies = []
    ##This adds the ASCII dice to the dies array
    for die in drSettings.dicenums:
        dies.append(dice[die])
    print('You rolled: \n')
    ##Prints the dice to the screen. \n.join() feels like a hack to make dice print on new line
    for i in range(len(dies)):
        print('\n'.join(dies[i]))
