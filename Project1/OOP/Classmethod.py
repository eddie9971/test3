# 可以访问类变量，不能访问instance 变量
# class Dog(object):
#
#     name = 'dogggg'
#
#     def __init__(self,name):
#         self.name = name
#
#     @classmethod #访问的是类变量 not instance created
#     def eat(self):
#         print(self)
#         print(f'dog {self.name} is eating')
#
#     @classmethod
#     def run(cls): #class
#         print(cls)
#
# d = Dog('abc')
# d.eat()

class Student(object):
    __stu_num = 0

    def __init__(self,name):
        self.name = name
        self.add_stu(self)
        # self.stu_num += 1 #其实是给instance a new variable,并不是类变量
        # Student.stu_num += 1
        # print(f'new student generated {self.name}, {self.stu_num}')

    @classmethod
    def add_stu(cls,obj): #obj stands for self instance
        if obj.name:
            cls.__stu_num += 1
            print(f'new student generated, number {cls.__stu_num}')

s1 = Student('aaa')
s2 = Student('bbb')
s3 = Student('ccc')

