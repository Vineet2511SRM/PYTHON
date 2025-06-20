#comparison query
import pandas as pd
data = {'name':['ALICE','BOB','CHARLIE'],'age':[25,30,27],'city':['NEW YORK','LOS ANGELES','CHICAGO']}

df = pd.DataFrame(data)
result = df.query('age>25')
print(result)

#combining combinations
result = df.query('age > 25 and city == "CHICAGO"')
print(result)

#string methods
#df.query('City.str.contains("LOS ANGELES")')
result = df.query('city.str.contains("LOS ANGELES")')
print(result)

#indexing-based query
data = {
    'Name': ['Alice', 'Bob', 'Charlie', 'David','Bala'],
    'Age': [25, 30, 22, 28,24],
    'City': ['New York', 'Los Angeles', 'Chicago', 'Houston','Chicago']
}
df = pd.DataFrame(data)
df.set_index('Name',inplace=True)
result = df.query('index=="Bob" | index=="David"') 
print(result)

