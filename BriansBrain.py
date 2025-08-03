import matplotlib.pyplot as plt
import matplotlib.animation as animation
from base_grid import BaseGrid
import numpy as np

class BriansBrain(BaseGrid):
    def __init__(self, off_colour=0, head_colour=255, tail_colour=128, size=10, speed=20, toroidal_boundary=1):
        super().__init__(size, speed, toroidal_boundary)  # call base init to set up grid, etc.
        self.OFF = off_colour
        self.HEAD = head_colour
        self.TAIL = tail_colour
        self.neighbour_condition=self.HEAD
        self.states = [self.OFF, self.HEAD, self.TAIL]
        # self.graph = np.full((self.SIZE, self.SIZE), self.OFF)  # initialize grid with OFF cells

    def decideState(self, curr_state, neighbour_count):
        if curr_state == self.OFF:
            return self.HEAD if neighbour_count == 2 else self.OFF
        elif curr_state == self.HEAD:
            return self.TAIL
        elif curr_state == self.TAIL:
            return self.OFF
        
if __name__=='__main__':
    rid=BriansBrain(size=30,speed=20)    
    rid.randomGrid(rid.states,[0.4,0.3,0.3])
    rid.animate()