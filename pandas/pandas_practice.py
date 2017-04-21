# 合并
import numpy as np
import pandas as pd
print(pd)
frame1 = pd.DataFrame({'id':['ball','pencil','pen','mug','ashtray'],
                       'price':[12.33,11.44,33.21,13.23,33.62]})
frame2 = pd.DataFrame({'id':['pencil','pencil','ball','pen'],
                       'color':['white','red','red','black']})

print(pd.merge(frame1,frame2))
# merge()函数默认执行的是内连接操作；其他的选项有左连接右连接跟外连接。外连接将所有的键整合在一起，其效果相当于左连接跟右连接的和。链接类型由HOW选项指定


  n