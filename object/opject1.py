# 为了给所有实例都绑定方法，可以给class绑定方法
def set_score(self, score):
    self.score = score


class Student(object):
    pass


Student.set_score = set_score

s1 = Student()

s1.set_score(200)

print(s1.score)


# 通常情况下，上面的set_score方法可以直接定义在class中，但动态绑定允许我们在程序运行的过程中动态给class加上功能，这在静态语言中很难实现。

# 但是，如果我们想要限制实例的属性怎么办？比如，只允许对Student实例添加name和age属性。

class Student1(object):
    __slots__ = ('name', 'age')

# 此时，Student1就只能动态绑定name,age属性了


# Python内置的@property装饰器就是负责把一个方法变成属性调用的：

class Student3(object):
    @property
    def score(self):
        return self.score

    @score.setter
    def score(self, value):
        if not isinstance(value, int):
            raise ValueError('score must be an integer!')
        if value < 0 or value > 100:
            raise ValueError('score must between 0~100')
        self._score = value


# @property的实现比较复杂，我们先考察如何使用。把一个getter方法变成属性，只需要加上@property就可以了，此时，@property本身又创建了另一个装饰器@score.setter，负责把一个setter方法变成属性赋值