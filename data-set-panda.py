import pandas as pd
print(pd.__version__)

df = pd.read_csv('/Users/deepika-14647/Downloads/Pokemon.csv')
# print(df)
print(df.head(3))
# print(df.tail(3))
# print(df.columns)
# print(df['Name'].head(3))
# print(df['Legendary'])