from itertools import starmap
from tkinter import *
from tkinter import ttk
from Graphing import *


#Every tkinter window has a root window which is our drawing board/canvas
#cv in this program for control variable
root=Tk()
root.title("GameOfLife")
alive_image=PhotoImage(file=r"C:\Users\91907\Desktop\Game-Dev\Sprites\GameOfLife_Alive.png")
root.iconphoto(False,alive_image)

#Control variables
toroidal_boundary_cv=IntVar()
size_cv=IntVar()
listbox_cv=StringVar()
listbox_cv.set('Random Glider')
speed_cv=IntVar()

#mainframe
mainframe=ttk.Frame(root)
mainframe['padding']=(5, 10)
mainframe['borderwidth']=40
mainframe['relief']='ridge'

#First image
image1=ttk.Label(mainframe)
image1['image']=alive_image

#Label to diplay "Size"
size_display_label=Label(mainframe,text="Size of the grid:")

#input field for SIZE
input_size=Entry(mainframe,textvariable=size_cv)

#Second Image
image2=Label(mainframe)
image2['image']=alive_image

#Checkbutton for toroidal boundary
toroidal_boundary_checkbox=Checkbutton(mainframe,activeforeground='green',variable=toroidal_boundary_cv,text="Toroidal Boundary")

#Listbox for the type of grid (As in the initial pattern)
grid_pattern_listbox=Listbox(mainframe,listvariable=listbox_cv,height=2)



#Speed Scale
speed_scale=Scale(mainframe,orient=HORIZONTAL,from_=500, to=5,variable=speed_cv)

def call_Graphing():
    graph=Grid(255,0,size_cv.get(),speed_cv.get(),toroidal_boundary_cv.get())
    xy=grid_pattern_listbox.curselection()
    for x in xy:
        if x==0:
            graph.randomGrid(0.4,0.6)
        else:
            graph.addGlider(0,0)
    graph.animate()
#START Button
start_button=Button(mainframe,text='START',command=call_Graphing)


#putting it on the screen
mainframe.grid(column=0,row=0,sticky=(N,S,E,W))
image1.grid(column=0,row=0)
size_display_label.grid(column=1,row=0)
image2.grid(column=3,row=0)
input_size.grid(column=2,row=0)
toroidal_boundary_checkbox.grid(column=1,row=1)
grid_pattern_listbox.grid(column=1,row=2)
speed_scale.grid(row=3,column=1)
start_button.grid(row=4,column=1)
#Resizing
root.columnconfigure(0,weight=1)
root.rowconfigure(0,weight=1)
mainframe.columnconfigure(0,weight=2)
mainframe.columnconfigure(1,weight=1)

mainframe.columnconfigure(2,weight=2)
mainframe.rowconfigure(0,weight=1)
root.mainloop()



