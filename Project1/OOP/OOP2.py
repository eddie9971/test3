# 关联
class Relationship:

    def __init__(self):
        self.couple = []

    def make_couple(self,obj1,obj2):
        self.couple = [obj1,obj2]
        print(f'{obj1.name} and {obj2.name} are in love')

    def get_my_partner(self,obj):
            for i in self.couple:
                if i != obj:
                    return i
            else:
                print('you dong have a object')

    def break_up(self):
        print(f'{self.couple[1].name} and {self.couple[0].name} broke up')
        self.couple.clear()


class Person:
    def __init__(self,name,age,sex,relation):
        self.name = name
        self.age = age
        self.sex = sex
        self.relation = relation

    def do_private_stuff(self):
        pass


relation_obj = Relationship()
p1 = Person('eddie',24,'M',relation_obj)
p2 = Person('lily',30,'F',relation_obj)

relation_obj.make_couple(p1,p2)
print(p1.relation.get_my_partner(p1).name)
# p1.relation.break_up()
# p2.relation.get_my_partner(p2)