# Inheritance
class Animal:
    type = 'mammal'

    def __init__(self,name,age,sex):
        self.name = name
        self.age = age
        self.sex = sex

    def eat(self):
        print(f'{self.name} is eating')


class Person(Animal):
    type = 'high level mammal'

    def __init__(self, name, age, sex, hobby):
        super().__init__(name, age, sex)
        self.hobby = hobby

    def talk(self):
        print(f'{self.name} is talking')

    def eat(self):
        # Animal.eat(self)
        super().eat() #run parent class method
        print('eating')


class Dog(Animal):
    def chase(self):
        print('Dog is chasing')


p = Person('eddie', 22, 'm', 'music')
p.eat()
p.talk()
print(p.name, p.hobby)

# d = Dog('jack', 3, 'F')
# d.eat()
# print(d.type)
# d.chase()