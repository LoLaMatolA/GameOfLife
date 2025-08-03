import matplotlib.pyplot as plt
import matplotlib.animation as animation
from base_grid import BaseGrid
import numpy as np

class Wireworld(BaseGrid):
    def __init__(self, empty=0, head=255, tail=128, conductor=200, size=10, speed=20, toroidal_boundary=1):
        super().__init__(size, speed, toroidal_boundary)
        self.EMPTY = empty
        self.HEAD = head
        self.TAIL = tail
        self.CONDUCTOR = conductor
        self.OFF= self.EMPTY
        self.choices = [self.EMPTY, self.HEAD, self.TAIL, self.CONDUCTOR]
        self.neighbour_condition = self.HEAD

    def decideState(self, curr_state, neighbour_count):
        if curr_state == self.EMPTY:
            return self.EMPTY
        elif curr_state == self.HEAD:
            return self.TAIL
        elif curr_state == self.TAIL:
            return self.CONDUCTOR
        elif curr_state == self.CONDUCTOR:
            return self.HEAD if neighbour_count in [1, 2] else self.CONDUCTOR
    def addWireLoop(self):
        # Square loop coordinates
        loop_coords = [
            (5, 5), (5, 6), (5, 7), (5, 8),
            (6, 8),
            (7, 8), (7, 7), (7, 6), (7, 5),
            (6, 5)
        ]
        
        for i, j in loop_coords:
            self.graph[i][j] = self.CONDUCTOR

        # Add an electron head and tail to start the loop
        self.graph[5][6] = self.HEAD
        self.graph[5][5] = self.TAIL
    def addDoubleLoopWithBridge(self):
        # First square loop (top-left)
        loop1 = [(i, j) for j in range(10, 30) for i in (10, 30)] + [(i, j) for i in range(10, 31) for j in (10, 30)]
        
        # Second square loop (bottom-right)
        loop2 = [(i, j) for j in range(60, 80) for i in (60, 80)] + [(i, j) for i in range(60, 81) for j in (60, 80)]

        # Bridge connecting both loops (a wire)
        bridge = [(i, i) for i in range(31, 60)]

        # Combine all
        for i, j in loop1 + loop2 + bridge:
            self.graph[i][j] = self.CONDUCTOR

        # Initial electron head and tail
        self.graph[10][11] = self.HEAD
        self.graph[10][10] = self.TAIL


if __name__ == '__main__':
    rid = Wireworld(size=100, speed=1)
    # rid.randomGrid(rid.choices, [0.7, 0.1, 0.1, 0.1])
    # rid.addWireLoop()
    rid.addDoubleLoopWithBridge()
    rid.animate()
