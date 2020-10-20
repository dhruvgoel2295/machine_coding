import random

class Dice(object):
    def __init__(self, low=1, high=6):
        self.low = low
        self.high = high

    def roll(self):
        return random.randint(self.low, self.high)
