import pandas as pd
import matplotlib.pyplot as plt

# Load the dataset
dataset_path = 'fatalities_isr_pse_conflict_2000_to_2023.csv'
events_data = pd.read_csv(dataset_path)

# Filter data for Palestinian and Israeli citizenships
selected_citizenships = ['Palestinian', 'Israeli']
filtered_data = events_data[events_data['citizenship'].isin(selected_citizenships)]

# Count the occurrences of each citizenship
citizenship_counts = filtered_data['citizenship'].value_counts()

# Visualize the distribution of fatalities across Palestinian and Israeli citizenships
plt.figure(figsize=(8, 6))
citizenship_counts.plot(kind='bar', color=['skyblue', 'lightcoral'])
plt.title('Distribution of Fatalities by Citizenship (Palestinian vs. Israeli)')
plt.xlabel('Citizenship')
plt.ylabel('Number of Fatalities')
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.xticks(rotation=45, ha='right', fontsize=10)
plt.show()
