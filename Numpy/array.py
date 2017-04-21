import numpy as np
import pandas as pd

s = pd.Series([12,-4,7,9], index=['a','b','c','d'])
# print(s)

# print(s.values)
# print(s.index)

# print(s>8)
# print(s[s>8])

serd = pd.Series([1,0,2,1,2,3],index=['white','white','blue','green','green','yellow'])
# print(serd.unique())
# print(serd.value_counts())


data = {'color':['blue','green','yellow','red','white'],
        'object':['ball','pen','pencil','paper','mug'],
        'price':[1.2,1.0,0.6,0.9,1.7]}
frame = pd.DataFrame(data)
# frame2 = pd.DataFrame(data, columns=['object','price'])
# print(frame)
# print(frame2)
frame['new']=12
# print(frame)

s1 = pd.Series([1,2,3,4],['white','yellow','green','blue'])
s2 = pd.Series([1,4,7,2,1],['white','yellow','black','blue','brown'])

print(s1+s2)

frame1 = pd.DataFrame(np.arange(16).reshape((4,4)),
                      index=['red','blue','yellow','white'],
                      columns=['ball','pen','pencil','paper'])
frame2 = pd.DataFrame(np.arange(12).reshape((4,3)),
                      index=['blue','green',' ','yellow'],
                      columns=['mug','pen','ball'])
print(frame1+frame2)