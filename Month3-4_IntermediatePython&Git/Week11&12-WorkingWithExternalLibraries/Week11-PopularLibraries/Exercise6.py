# Group data by a specific column and calculate summary statistics for each group.

# Import the 'pandas' library to handle data manipulation
import pandas as pd

# Load the CSV file into a DataFrame
df = pd.read_csv('C:/Users/geoko/Desktop/PythonBackEndRoadmap/Month3-4_IntermediatePython&Git/Week11&12-WorkingWithExternalLibraries/Week11-PopularLibraries/WorldPopulationByCountry.csv')

# Group the data by a specific column (the column name is 'Population 2024')
grouped_df = df.groupby('Population 2024')

# Calculate summary statistics for each group
summary_stats = grouped_df['Population 2024'].describe()
print(summary_stats)
