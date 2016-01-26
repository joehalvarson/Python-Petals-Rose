import sys, random
## The instructions
print("""The name of the game is 'Petals Around the Rose'\n
RULES:\n
1. The name of the game is significant.\n
2. Every answer is zero or an even number.\n
3. There is one correct answer for every throw of the dice.\n""")
##play is initiated empty, and the game auto-starts
play = ""
while play.lower() != "q":
    ##The dice. The first update will seek to auto-build the dice instead
    dice = {
        1: [
            "|---|\n"
            "| o |\n"
            "|___|\n",
        ],
        2: [
            "|o--|\n"
            "|   |\n"
            "|__o|\n",
        ],
        3: [
            "|o--|\n"
            "| o |\n"
            "|__o|\n",
        ],
        4: [
            "|o-o|\n"
            "|   |\n"
            "|o_o|\n",
        ],
        5: [
            "|o-o|\n"
            "| o |\n"
            "|o_o|\n",
        ],
        6: [
            "|o-o|\n"
            "|o o|\n"
            "|o_o|\n",
        ]
    }
    ##This randmoly generates 6 numbers from 1 to 6
    dicenums = []
    while len(dicenums) < 6:
        randdie = random.randrange(1,7)
        dicenums.append(randdie)
    ##Instead of the sort of magic read variable, probably an cleaner way to accomplish this
    read = 0
    ##This stores the total of the Petals Around the Rose (and spoils the game)
    total = 0
    while read < 6:
        if dicenums[read] == 3:
            total += 2
            read += 1
        elif dicenums[read] == 5:
            total += 4
            read += 1
        else:
            read += 1
    ##Array to store the ASCII dice images based on the randomly rolled number
    dies = []
    ##This adds the ASCII dice to the dies array
    for die in dicenums:
        dies.append(dice[die])
    print("You rolled:")
    ##Variable to get an integer of dies length
    dies_length = len(dies)
    ##Prints the dice to the screen. \n.join() feels like a hack to make dice print on new line
    for i in range(dies_length):
        print("\n".join(dies[i]))
    guess = input("What is your guess?")
    ##Words can't be used
    if int(total) == int(guess):
        print("You got that one!")
        play = input("Press Y to play! Press Q to quit!")
    else:
        print("That wasn't right. The correct total is " + str(total) + ".")
        play = input("Press Y to play! Press Q to quit!")
else:
    sys.exit(0)
