from random import randint

class Die:
    '''Simulate roll the die'''
    def __init__(self, sides=6):
        self.sides = sides
    
    def roll_die(self):
        print('Die' + str(self.sides) + ':', randint(1, self.sides))

die6 = Die()
for i in range(10):
    die6.roll_die()

die10 = Die(10)
for i in range(10):
    die10.roll_die()