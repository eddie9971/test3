# Multiple Inheritance
class ShenXian:
    def fly(self):
        print('can fly')

    def fight(self):
        print('shenxian fighting')


class Monkey:
    def eat_peach(self):
        print('monkeys like eat peach')

    def fight(self):
        print('monkey fighting')


class MonkeyKing(ShenXian,Monkey):
    def play_stick(self):
        print('Money can play stick')


m = MonkeyKing()
m.fly()
m.eat_peach()
m.play_stick()
m.fight() #按顺序从左到右继承