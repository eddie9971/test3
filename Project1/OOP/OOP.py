

class Dog:
    role = 'dog'

    def __init__(self,name,breed,attack_val,master):
        self.name = name
        self.breed = breed
        self.attack_val = attack_val
        self.life_val = 100
        self.master = master
        self.sayhi()

    def sayhi(self):
        print(f'Hi, I\'m {self.name}, my master is {self.master.name}')

    def bite(self,person):
        person.life_val -= self.attack_val
        print(f'Dog {self.name} bite {person.name}, human lost blood {self.attack_val}, still have {person.life_val}')
        if person.life_val < 30:
            print(f'{person.name} is in danger')


class Weapon:
    def dog_stick(self,obj):
        self.name = 'dog stick'
        self.attack_val = 40
        obj.life_val -=self.attack_val
        self.print_log(obj)

    def knife(self,obj):
        self.name = 'knife'
        self.attack_val = 80
        obj.life_val -=self.attack_val
        self.print_log(obj)

    def gun(self, obj):
        self.name = 'gun'
        self.attack_val = 100
        obj.life_val -= self.attack_val
        self.print_log(obj)

    def print_log(self,obj):
        print(f'{obj.name} was attacked by {self.name}, lost {self.attack_val} blood, still have {obj.life_val}')


class Person:
    role = 'person'

    def __init__(self,name,sex,attack_val):
        self.name = name
        self.sex = sex
        # self.attack_val = attack_val
        self.life_val = 100
        self.weapon = Weapon()

    def attack(self,dog):
        dog.life_val -= self.attack_val
        print(f'Human {self.name} attacks dog {dog.name}, dog lost blood {self.attack_val}, still have {dog.life_val}')
        if dog.life_val < 30:
            print(f'{dog.name} is in danger')

    def walk_dog(self,dog_obj):
        print(f'Master {self.name} brings {dog_obj.name} for a walk.')


# p1 = Person('Eddie', 'M', 85)
# d1 = Dog('ABC', 'AAA', 80, p1)
#
# d1.bite(p1)
# p1.attack(d1)
p = Person('Eddie', 'M', 50)
d = Dog('aaa','bbb', 30,p)

d.bite(p)
p.weapon.gun(d)