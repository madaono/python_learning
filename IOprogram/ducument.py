import os
print(os.name)
# os.uname() 这个函数可以生成更加详细的系统信息，但是windows不支持
print(os.environ)
print(os.path.abspath('.'))
# 在某个目录下创建一个新目录，首先把新目录的完整路径表示出来:
# >>> os.path.join('/Users/michael', 'testdir')
# '/Users/michael/testdir'
# 然后创建一个目录:
# >>> os.mkdir('/Users/michael/testdir')
# 删掉一个目录:
# >>> os.rmdir('/Users/michael/testdir')


import json
d = dict(name='Bob', age=20, score=88)
json.dumps(d)
print(d)