import random


class AI:

    def __init__(self):
        self.num_hit = 0
        self.tried_positions = set()

    def make_move(self):
        """
        Randomly select a square to hit
        :return:
        """
        done = False

        while not done:
            spot = (random.randint(0, 9), random.randint(0, 9))
            if spot not in self.tried_positions:
                self.tried_positions.add(spot)
                done = True

        return spot

