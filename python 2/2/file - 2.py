import numpy as np
import pandas as pd

df = pd.read_csv('electronic-card-transactions-aug-2021-csv-tables.csv')
df.head()
# print(df.head())
x = df.iloc[:, 1:3]
# print(x)
# df.info()
# ------------------------------------------ total (value columns)
Total = df['Magnitude'].sum()
# print('total:', Total)

# -------------------------------------------
mean = df['Magnitude'].mean()
# print(mean)
# print(round(mean,2))
# -------------------------------------------
df2 = pd.read_csv('Book1.csv')
# df2.head()
# print(df2.head())

# -------------------------------------------
# PCA
# from sklearn.preprocessing import StandardScaler
df.describe()
# print(df.describe())
# print(df.isnull().sum())

from sklearn.impute import SimpleImputer

df3 = pd.read_csv('cancer.csv')
df3 = df3.replace('?', np.nan)
a = df3.isna().sum()
print(a)
imputer = SimpleImputer(missing_values=np.nan, strategy='mean')
imputer = imputer.fit(df3)

df3 = imputer.transform(df3)
print(df3)
b = df3.isna().sum()
print(b)
# df3=df3.fillna(df.mean())

# pca = PCA(n_components=2)
# principalComponents = pca.fit_transform(df3)
# principalDf = pd.DataFrame(data = principalComponents
#              , columns = ['principal component 1', 'principal component 2'])
# print(principalDf)
