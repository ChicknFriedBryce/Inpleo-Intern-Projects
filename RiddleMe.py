###########################
## RiddleMe
##
## Created by: Bryce Mathews
###########################
# Imports
import re
import time
import random
from timeit import repeat
import pandas as pd

##############################################
# Collection of riddles and answers
riddledata = {'riddles': ['What month of the year has 28 days?', 'I am tall when I am young, and I am short when I am old. What am I?', 'What has to be broken before you can use it?', 'What can you break, even if you never pick it up or touch it?', 'I shave every day, but my beard stays the same. What am I?', 'What cannot talk but will reply when spoken to?', 'The more of this there is, the less you see. What is it?', 'What has hands, but cannot clap?', 'Why cant dinosoars clap?','What has a head and a tail but no body?', 'What building has the most stories?', 'What kind of coat is best put on wet?', 'I am an odd number. Take away a letter and I become even. What number am I?', 'If two is company, and three is a crowd, what are four and five?', 'What five-letter word becomes shorter when you add two letters to it?', 'Two in a corner, one in a room, zero in a house, but one in a shelter. What is it?', 'What can go up a chimney down, but cannot go down a chimney up?', 'What can you catch, but not throw?', 'What has many teeth, but cannot bite?', 'What can travel all around the world without leaving its corner?', 'What is the end of everything?', 'A plane crashed between the border of France and Belgium. Where were the survivors buried?', 'Poor people have it. Rich people need it. If you eat it you die. What is it?', 'What runs, but never walks. Murmurs, but never talks. Has a bed, but never sleeps. And has a mouth, but never eats?', 'The person who makes it has no need of it; the person who buys it has no use for it. The person who uses it can neither see nor feel it. What is it?', 'I have branches, but no fruit, trunk, or leaves. What am I?', 'What belongs to you, but everyone else uses it?', 'What starts with a T, ends with a T, and has T in it?', 'Sara has four daughters, and each of her daughters has a brother. How many children does Sara have?', 'Take one out and scratch my head, I am now black but once was red. What am I?'], 'answer': ['All', 'Candle', 'Egg', 'Promise', 'Barber', 'Echo', 'Darkness', 'Clock', 'Theyre dead', 'Coin', 'Library', 'Paint', 'Seven', 'Nine', 'Short', 'R', 'Umbrella', 'Cold', 'Comb', 'Stamp', 'G', 'Nowhere', 'Nothing', 'River', 'Coffin', 'Bank', 'Name', 'Teapot', 'Five', 'Match']}

# Loading riddledata into a dataframe
riddledf = pd.DataFrame(data=riddledata, index=[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29])
#print(riddledf)

# firstriddle = random.choice(riddledf['riddles'])
# print(firstriddle)
# riddleanswer = riddledf.loc[riddledf['riddles'] == firstriddle, 'answer'].item()
# print(riddleanswer)

streak = 0
##############################################
# Repeat riddle function

def repeatGame():
    test = riddleMe()
    print(test)
    return

#############################################
# Riddle function

def riddleMe():

    """Chooses a riddle at random, prints it, then compares the response with the true answer."""

    # Globals
    global streak

# Choose random riddle from riddledata
    riddle = random.choice(riddledf['riddles'])
    riddler = riddledf.loc[riddledf['riddles'] == riddle, 'answer'].item()
    # riddler = (riddler['answer'])

    print(riddle)
    # print(str(riddler))

    response_1 = input()
    # print(response_1)

# If the given response alligns with the chosen riddle's answer, then increase the streak, and repeat. Else, return streak to 0, and stop the game
    if response_1 == str(riddler):
        print('----------> Correct <-----------')
        streak += 1
        print('Your streak is: ' + str(streak))

        return repeatGame()
    else:
        streak = 0
        return ('Incorrect. Game Over!')

##############################################
test = riddleMe()
print(test)

