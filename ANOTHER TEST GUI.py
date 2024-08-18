from tkinter import *
import tkinter as tk
from threading import Thread

#--- GUI Stuff I kinda Understand ---
top = Tk()
top.geometry('600x400')
#--- Settings ---
DarkMode = False
ChartColour1Colour = 'Red'



def donothing():
   filewin = Toplevel(top)
   button = Button(filewin, text="Do nothing button")
   button.pack()

#--- Menu Bar ---
menubar = Menu(top)
filemenu = Menu(menubar, tearoff=0)
filemenu.add_command(label="New", command=donothing)
filemenu.add_command(label="Open", command=donothing)
filemenu.add_command(label="Save", command=donothing)
filemenu.add_command(label="Save as...", command=donothing)
filemenu.add_command(label="Close", command=donothing)

filemenu.add_separator()
filemenu.add_command(label="Exit", command=top.quit)
menubar.add_cascade(label="File", menu=filemenu)
editmenu = Menu(menubar, tearoff=0)
editmenu.add_command(label="Undo", command=donothing)
editmenu.add_separator()
editmenu.add_command(label="Cut", command=donothing)
editmenu.add_command(label="Copy", command=donothing)
editmenu.add_command(label="Paste", command=donothing)
editmenu.add_command(label="Delete", command=donothing)
editmenu.add_command(label="Select All", command=donothing)

menubar.add_cascade(label="Edit", menu=editmenu)
helpmenu = Menu(menubar, tearoff=0)
helpmenu.add_command(label="Help Index", command=donothing)
helpmenu.add_command(label="About...", command=donothing)
menubar.add_cascade(label="Help", menu=helpmenu)

top.config(menu=menubar)

#--- Menu ---
ChartColour1 = Listbox(top)
ChartColour1.insert(1, "Red")
ChartColour1.insert(2, "Yellow")
ChartColour1.insert(3, "Green")
ChartColour1.insert(4, "Cyan")
ChartColour1.insert(5, "Blue")
ChartColour1.insert(6, "Magenta")
ChartColour1.insert(6, "Black")

var = IntVar()
R1 = Radiobutton(top, text="Red", variable=ChartColour1Colour, value='Red')
R1.pack( anchor = W )
R2 = Radiobutton(top, text="Yellow", variable=ChartColour1Colour, value='Yellow')
R2.pack( anchor = W )
R3 = Radiobutton(top, text="Green", variable=ChartColour1Colour, value='Green')
R3.pack( anchor = W)
label = Label(top)


DarkMode = Checkbutton(top, text = "Dark Mode", variable = DarkMode,  \
   onvalue = 1, offvalue = 0, height=5,\
   width = 20, )

#--- Text ---


  Text()

def main():
    #--- Gui Order ---
    DarkMode.pack()
    ChartColour1Text.pack()
    ChartColour1.pack()
    label.pack()


    #--- Run GUI ---
    top.mainloop()