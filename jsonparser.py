import pandas as pd

df = pd.read_json(r'D:\DeepakKarna\Personal\practices\python\others\countryfile.json')
#print(df)
df1 = df[['name','alpha3Code','capital','region','population','area']]
df_cur = df[['currencies']]

cur = []

for i in range(len(df_cur)):
    cur.append((df_cur['currencies'][i])[0]['code'])

df1['currency_code'] = cur

df1 = df1.rename(columns = {'alpha3Code' : 'country_code'})

df1.to_csv('parsedfile.csv', index=False)
