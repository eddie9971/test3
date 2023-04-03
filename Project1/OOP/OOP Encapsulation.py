# Encapsulation

class Person(object):
    def __init__(self,name,age):
        self.name = name
        self.age = age
        self.__life_val = 100 #private attribute

    def get_life_val(self):
        print(f'life is {self.__life_val}')
        return self.__life_val

    # private method

    def __breath(self):
        print('breathing')

    def got_attack(self):
        self.__life_val -= 20
        return self.__life_val


a = Person('Eddie', 22)
a.get_life_val()
a.got_attack()
a.get_life_val()

# a._Person__breath() #强行访问private method
# a._Person__life_val = 10 #change private attribute
# a.get_life_val()

