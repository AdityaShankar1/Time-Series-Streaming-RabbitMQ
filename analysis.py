import pandas as pd
import matplotlib.pyplot as plt

# 1. Load dataset
df = pd.read_csv("/Users/adityashankar/Downloads/electricity_dataset.csv")
df['DateTime'] = pd.to_datetime(df['DateTime'])
df.set_index('DateTime', inplace=True)

# 2. Basic exploration
print("Shape:", df.shape)
print("\nColumns:", df.columns.tolist())
print("\nSummary stats:\n", df.describe())

# 3. Export vs Import hours
df['Balance'] = df['Production'] - df['Consumption']
exports = df[df['Balance'] > 0]
imports = df[df['Balance'] < 0]
print(f"\nExport hours: {len(exports)}, Import hours: {len(imports)}")

# 4. Energy mix (average share of each source)
sources = ['Nuclear','Wind','Hydroelectric','Oil and Gas','Coal','Solar','Biomass']
mix = df[sources].mean() / df['Production'].mean() * 100
print("\nAverage energy mix (% of total production):\n", mix)

# 5. Hourly consumption pattern
df['Hour'] = df.index.hour
hourly_avg = df.groupby('Hour')['Consumption'].mean()
print("\nAverage consumption by hour:\n", hourly_avg)

# 6. Visualizations
plt.figure(figsize=(12,6))
df[['Consumption','Production']].resample('D').mean().plot()
plt.title("Daily Avg Consumption vs Production")
plt.ylabel("MW")
plt.show()

plt.figure(figsize=(6,6))
mix.plot(kind='pie', autopct='%1.1f%%')
plt.title("Average Energy Mix")
plt.ylabel("")
plt.show()

plt.figure(figsize=(10,5))
hourly_avg.plot(kind='bar')
plt.title("Average Consumption by Hour of Day")
plt.xlabel("Hour")
plt.ylabel("MW")
plt.show()
