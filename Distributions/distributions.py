#%%
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

cancer_filepath = r"C:\Desktop\DATA VISUALIZATION - KAGGLE\Distributions\cancer.csv"

cancer_data = pd.read_csv(cancer_filepath, index_col="Id")

print(cancer_data.head())

# Histograms for benign and maligant tumors
#sns.histplot(data=cancer_data, x = "Area (mean)", hue = "Diagnosis")

# KDE plots for benign and malignant tumors
sns.kdeplot(data = cancer_data, x = "Radius (worst)", hue = "Diagnosis", shade = True)
# %%
