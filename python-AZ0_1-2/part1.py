import pandas as pd

df = pd.read_csv('World-happiness-report-2024.csv')
print(df.head())

print(df.info())

print(df.describe())