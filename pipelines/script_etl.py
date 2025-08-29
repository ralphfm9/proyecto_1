import pandas as pd

df = pd.DataFrame({
    'column1': [1, 2, 3],
    'column2': ['A', 'B', 'C']
})
df.to_csv('data_mkt.csv', index=False)