import random

ranges = {
    'd6': (1,6),
    'd12': (1,12),
    'd20': (1,20)
}

dice_size = input("Do you want to roll a d6, d12, or d20? ").lower()
_range = ranges[dice_size]
print(_range)
print(random.randint(_range[0], _range[1]))


class Dice:
    def roll(self):
        first = random.randint(1,6)
        second = random.randint(1, 6)
        return (first,second)

dice = Dice()
print(dice.roll())