import pandas as pd
data = {
    "name": ["abhi",None,"satyam","satish","prashant"],

    "age": [67,None,67,56,None],
    "salary": [5000,None,67800,None,67890],
    "city": ["dilli",None,"pune","banglore","chenaai"]
}
df = pd.DataFrame(data)
print(df)
df.dropna(inplace=True)
print(df)