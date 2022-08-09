# Import pyplot
from numpy import average
import pandas as pd
import matplotlib.pyplot as plt
#################

stars = pd.read_csv('startypes.csv')
# print(stars)

# Bar chart of star color

df_sub = stars['Spectral Class']
df_count = df_sub.value_counts()

count_df = pd.DataFrame(df_count)
# print(count_df)

count_df['Class'] = count_df.index
# print(count_df)

# Rename Star Color column
count_df.columns = ['count', 'Class']
# print(count_df)


# Define plot space
fig, ax = plt.subplots(figsize=(50, 6))

# Create pie chart 
plt.pie(count_df['count'], labels = count_df['Class'], autopct='%.1f%%')

ax.set(title = 'Frequency of Star Class Types',
)

plt.show()