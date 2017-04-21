import pandas as pd
import numpy as np

csvframe = pd.read_csv('myCSV_01.csv')
csvframe2 = pd.read_table('myCSV_01.csv',sep=',')
# sep指定分隔符，可以是一个正则
# print(csvframe)

# csvframe2.to_csv('myCSV_O2.csv')

frame = pd.DataFrame(np.arange(4).reshape(2,2))
# print(frame.to_html())

frame2 = pd.DataFrame(np.random.random((4,4)),
                      index=['white','black','red','blue'],
                      columns=['up','down','right','left'])

s = ['<html>']
s.append('<head><title>my DateFrame</title></head>')
s.append('<body>')
s.append(frame2.to_html())
s.append('</body></html>')
html = ''.join(s)

html_file = open('myFrame.html','w')
html_file.write(html)
html_file.close()