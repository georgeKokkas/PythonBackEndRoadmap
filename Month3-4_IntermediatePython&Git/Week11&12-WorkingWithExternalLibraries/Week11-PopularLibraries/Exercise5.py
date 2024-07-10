# Load a CSV file into a DataFrame and perform basic data analysis 
# (e.g., calculate average, filter data)

# Import the 'pandas' library to handle data manipulation
import pandas as pd

# Load the CSV file into a DataFrame
df = pd.read_csv('C:/Users/geoko/Desktop/PythonBackEndRoadmap/Month3-4_IntermediatePython&Git/Week11&12-WorkingWithExternalLibraries/Week11-PopularLibraries/WorldPopulationByCountry.csv')

# Print the first few rows of the DataFrame
print(df.head())

# Calculate the average of a column (the column name is 'Population 2024')
average_population2024 = df['Population 2024'].mean()
print(f"Average Population 2024: {average_population2024}")

# Filter the DataFrame to include only rows where the 'Population 2024' 
# column is greater than 1 billion
filtered_df = df[df['Population 2024'] > 1000000000 ]
print(filtered_df)

# Output :
#          Country  Population 2024  Population 2023  ... Growth Rate  World %  World Rank
# 0          India       1441719852       1428627663  ...      0.0092   0.1801           1
# 1          China       1425178782       1425671352  ...     -0.0003   0.1780           2
# 2  United States        341814420        339996563  ...      0.0053   0.0427           3
# 3      Indonesia        279798049        277534122  ...      0.0082   0.0350           4
# 4       Pakistan        245209815        240485658  ...      0.0196   0.0306           5

# [5 rows x 8 columns]
# Average Population 2024: 34688615.31196581
#   Country  Population 2024  Population 2023 Area (km2)  Density (/km2)  Growth Rate  World %  World Rank     
# 0   India       1441719852       1428627663         3M           485.0       0.0092   0.1801           1     
# 1   China       1425178782       1425671352       9.4M           151.0      -0.0003   0.1780           2     