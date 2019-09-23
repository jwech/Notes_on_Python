from random import randint

class Die:
    '''Die class represent die'''
    
    def __init__(self, num_sides=6):
        self.num_sides = 6
    
    def roll_die(self):
        return randint(1, self.num_sides)