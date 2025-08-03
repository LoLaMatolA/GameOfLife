import matplotlib.pyplot as plt
import matplotlib.animation as animation
from base_grid import BaseGrid
import numpy as np

class HighLife(BaseGrid):
    def __init__(self, on_colour=255, off_colour=0, size=10, speed=20, toroidal_boundary=1):
        super().__init__(size, speed, toroidal_boundary)
        self.ON = on_colour
        self.OFF = off_colour
        self.neighbour_condition=self.ON
        self.states = [self.OFF, self.ON]

    def decideState(self, curr_state, neighbour_count):
        if curr_state == self.ON:
            return self.ON if neighbour_count in [2, 3] else self.OFF
        else:
            return self.ON if neighbour_count in [3, 6] else self.OFF

if __name__ == '__main__':
    rid = HighLife(size=30, speed=20)
    rid.randomGrid(rid.states, [0.5, 0.5])
    rid.animate()
