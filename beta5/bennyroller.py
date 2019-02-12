import random

class dice2:
    def __init__(self, numSides):
        self.numSides = numSides
        def rollDice(self):
            return random.randint(1,self.numSides)
        dice = dice2(6)
        print(dice)
        input()
