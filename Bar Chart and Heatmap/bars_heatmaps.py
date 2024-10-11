#%%
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

ign_filepath = r"C:\Desktop\DATA VISUALIZATION - KAGGLE\Bar Chart and Heatmap\ign_scores.csv"

ign_data = pd.read_csv(ign_filepath, index_col = "Platform")

#print(ign_data)

plt.figure(figsize = (10, 10))
plt.title("Average score for racing games by platform")

sns.barplot(x = ign_data['Racing'], y = ign_data.index)
plt.xlabel("Genre")

sns.heatmap(data = ign_data, annot = True)

# %%
