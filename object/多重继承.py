class Animal(object):
    pass

class Mammal(Animal):
    pass

class Runnable(object):
    pass

class Dog(Mammal, Runnable):
    pass



# 定制类
# __iter__

# 如果一个类想被用于for ... in循环，类似list或tuple那样，就必须实现一个__iter__()方法，该方法返回一个迭代对象，然后，Python的for循环就会不断调用该迭代对象的__next__()方法拿到循环的下一个值，直到遇到StopIteration错误时退出循环。

# 我们以斐波那契数列为例，写一个Fib类，可以作用于for循环：