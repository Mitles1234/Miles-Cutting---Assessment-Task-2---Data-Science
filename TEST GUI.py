
import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import askyesno

#--- Setting Toggles ---
DarkMode = False
FontSize = 12
ChartColour = 'blue'

# root window
root = tk.Tk()
root.geometry('400x300')
root.title('Notebook Demo')

# create a notebook
notebook = ttk.Notebook(root)
notebook.pack(pady=15, expand=True)

# create frames
frame1 = ttk.Frame(notebook, width=350, height=280)
frame2 = ttk.Frame(notebook, width=350, height=280)

frame1.pack(fill='both', expand=True)
frame2.pack(fill='both', expand=True)

# add frames to notebook

notebook.add(frame1, text='Home')
notebook.add(frame2, text='Settings')

ttk.Button(
    root,
    text='Ask Yes/No',
    command=confirm).pack(expand=True)

root.mainloop()