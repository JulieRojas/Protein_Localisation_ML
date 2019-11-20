import matplotlib
import pandas as pd
import csv

df = pd.read_csv('data/Dataset.csv', sep="\t")
df.head()
print(df.columns)
df.groupby("Compartment Prediction").count().hist()