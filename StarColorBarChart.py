# Import pyplot
from numpy import average
import pandas as pd
import matplotlib.pyplot as plt
#################

stars = pd.read_csv('startypes.csv')
# print(stars)

# Bar chart of star color

df_sub = stars['Star color']
df_count = df_sub.value_counts()
df_top = df_count.nlargest(n=10)

count_df = pd.DataFrame(df_top)
# print(count_df)

count_df['Color'] = count_df.index
# print(count_df)

# Rename Star Color column
count_df.columns = ['count', 'color']
# print(count_df)


# Define plot space
fig, ax = plt.subplots(figsize=(50, 6))

# Create bar plot
ax.bar(count_df['color'], 
       count_df['count'])
        
ax.set(title = "Star Color Frequency",
        xlabel = 'Colors',
        ylabel = 'Count of Colors')


plt.show()