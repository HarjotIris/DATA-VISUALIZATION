#%%
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

spotify_filepath = r"C:\Desktop\DATA VISUALIZATION - KAGGLE\Choosing Plot Types and Custom Styles\spotify.csv"

spotify_data = pd.read_csv(spotify_filepath, index_col="Date", parse_dates=True)

# change the style of the figure
sns.set_style("dark")
#sns.set_style("whitegrid")
#sns.set_style("darkgrid")
#sns.set_style("white")
#sns.set_style("ticks")


# line chart
plt.figure(figsize=(12, 6))
sns.lineplot(data=spotify_data)
# %%
