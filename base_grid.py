import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

class BaseGrid:
    #Constants

    def __init__(self,size=10,speed=20,toroidal_boundary=1):
        self.SIZE=size
        self.SPEED=speed 
        if toroidal_boundary==0:
            self.TOROIDAL_BOUNDARY=False
        else:
            self.TOROIDAL_BOUNDARY=True
        #creating the grid using the numpy full function, I initially just make a 2d matrix with every cell having a value OFF
        self.graph=np.full((self.SIZE,self.SIZE),0)


    #function for generating a random grid. The first [] contains the values that will be in the output. Second is size.
    #third is the probability associated with each element in the first[], i.e, the probability of occurrence of each element in the returned array
    #.reshape() does what it's name suggests. It reshapes the 1d array to a SIZE*SIZE shape
    def randomGrid(self,states,prob):
        self.graph[:]=np.random.choice(states,self.SIZE*self.SIZE,p=prob).reshape(self.SIZE,self.SIZE)

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


    #function to get number of neighbours(alive/ON cells)
    def getNeighbours(self,graph,i,j):
        c=0
        list_of_rows,list_of_columns=self.get_Adjacent_Cells(i,j)
            
        for m in list_of_rows:
            for n in list_of_columns:
                if (m,n) != (i,j):
                    if graph[m][n]==self.neighbour_condition:
                        c+=1
        
        return c

    


    #updating
    #fn is a discarded variable
    #A new graph is made in each iteration and is changed according to the cells in the graph of previous iteration/generation
    def decideState(self,fn,img,graph):
        raise NotImplementedError("Yo subclasses must implement updateGrid.")
        
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
    
    
