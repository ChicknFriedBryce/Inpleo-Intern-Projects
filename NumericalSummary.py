##############################
## Numerical Summarization of stars 
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
Temperature = 0
Luminosity = 1
Radius = 2 
Absolute_Magnitude = 3


# Define summary function
def getColumnSummary(df, col):
    """"
    Description: this function finds and displays the five number summary of an inputtable numerical column.
    It will only work for numerical columns, catagorical columns will not be processed.
    input: dataframe, numerical Column
    output: print statement with summary
    """
    # If the column is numerical (Is among the first 4 columns), contintue the function.
    if (col <= 3):
        df_sub = stars[stars.columns[col]]
        
        # 5 Number Summary
        df_min = df_sub.min().round(5)
        df_quant1 = df_sub.quantile(.25).round(5)
        df_mean = df_sub.mean().round(2)
        df_quant3 = df_sub.quantile(.75).round(2)
        df_max = df_sub.max().round(2)

        # Create/Define the summary of min, mean, max, and quantiles
        ColSummary = {'Min: ': df_min, '1st Quantile ': df_quant1, 'Median ': df_mean, '3rd Quantile ': df_quant3, 'Max ': df_max}

        return ColSummary

    # If the input is not a numerical catagory, return a fail statement (Wrong Input). 
    else:
        wronginputstatement = ("That column is not numerical. Please try again.")
        return wronginputstatement
    
test = getColumnSummary(stars, Temperature)
print(test)