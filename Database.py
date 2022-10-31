class my_class(object):
    import pandas as pd

url= "https://people.sc.fsu.edu/~jburkardt/data/csv/cities.csv"
df=pd.read_csv(url)
headers=["aaaaa","bbbb","c","d","e","f","g","h","i","j"]

#df.columns=headers

print(df.head(2))
#print(df.dtypes)
#print(df.describe(include='all'))
print(df.info)
    




