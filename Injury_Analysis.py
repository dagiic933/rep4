import pandas as pd
import matplotlib.pyplot as plt

# Load the dataset
dataset_path = 'fatalities_isr_pse_conflict_2000_to_2023.csv'
events_data = pd.read_csv(dataset_path)

# Exclude specific categories ('palestinian' and 'israel civilian')
exclude_categories = ['palestinian', 'israel civilian']
filtered_data = events_data[~events_data['citizenship'].isin(exclude_categories)]

# Analyze the 'type_of_injury' column
injury_data = filtered_data['type_of_injury']

# Count the occurrences of each type of injury
injury_counts = injury_data.value_counts()

# Select the top N most frequent types of injuries
top_n = 15
top_n_injuries = injury_counts[:top_n]

# Visualize the most common types of injuries
plt.figure(figsize=(12, 8))
top_n_injuries.plot(kind='barh', color='salmon')
plt.title(f'Most Common Types of Injuries (Excluding Palestinian and Israel Civilian)')
plt.xlabel('Number of Occurrences')
plt.ylabel('Type of Injury')
plt.grid(axis='x', linestyle='--', alpha=0.7)
plt.show()
