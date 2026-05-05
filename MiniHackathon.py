# Kunal Tyagi(202501100400193)
# Nirnay Mathur(202501100400230)

#Importing Libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
df = pd.read_csv("PS24_Dataset_24.csv")
df.dropna(inplace=True)
print("Clean Dataset:\n", df.head())
df['Total'] = df.sum(axis=1)
df['Average'] = np.mean(df[['A','B','C','D']], axis=1)
mean_values = np.mean(df[['A','B','C','D']], axis=0)
std_values = np.std(df[['A','B','C','D']], axis=0)
print("\nMean Values:\n", mean_values)
print("\nStandard Deviation:\n", std_values)
top_row = df.loc[df['Total'].idxmax()]
print("\nHighest Total Row:\n", top_row)
lowest_row = df.loc[df['Total'].idxmin()]
print("\nLowest Total Row:\n", lowest_row)
#BArchart
plt.bar(['A','B','C','D'], mean_values,color='pink',edgecolor='black')
plt.title("Average Values of Columns")
plt.xlabel("Columns")
plt.ylabel("Mean")
plt.show()
#histogram
plt.hist(df['Total'],color='yellow',edgecolor='black')
plt.title("Distribution of Total Values")
plt.xlabel("Total")
plt.ylabel("Frequency")
plt.show()
#Linechart
plt.plot(df['Average'],color='red',marker='o')
plt.title("Average Trend")
plt.xlabel("Index")
plt.ylabel("Average Value")
plt.show()