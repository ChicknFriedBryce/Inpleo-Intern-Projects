##############################
## Catagorization of stars 
##
##
## Created and managed by: Bryce Mathews
##############################
## Loading Library

from numpy import average
import pandas as pd

##############################
## Read dataset
## 
stars = pd.read_csv("startypes.csv")
##
##############################
## Some variables (in case you choose to input words instead of numbers.)

Star_Type = 4
Star_Color = 5
Spectral_Class = 6

##############################
##
## Index (In case you need to figure out what some catagories mean)
##
## Star Type 0 = Red Dwarf, 1 = Brown Dwarf, 2 = White Dwarf, 3 = Main Sequence, 4 = SuperGiants, 5 = HyperGiants
## 
###############################

def countCatagorical(df, col):

    """
    Description: Takes dataset and column and counts the amount of each value within said column
    Fails if the column is not catagorical
    """
    # Input: Dataframe, column number/name
    # Output: Count

    # If the catagory has a value over 3, resume the function.
    if (col > 4):

        # Create a subdf with only the given column, then count the calue of each variable.

        df_sub = stars[stars.columns[col]]
        df_count = df_sub.value_counts()
        
        return df_count
    
    # If not, return the fail statement
    else:
        wronginputstatement = ("That column is not catagorical. Please try again.")
        return wronginputstatement

#########################################
test = countCatagorical(stars, Star_Color)
print(test)


