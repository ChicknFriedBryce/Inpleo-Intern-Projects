#############################
## Name / Age Dictionary
#
#
#
## Created by: Bryce Mathews
##############################
## Library
import json
import random
from unicodedata import name
##
###############################
# Create a blank dictionary
name_age = {}

########################################################################
# Repeats the dataBot funtion after a print.

def repeatDataBot():
    dataBot()
    return

#########################################################################
# Function for adding an entry to the dictionary.

def addEntry():

    """Input: name/age
    Output: name/age added to dictionary"""

    newname = input('Enter your name here: ')
    newage = input('Enter your age here: ')

    # If newage is an integer, add the name and the age to the dictionary, then repeat the entry.
    if (int(newage) // 1): 
        name_age[str(newname)] = str(newage)
        print(name_age)
        dataBot()
        return
    # If age input is NOT an integer, send error message below.
    else:
        print('This is not an age. Please try again.')
        dataBot()
        return

#########################################################################
# Function for removing an entry

def removeEntry():

    removename = input('Enter the name you wish to remove: ')
    del name_age[str(removename)]
    print ('Sucess! ' + removename + ' has been removed from the database.')
    dataBot()
    return

#########################################################################
# Function for appeding an entry

def appendEntry():

    changename = input('Please enter the name you would lke to change: ')
    changeage = input('Please enter the year you would like to edit: ')

    if (changename in name_age):
        name_age.update({str(changename): changeage})
        print ('Success, your name/age data has been changed.')
        print(name_age)
        dataBot()
    else:
        print(' - > Sorry. That name is not found in the dictionary. < -')
        dataBot()

#########################################################################
# Data functions hub

def dataBot():

    prompt = input('Welcome to the name and age database! Would you like to Add, Remove, Append, or Print an entry? ')

    if (str(prompt) == 'Add'):
        addEntry()

    elif (str(prompt) == 'Remove'):
        removeEntry()

    elif (str(prompt) == 'Append'):
        appendEntry()

    elif (str(prompt) == 'Print'):
        print(name_age)
        repeatDataBot()

    else:
        print('- > I do not recognize that response. Please try again. < -')
        repeatDataBot()

test = dataBot()
print(test)