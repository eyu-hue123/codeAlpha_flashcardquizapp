# unemployment_analysis.py

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load dataset
df = pd.read_csv('unemployment.csv')

# Display top records
print(df.head())
print(df.info())

# Rename columns for easier access
df.rename(columns={
    'Region': 'State',
    'Date': 'Month',
    'Estimated Unemployment Rate (%)': 'Unemployment Rate'
}, inplace=True)

# Check missing values
print("\nMissing Values:\n", df.isnull().sum())

# Summary stats
print("\nStatistical Summary:\n", df.describe())

# Lineplot for Unemployment Rate by State
plt.figure(figsize=(12, 6))
sns.lineplot(x='Month', y='Unemployment Rate', hue='State', data=df)
plt.title('Unemployment Rate Trends by State')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# Correlation Heatmap
plt.figure(figsize=(6, 4))
sns.heatmap(df.corr(), annot=True, cmap='coolwarm')
plt.title('Correlation Heatmap')
plt.show()