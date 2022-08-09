#####################
## Pandas Practice (FINALLY!)
##
##
## Created & Maintained by: Bryce Mathews
#####################
## Legend for startypes.csv
##  
## Star Types: 0 - Brown Dwarf, 1 - Red Dwarf, 2 - White Dwarf, 3 - Main Sequence, 4 - Supergiant, 5 - Hypergiant
##
##
##
#####################
##Loading Library
from numpy import average
import pandas as pd

#################################################################################################################
##Read Dataset & Assign global data variable

stars = pd.read_csv('startypes.csv')

###############################################################################################################
##Class M Selection & Printout

##Assign Local 'Class Variable' (M in this case) and count the number of class 'M' stars
class_m = stars[stars['Spectral Class'] == 'M']
mCount = class_m['Spectral Class'].count()

##Calculate min, max, and average temperature for class 'M' stars
class_m_min = class_m['Temperature (K)'].min()
class_m_max = class_m['Temperature (K)'].max()
class_m_avg = class_m['Temperature (K)'].mean().round(2)

##Format the min, max, and average temperature and assign a variable
summary_dict_m = {'Average Class M Temperature': class_m_avg,
                'Min Class M Temperature': class_m_min,
                'Max Class M Temerature': class_m_max}

##Print the summary variable and the mCount to the terminal

print('There is/are ' + str(mCount) + ' class M star(s) in the dataset.')
print(summary_dict_m)

###############################################################################################################
##Class B Selection & Printout

##Assign Local 'Class Variable' (B in this case) and count the number of class 'B' stars
class_b = stars[stars['Spectral Class'] == 'B']
bCount = class_b['Spectral Class'].count()

##Calculate min, max, and average temperature for class 'B' stars
class_b_min = class_b['Temperature (K)'].min()
class_b_max = class_b['Temperature (K)'].max()
class_b_avg = class_b['Temperature (K)'].mean().round(2)

##Format the min, max, and average temperature and assign a variable
summary_dict_b = {'Average Class B Temperature': class_b_avg,
                'Min Class B Temperature': class_b_min,
                'Max Class B Temperature': class_m_max}

##Print the summary variable and count of class B stars

print('There is/are ' + str(bCount) + ' class B star(s) in the dataset.')
print(summary_dict_b)

##############################################################################################################
##Class A Selection & Printout

##Assign Local 'Class Variable' (A in this case) and count the amount of class 'A' stars
class_a = stars[stars['Spectral Class'] == 'A']
aCount = class_a['Spectral Class'].count()

##Calculate min, max, and average temperature for class 'A' stars
class_a_min = class_a['Temperature (K)'].min()
class_a_max = class_a['Temperature (K)'].max()
class_a_avg = class_a['Temperature (K)'].mean().round(2)

##Format the min, max, and average temperature and assign a variable
summary_dict_a = {'Average Class A Temperature': class_a_avg,
                'Min Class A Temperature': class_a_min,
                'Max Class A Temperature': class_a_max}

##Print the summary variable and count of class 'A' stars

print('There is/are ' + str(aCount) + ' class A star(s) in the dataset.')
print(summary_dict_a)

###################################################################################################################
##Class F Selection & Printout

##Assign Local 'Class Variable' (F in this case) and count the number of class 'F' stars
class_f = stars[stars['Spectral Class'] == 'F']
fCount = class_f['Spectral Class'].count()

##Calculate min, max, and average temperature for class 'F' stars
class_f_min = class_f['Temperature (K)'].min()
class_f_max = class_f['Temperature (K)'].max()
class_f_avg = class_f['Temperature (K)'].mean().round(2)

##Format the min, max, and average temperature and assign a variable
summary_dict_f = {'Average Class F Temperature': class_f_avg,
                'Min Class F Temperature': class_f_min,
                'Max Class F Temperature': class_f_max}

##Print the summary variable and the fCount
print('There is/are ' + str(fCount) + ' class F star(s) in the dataset.')
print(summary_dict_f)
###############################################################################################################
##Class K Selection & Printout

##Assign Local 'Class Variable (K in this case) and count the number of class 'K' stars
class_k = stars[stars['Spectral Class'] == 'K']
kCount = class_k['Spectral Class'].count()

##Calculate min, max, and average temperature for class 'K' stars
class_k_min = class_k['Temperature (K)'].min()
class_k_max = class_k['Temperature (K)'].max()
class_k_avg = class_k['Temperature (K)'].mean().round(2)

##Format the min, max, and average temperature and assign a variable
summary_dict_k = {'Average Class K Temperature': class_k_avg,
                'Min Class K Temperature': class_k_min,
                'Max Class K Temperature': class_k_max}

##Print the summary variable and the kCount

print('There is/are ' + str(kCount) + ' class K star(s) in the dataset.')
print(summary_dict_k)

##################################################################################################################
##Class O Selection & Printout

##Assign Local 'Class Variable' (O in this case) and count the number of class 'O' stars
class_o = stars[stars['Spectral Class'] == 'O']
oCount = class_o['Spectral Class'].count() 

##Calculate min, max, and average temperature for class 'O' stars
class_o_min = class_o['Temperature (K)'].min()
class_o_max = class_o['Temperature (K)'].max()
class_o_avg = class_o['Temperature (K)'].mean().round(2)

##Format the min, max, and average temperature and assign a variable
summary_dict_o = {'Average Class O Temperature': class_o_avg,
                'Min Class O Temperature': class_o_min,
                'Max Class O Temperature': class_o_max}

##Print the summary variable and the oCount

print('There is/are ' + str(oCount) + ' class O star(s) in the dataset.')
print(summary_dict_o)

##################################################################################################################
##Class G Selection & Printout

##Assign Local 'Class Variable' (G in this case) and count the number of class 'G' stars
class_g = stars[stars['Spectral Class'] == 'G']
gCount = class_g['Spectral Class'].count()

##Calculate min, max, and average temperature for class 'G' stars
class_g_min = class_g['Temperature (K)'].min()
class_g_max = class_g['Temperature (K)'].max()
class_g_avg = class_g['Temperature (K)'].mean().round(2)

##Format the min, max, and average temperature and assign a variable
summary_dict_g = {'Average Class G Temperature': class_g_avg,
                'Min Class G Temperature': class_g_min,
                'Max Class G Temperature': class_g_max}

##Print the count of class 'G' stars as well as the summary
print('There is/are ' + str(gCount) + ' class G star(s) in the dataset.')
print(summary_dict_g)

##################################################################################################################

def summaryOfColumn(df, sc):
    """
    description: this function finds min, max, and mean of temp for a given spectral class;
    input: dataframe, user specified spectral class;
    output: print statement with desired information
    """
    # subset dataframe by user input sc
    df_sub = df[df['Spectral Class'] == sc]
    sc_count = df_sub['Spectral Class'].count()
    # calculate temp min, max, and mean for that sc
    temp_min = df_sub['Temperature (K)'].min()
    temp_max = df_sub['Temperature (K)'].max()
    temp_ave = df_sub['Temperature (K)'].mean().round(2)
    # compile the information
    summary_dict = {'Min Temp': temp_min, 'Max Temp': temp_max, 'Ave Temp': temp_ave}
    # output0
    statement = ('There is/are ' + str(sc_count) + ' class ' + str(sc) + ' stars in the dataset.')
    return statement, summary_dict
test = summaryOfColumn(stars, 'M')
print(test)