# 不能访问类变量也不能访问instance变量
# staticmethod 隔离的跟class里的任何关系

class Student(object):
    role = 'stu'

    def __init__(self,name):
        self.name = name

    @staticmethod
    def fly(self):
        print(f'{self.name} is flying')
    @staticmethod
    def walk():
        print('walking')

s = Student('Jack')
# s.fly(s) 强行使用