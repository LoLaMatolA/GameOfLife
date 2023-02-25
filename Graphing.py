
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

class Grid:
    #Constants

    def __init__(self,on_colour=255,off_colour=0,size=10,speed=20,toroidal_boundary=1):
        self.ON=on_colour
        self.OFF=off_colour
        self.SIZE=size
        self.SPEED=speed 
        if toroidal_boundary==0:
            self.TOROIDAL_BOUNDARY=False
        else:
            self.TOROIDAL_BOUNDARY=True
        #creating the grid using the numpy full function, I initially just make a 2d matrix with every cell having a value OFF
        self.graph=np.full((self.SIZE,self.SIZE),self.OFF)


    #function for generating a random grid. The first [] contains the values that will be in the output. Second is size.
    #third is the probability associated with each element in the first[], i.e, the probability of occurrence of each element in the returned array
    #.reshape() does what it's name suggests. It reshapes the 1d array to a SIZE*SIZE shape
    def randomGrid(self,prob_ON,prob_OFF):
        self.graph[:]=np.random.choice([self.ON,self.OFF],self.SIZE*self.SIZE,p=[prob_ON,prob_OFF]).reshape(self.SIZE,self.SIZE)

    #takes a cell and return a list of it's adjacent row and columns
    def get_Adjacent_Cells(self,i,j):
        SIZE=self.SIZE
        if i==0:
            list_of_rows=[SIZE-1,0,1]
        elif i==SIZE-1:
            list_of_rows=[SIZE-2,SIZE-1,0]
        else:
            list_of_rows=[i-1,i,i+1]
        
        if j==0:
            list_of_columns=[SIZE-1,0,1]
        elif j==SIZE-1:
            list_of_columns=[SIZE-2,SIZE-1,0]
        else:
            list_of_columns=[j-1,j,j+1]

        return list_of_rows,list_of_columns

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



    #function to get number of neighbours(alive/ON cells)
    def getNeighbours(self,graph,i,j):
        if graph[i][j]==self.ON:
            c=-1
        else:
            c=0

        list_of_rows,list_of_columns=self.get_Adjacent_Cells(i,j)
            
        for m in list_of_rows:
            for n in list_of_columns:
                if graph[m][n]==self.ON:
                    c+=1
        
        return c

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


    #updating
    #fn is a discarded variable
    #A new graph is made in each iteration and is changed according to the cells in the graph of previous iteration/generation
    def updateGrid(self,fn,img,graph):
        temp_graph=np.full((self.SIZE,self.SIZE),self.OFF)
        if self.TOROIDAL_BOUNDARY==1:
            for m in range(0,self.SIZE):
                for n in range(0,self.SIZE):
                    temp_graph[m][n]=self.decideState(graph[m][n],self.getNeighbours(graph,m,n))
        else:
            deciding_graph=np.pad(graph,(1,),'constant',constant_values=(self.OFF,self.OFF))
            for m in range(0,self.SIZE):
                for n in range(0,self.SIZE):
                    temp_graph[m][n]=self.decideState(deciding_graph[m+1][n+1],self.getNeighbours(deciding_graph,m+1,n+1))
        
        
        img.set_data(temp_graph)
        graph[:]=temp_graph[:]
        return img
        

    def animate(self):
        fig, ax = plt.subplots()
        img = ax.imshow(self.graph)
        anim = animation.FuncAnimation(fig,self.updateGrid,fargs=(img,self.graph),frames=100,interval=self.SPEED)
        plt.show()

if __name__=='__main__':
    rid=Grid()    
    #rid.randomGrid(0.4,0.6)
    rid.addGlider(0,0)
    rid.animate()