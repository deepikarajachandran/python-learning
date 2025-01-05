import pandas as pd
print(pd.__version__)


#Series
n1 = pd.Series([10,20,30], index=['a', 'b', 'c'])
# print(n1)
# print(n1['b'])

#DataFrame
data = {
    'Name': ['Alice', 'Bob', 'Charlie'],
    'Age': [23, 33, 23],
    'Salary': [1234, 324, 456]
}
df = pd.DataFrame(data)
print(df.sort_values('Salary', ascending=False))

