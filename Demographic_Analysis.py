import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the dataset
dataset_path = 'fatalities_isr_pse_conflict_2000_to_2023.csv'
events_data = pd.read_csv(dataset_path)

# Filter data for Palestinian and Israeli citizenships
selected_citizenships = ['Palestinian', 'Israeli']
filtered_data = events_data[events_data['citizenship'].isin(selected_citizenships)]

# Demographic Analysis: Age Distribution
plt.figure(figsize=(14, 6))
sns.histplot(data=filtered_data, x='age', bins=30, kde=True, hue='citizenship', multiple='stack', palette='Set2')
plt.title('Age Distribution of Fatalities by Citizenship')
plt.xlabel('Age')
plt.ylabel('Number of Fatalities')
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.show()

# Demographic Analysis: Gender Distribution
plt.figure(figsize=(8, 6))
sns.countplot(data=filtered_data, x='gender', hue='citizenship', palette='Set2')
plt.title('Gender Distribution of Fatalities by Citizenship')
plt.xlabel('Gender')
plt.ylabel('Number of Fatalities')
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.show()
