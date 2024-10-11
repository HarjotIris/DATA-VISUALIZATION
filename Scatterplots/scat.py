#%%
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

candy_filepath = r"C:\Desktop\DATA VISUALIZATION - KAGGLE\Scatterplots\candy.csv"

candy_data = pd.read_csv(candy_filepath, index_col = "id")

#print(candy_data.head())
# Scatter plot showing the relationship between 'sugarpercent' and 'winpercent'
#sns.scatterplot(x = candy_data['sugarpercent'], y = candy_data['winpercent'])

#Scatter plot w/ regression line showing the relationship between 'sugarpercent' and 'winpercent'
#sns.regplot(x = candy_data['sugarpercent'], y = candy_data['winpercent'])

# Scatter plot showing the relationship between 'pricepercent', 'winpercent', and 'chocolate'
#sns.scatterplot(x = "pricepercent", y = "winpercent", hue = "chocolate", data = candy_data)

# Scatter plot showing the relationship between 'chocolate' and 'winpercent'
sns.swarmplot(x = candy_data['chocolate'], y = candy_data['winpercent'])
# %%
