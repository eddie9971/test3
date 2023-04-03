# Polymorphism 多态

# class Dog():
#     def sound(self):
#         print('wawawa')
#
#
# class Cat():
#     def sound(self):
#         print('miaomiao')
#
#
# def make_sound(animal_obj):
#     animal_obj.sound()
#
#
# d = Dog()
# c = Cat()
# make_sound(d)
# make_sound(c)

class Document:
    def __init__(self,name):
        self.name = name

    def show(self):
        raise NotImplementedError ('Subclass must implement abstract method')


class Pdf(Document):
    def show(self):
        return 'Show pdf contents'


class Word(Document):
    def show(self):
        return 'show word content'


pdf_obj = Pdf('AAA.pdf')
word_obj = Word('BBB.doc')
objs = [pdf_obj, word_obj]

for i in objs:
    print(i.show())


class Car:
    def __init__(self,name):
        self.name = name

    def drive(self):
        raise NotImplementedError('Subclass must implement abstract method')

    def stop(self):
        raise NotImplementedError('Subclass must implement abstract method')


class Sportscar(Car):
    def drive(self):
        return 'Sportscar driving'

    def stop(self):
        return 'Sportscar stopped'


class Truck(Car):
    def drive(self):
        return 'Truck driving slowly'

    def stop(self):
        return 'Truck Stopped'


cars = [
    Truck('AAA'),
    Truck('BBB'),
    Sportscar('CCC'),
    Sportscar('DDD')
]

for car in cars:
    print(f'{car.name}, {car.drive()}')