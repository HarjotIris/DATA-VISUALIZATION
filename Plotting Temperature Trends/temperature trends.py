import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

# load the dataset
path = r"C:\Users\HP\temperature-change\Environment_Temperature_change_E_All_Data_NOFLAG.csv"

df = pd.read_csv(path, encoding = 'latin1')

print(df.head())

# check column names
print(df.columns)

# check the missing values
print(df.isnull().sum())

# get basic statistics
print(df.describe())

# filter data for a specific area and element
filtered_df = df[(df['Area'] == 'United Kingdom') & (df['Element'] == 'Temperature change') ]

# display the filtered dataset
print(filtered_df)

# melt the df to have years in one column
melted_df = filtered_df.melt(id_vars = ['Area', 'Element', 'Unit', 'Area Code', 'Months Code', 'Months', 'Element Code'],
                             var_name = 'Year',
                             value_name = "Temperature change")

melted_df['Year'] = melted_df['Year'].str.replace('Y', '').astype(int)
print(melted_df.head())

# USING MATPLOTLIB

# plot the data
plt.figure(figsize=(10,6))
plt.plot(melted_df['Year'], melted_df['Temperature change'], marker = 'o',
         linestyle = '-')

# add labels and titles
plt.title("UK Temperature Change Over Time (1961-2019)")
plt.xlabel("Year")
plt.ylabel("Temperature Change (°C)")
plt.grid(True)

plt.show()

# USING SEABORN

sns.set_theme(style='whitegrid')
plt.figure(figsize=(10,6))
sns.lineplot(data=melted_df, x = 'Year', y ='Temperature change', marker='o')
plt.title("UK Temperature Change Over Time (1961-2019)")
plt.xlabel("Year")
plt.ylabel("Temperature Change (°C)")

sns.regplot(data=melted_df, x = 'Year', y = 'Temperature change', scatter=False, color = 'red', label='Trendline')
plt.legend()
plt.savefig('temperature_trend.png', dpi=300, bbox_inches='tight')
plt.show()

years = melted_df['Year']
temps = melted_df['Temperature change']

years = years.to_numpy()
temps = temps.to_numpy()

# Fit a trendline (linear regression)
slope, intercept = np.polyfit(years, temps, 1)

# Generate trendline values
trendline = slope * years + intercept

# Plot data
plt.figure(figsize=(10, 5))
plt.scatter(years, temps, label="Actual Data", color="blue")
plt.plot(years, trendline, label=f"Trendline (Slope: {slope:.4f})", color="red")

# Labels and title
plt.xlabel("Year")
plt.ylabel("Temperature (°C)")
plt.title("Temperature Trend")
plt.legend()
plt.grid()

# Save and show figure
plt.savefig("trendline.png")
plt.show()

# Compute R-squared
correlation_matrix = np.corrcoef(years, temps)
r_squared = correlation_matrix[0, 1] ** 2

print(f"R-squared: {r_squared:.4f}")

