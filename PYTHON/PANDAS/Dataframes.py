import pandas as pd
import numpy as np
data = {'name':['ALICE','BOB','CHARLIE'],'age':[25,30,27],'gender':['F','M','M']}
df = pd.DataFrame(data)
print(df)
import pandas as pd 
d = { 'name': ['Bob','Bart','Bobby'], 'occupation': ['Lawyer','Programmer','Teacher']}
frame = pd.DataFrame(d, columns=['name','occupation'])
print(frame)
#creating data frame with numpy array
a = np.array([2012,2013,2020,2004])
dict_ndarray = {'year':a}
df_ndarray = pd.DataFrame(dict_ndarray)
print(df_ndarray)

data = [{'a': 1, 'b': 2},{'a': 5, 'b': 10, 'c': 20}]

#With two column indices, values same as dictionary keys
df1 = pd.DataFrame(data, index=['first', 'second'], columns=['a', 'b'])

#With two column indices with one index with other name
df2 = pd.DataFrame(data, index=['first', 'second'], columns=['a', 'b1'])
print(df1)
print(df2)