import pandas as pd
#basic method
#S = pd.Series(data,index = [index])
S = pd.Series([0.25,0.5,0.75,1])
print(S)
#Series with non-integer index
S = pd.Series([1,2,3,4],index = ['a','b','c','d'])
print(S)