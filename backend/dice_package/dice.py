from random import randint

class RollableDie:
    def __init__(self, sides=6):
        self.sides = sides

    def roll(self):
        return randint(1, self.sides)


def create_dice_from_sides(sides):
    return list(map(lambda side: RollableDie(side), sides))


class DiceBag:
    def __init__(self, dice_sides=[]):
        self.dice = create_dice_from_sides(dice_sides)

    def roll_bag(self):
        return list(map(lambda dice: dice.roll(), self.dice))
