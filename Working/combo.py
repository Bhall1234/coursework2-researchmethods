import pandas as pd

# Load your initial detailed data
df = pd.read_csv('grouped_data.csv')

# Normalise the participant numbers
df['n_participants'] = df['n_participants'] / 1000

# Aggregate the data
df_grouped = df.groupby(['diet_group', 'age_group', 'grouping']).agg({
    'mean_ghgs': 'sum', 
    'mean_land': 'sum', 
    'mean_watscar': 'sum', 
    'mean_ghgs_ch4': 'sum', 
    'mean_ghgs_n2o': 'sum', 
    'mean_bio': 'sum', 
    'mean_acid': 'sum', 
    'mean_watuse': 'sum',
    'n_participants': 'sum',  # Sum already adjusted participant numbers
}).reset_index()

# Save to CSV
df_grouped.to_csv('remove_monte_carlo.csv', index=False)

# Print DataFrame to check
print(df_grouped)