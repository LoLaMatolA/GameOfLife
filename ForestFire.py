import matplotlib.pyplot as plt
import matplotlib.animation as animation
from base_grid import BaseGrid
import numpy as np
import random

class ForestFire(BaseGrid):
    def __init__(self, empty=0, tree=128, burning=255, size=10, speed=20, toroidal_boundary=1):
        super().__init__(size, speed, toroidal_boundary)
        self.EMPTY = empty
        self.TREE = tree
        self.BURNING = burning
        self.OFF=self.EMPTY
        self.neighbour_condition=self.BURNING
        self.states = [self.EMPTY, self.TREE, self.BURNING]
        self.neighbour_condition = self.BURNING

    def decideState(self, curr_state, non):
        # If tree is burning, it becomes empty
        if curr_state == self.BURNING:
            return self.EMPTY
        
        # If tree is present and at least one neighbor is burning, it starts burning
        elif curr_state == self.TREE:
            if non > 0:
                return self.BURNING
            elif random.random() < 0.001:  # spontaneous ignition
                return self.BURNING
            else:
                return self.TREE

        # If empty, a tree may grow
        elif curr_state == self.EMPTY:
            if random.random() < 0.01:  # spontaneous growth
                return self.TREE
            else:
                return self.EMPTY

if __name__ == '__main__':
    rid = ForestFire(speed=5,size=100)
    rid.randomGrid(rid.states, [0.4,0.3,0.3])
    rid.animate()
