import numpy as np
import pandas as pd
from sklearn.decomposition import PCA
from sklearn.impute import SimpleImputer

df = pd.read_csv('cancer.csv')
df = df.replace('?', np.nan)
df3 = df.iloc[:, 1:10]
# print(df3.isnull().sum())


imputer = SimpleImputer(missing_values=np.nan, strategy='mean')
imputer = imputer.fit(df3)
df3 = imputer.transform(df3)
# df3.isnull().sum()

pca = PCA(n_components=2)
principalComponents = pca.fit_transform(df3)
principalDf = pd.DataFrame(data=principalComponents
                           , columns=['principal component 1', 'principal component 2'])
# print(principalDf)

df3 = pd.concat([df["class"]])
cancer = pd.concat([principalDf, df['class']], axis=1)
print(cancer)
