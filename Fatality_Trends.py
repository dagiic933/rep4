import pandas as pd
import matplotlib.pyplot as plt

# Load the dataset
dataset_path = 'fatalities_isr_pse_conflict_2000_to_2023.csv'
events_data = pd.read_csv(dataset_path)

# Convert 'date_of_event' to datetime format
events_data['date_of_event'] = pd.to_datetime(events_data['date_of_event'])

# Add a new column 'nation' based on citizenship
events_data['nation'] = events_data['citizenship'].apply(lambda x: 'Israel' if x == 'Israeli' else 'Palestine')

# Group the data by the year and nation of the event and count the number of fatalities for each combination
fatality_trends = events_data.groupby([events_data['date_of_event'].dt.year, 'nation']).size()

# Unstack the DataFrame to get separate columns for each nation
fatality_trends = fatality_trends.unstack('nation', fill_value=0)

# Visualize fatality trends over time using a bar chart
plt.figure(figsize=(20, 10))
fatality_trends.plot(kind='bar', stacked=True, color=['skyblue', 'lightcoral'])
plt.title('Fatality Trends Over Time (Yearly Aggregation)')
plt.xlabel('Year')
plt.ylabel('Number of Fatalities')
plt.xticks(rotation=45, ha='right')
plt.legend(title='Nation')
plt.show()
