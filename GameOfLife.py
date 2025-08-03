import matplotlib.pyplot as plt
import matplotlib.animation as animation
from base_grid import BaseGrid
import numpy as np

class GameOfLife(BaseGrid):
    #Constants

    def __init__(self,on_colour=255,off_colour=0,size=10,speed=20,toroidal_boundary=1):
        super().__init__(size, speed, toroidal_boundary)
        self.ON=on_colour
        self.OFF=off_colour
        self.SIZE=size
        self.SPEED=speed 
        self.neighbour_condition=self.ON
        if toroidal_boundary==0:
            self.TOROIDAL_BOUNDARY=False
        else:
            self.TOROIDAL_BOUNDARY=True
        self.states=[self.ON, self.OFF]
        # #creating the grid using the numpy full function, I initially just make a 2d matrix with every cell having a value OFF
        # self.graph=np.full((self.SIZE,self.SIZE),self.OFF)


    

    #adding a glider. lor=list of rows; loc=list of colummns
    #--0
    #0-0
    #-00
    #makes this stage of the glider
    def addGlider(self,i,j):
        lor,loc=self.get_Adjacent_Cells(i,j)
        self.graph[lor[0]][loc[2]]=self.ON
        self.graph[lor[1]][loc[0]]=self.ON
        self.graph[lor[1]][loc[2]]=self.ON
        self.graph[lor[2]][loc[1]]=self.ON
        self.graph[lor[2]][loc[2]]=self.ON



   

    #function to decide the state of a cell for the next iteration
    #non=number of neighbours(Alive/ON cells)
    #rules of game of life state:-
    #Any live cell with fewer than two live neighbours dies.
    #Any live cell with two or three live neighbours lives on to the next generation.
    #Any live cell with more than three live neighbours dies.
    #Any dead cell with exactly three live neighbours becomes a live cell.
    def decideState(self,curr_state,non):
        if curr_state==self.ON:
            if non<2 or non>3:
                return self.OFF
            else:
                return self.ON
        if curr_state==self.OFF:
            if non==3:
                return self.ON
            else:
                return self.OFF


   
    

if __name__=='__main__':
    rid=GameOfLife()    
    rid.randomGrid(rid.states,[0.4,0.6])
    rid.addGlider(0,0)
    rid.animate()