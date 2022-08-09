#######################################
## I'm thinking of a number...
#
#
#
##
#######################################
##
import random
##
#######################################
## Static Code (For debugging purposes)

# Assign the streak to 0, then have the function count up.
streak = 0

# Max limit should be one number OVER the true limit, as python excludes the value given from randrange.
maxlimit = 3

# Work in progress
helpCount = 0

# Choose a number from one to the maxlimit (-1).
# botChoice = random.randrange(1, maxlimit)
# print(botChoice)

# print('I am thinking of a number from 1 to ' + str(maxlimit) + '.')

# guess = input('Enter your guess here: ')

# if guess == str(botChoice):
#     streak += 1 
#     print('Correct! You have a streak of: ' + str(streak) + '.')
# else:
#     print('Incorrect')

##################################################
def repeatGame():
    test = runGame()
    print(test)
    return

##################################################
def runGame():
    "Runs the game function. Chooses a # at random, and prompts you to guess it."
    
    # Globals
    global streak
    global maxlimit
    global helpCount

# Choose a number at random, with 1 being the minimum limit, and the maxlimit - 1 as the maximum

    botChoice = random.randrange(1, maxlimit - 1)

    # In case you want to cheat. 
    #print(botChoice) 

    print('[GAME] I am thinking of a number from 1 to ' + str(maxlimit - 1) + '.')

# If the bot's choice lies in the latter half of the maximum limit, then the game will give a hint.

    if botChoice > maxlimit//2:
        print(' - > HINT! < - The answer is in the latter half of ' + str(maxlimit - 1) + '!')

# If you asked for help before, the game will give you another round for free.

    if helpCount > 0:
        print('[GAME] Here is some more help. The answer is: ' + str(botChoice) + '.')
        helpCount -= 1

    guess = input('Enter your guess here: ')

# If guess = random choice, add 1 to the streak and maximum limit, announce result, then repeat.

    if guess == str(botChoice):
        streak += 1
        maxlimit += 1 
        print(' - - - - - > Correct! You have a streak of: ' + str(streak) + '. < - - - - -')
        repeatGame()

# If player types 'HELP', and they have a streak  >= 3, they can spoil the answer for a round at the cost of two streak 'points'. 

    elif guess == 'HELP' and streak >= 3:
        print('Here was the number: ' + str(botChoice))
        streak -= 2
        print('[GAME] You got some help, your streak is now ' + str(streak) + '. ')
        helpCount = 1
        repeatGame()

# If player types 'LOWER LIMIT' and they have a streak of 5, they can lower the maxlimit by 5 at the cost of 3 streak points. 
    elif guess == 'LOWER LIMIT' and streak >= 3:
        if maxlimit >= 8:
            print('[GAME] The maximum limit will be lowered by 5! Your streak is now: ' + str(streak) + '.')
            maxlimit -= 5
            streak -= 3
            repeatGame()
        else:
            print('[GAME] The maximum limit cannot be lowered that far!')
            repeatGame()

# If statements above are not true, or answer is incorrect, stop the game. 
    else:
        print('- - - > [GAME] Incorrect. Game Over. < - - - ')

test = runGame()
print(test)
######################################################