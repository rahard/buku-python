import pandas as pd

df = pd.read_csv('cluster.csv', header=None)
df.columns = ['x', 'y']
print(df)
