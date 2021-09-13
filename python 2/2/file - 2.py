import pandas as pd

df = pd.read_csv('electronic-card-transactions-aug-2021-csv-tables.csv')
df.head()
# print(df.head())
x = df.iloc[:, 1:3]
# print(x)
# df.info()
# ------------------------------------------ total (value columns)
Total = df['Magnitude'].sum()
print('total:', Total)

# ------------------------------------------
mean = df['Magnitude'].mean()
print(mean)
