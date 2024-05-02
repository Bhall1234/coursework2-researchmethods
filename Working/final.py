import pandas as pd

# Load the environmental impact data, already adjusted per participant
df = pd.read_csv('remove_monte_carlo.csv')

# Setup regional dietary preferences including population sizes
data = {
    'Region': ['London'] * 6 + ['Midlands'] * 6 + ['North'] * 6 + ['Scotland'] * 6 + ['Wales'] * 6, # Region names
    'diet_group': ['vegan', 'veggie', 'meat', 'fish', 'high_meat', 'none'] * 5, # Diet group names
    'Percentage': [4, 7, 18, 4, 64, 3] + [3, 5, 14, 3, 72, 3] + [3, 5, 14, 3, 72, 5] + [3, 3, 14, 5, 67, 8] + [0, 3, 15, 0, 78, 3], # Diet percentages
    'Population': [8982000] * 6 + [4934939] * 6 + [15000000] * 6 + [5447700] * 6 + [3131640] * 6 # Population sizes
}
diet_prefs = pd.DataFrame(data)

# Normalize string data for accurate merging
df['diet_group'] = df['diet_group'].str.lower()

# Calculate per-person impacts from the raw data
df['Per_Person_GHGs'] = df['mean_ghgs'] / df['n_participants']

# Merge datasets on 'diet_group' and multiply impacts by population percentages
combined_data = pd.merge(diet_prefs, df, on='diet_group', how='left')
combined_data['Scaled GHGs'] = combined_data['Per_Person_GHGs'] * combined_data['Population'] * (combined_data['Percentage'] / 100)

# Output results
combined_data.to_csv('regional_scaled_data_4.csv', index=False)
print(combined_data[['Region', 'diet_group', 'Percentage', 'Population', 'Per_Person_GHGs', 'Scaled GHGs']])