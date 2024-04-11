import pandas as pd

df = pd.read_csv('raws.csv', encoding='utf-8-sig', sep='\s*,\s*', engine='python')

res = df.groupby([df.columns[0],df.columns[1]])[[df.columns[2]]].mean().reset_index()

print(res)
