import pandas as pd 

df=pd.read_csv("pycsv.csv")
print(df)
df=df.insert(4,4,["Keyboard","a10",90])
print(df)
