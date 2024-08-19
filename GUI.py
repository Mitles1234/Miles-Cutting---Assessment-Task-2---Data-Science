#--- Imports ---
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.figure import Figure 
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from tkinter import *
import tkinter as tk
from tkinter import ttk

#--- Variables ---

Location = 'Unknown'

#- Albury -
Albury = False
AlburyWindSpeed = False
AlburyGustSpeed = False
AlburyBuildings = False

#- CoffsHarbour -
CoffsHarbour = False
CoffsHarbourWindSpeed = False
CoffsHarbourGustSpeed = False
CoffsHarbourBuildings = False

#- NewCastle -
NewCastle = False
NewCastleWindSpeed = False
NewCastleGustSpeed = False
NewCastleBuildings = False

#- Penrith -
Penrith = False
PenrithWindSpeed = False
PenrithGustSpeed = False
PenrithBuildings = False

#- Settings -
DarkMode = False
ChartColour1 = 'red'
ChartColour2 = 'blue'
ChartColour3 = 'yellow'

#--- Data Frames ---


#--- Plotting Graphs ---
print('''
def Graph():
      
    
    if Albury == True:
        if AlburyWindSpeed == True:
            plt.plot(
                        WindSpeed_Albury_Weather_df['Date'],
                        WindSpeed_Albury_Weather_df['WindSpeed3pm'],
                        color=ChartColour1,
                        alpha=0.3,
                        label = 'Wind Speed'
            )
        elif AlburyGustSpeed == True:
            plt.plot(
                        Gusts_Albury_Weather_df['Date'],
                        Gusts_Albury_Weather_df['WindGustSpeed'],
                        color=ChartColour2,
                        alpha=0.3,
                        label = 'Gust Speed'
            )
        elif AlburyBuildings == True:
            plt.plot(
                        ???_df['Year'],
                        ???_df['WindSpeed3pm'],
                        color=ChartColour3,
                        alpha=0.3,
                        label = 'Qty of Buildings'
            )
    
    if CoffsHarbour == True:
        if CoffsHarbourWindSpeed == True:
            plt.plot(
                        WindSpeed_CoffsHarbour_Weather_df['Date'],
                        WindSpeed_CoffsHarbour_Weather_df['WindSpeed3pm'],
                        color=ChartColour1,
                        alpha=0.3,
                        label = 'Wind Speed'
            )
        elif CoffsHarbourGustSpeed == True:
            plt.plot(
                        Gusts_CoffsHarbour_Weather_df['Date'],
                        Gusts_CoffsHarbour_Weather_df['WindGustSpeed'],
                        color=ChartColour2,
                        alpha=0.3,
                        label = 'Gust Speed'
            )
        elif CoffsHarbourBuildings == True:
            plt.plot(
                        ???_df['Year'],
                        ???_df['WindSpeed3pm'],
                        color=ChartColour3,
                        alpha=0.3,
                        label = 'Qty of Buildings'
            )

    if NewCastle == True:
        if NewCastleWindSpeed == True:
            plt.plot(
                        WindSpeed_NewCastle_Weather_df['Date'],
                        WindSpeed_NewCastle_Weather_df['WindSpeed3pm'],
                        color=ChartColour1,
                        alpha=0.3,
                        label = 'Wind Speed'
            )
        elif NewCastleGustSpeed == True:
            plt.plot(
                        Gusts_NewCastle_Weather_df['Date'],
                        Gusts_NewCastle_Weather_df['WindGustSpeed'],
                        color=ChartColour2,
                        alpha=0.3,
                        label = 'Gust Speed'
            )
        elif NewCastleBuildings == True:
            plt.plot(
                        ???_df['Year'],
                        ???_df['WindSpeed3pm'],
                        color=ChartColour3,
                        alpha=0.3,
                        label = 'Qty of Buildings'
            )
      
    if Penrith == True:
        if PenrithWindSpeed == True:
            plt.plot(
                        WindSpeed_Penrith_Weather_df['Date'],
                        WindSpeed_Penrith_Weather_df['WindSpeed3pm'],
                        color=ChartColour1,
                        alpha=0.3,
                        label = 'Wind Speed'
            )
        elif PenrithGustSpeed == True:
            plt.plot(
                        Gusts_Penrith_Weather_df['Date'],
                        Gusts_Penrith_Weather_df['WindGustSpeed'],
                        color=ChartColour2,
                        alpha=0.3,
                        label = 'Gust Speed'
            )
        elif PenrithBuildings == True:
            plt.plot(
                        ???_df['Year'],
                        ???_df['WindSpeed3pm'],
                        color=ChartColour3,
                        alpha=0.3,
                        label = 'Qty of Buildings'
            )
      
    else:
      print('Error 404')

    plt.legend()
    if Albury == True:
        Location = 'Albury'
    elif CoffsHarbour == True:
        Location = 'Coffs Harbour'
    elif NewCastle == True:
        Location = 'Newcastle'
      elif Penrith == True:
        Location = 'Penrith'
    plt.title(f'Wind Speed vs Gust Speed in {Location}')
      

    fig = Figure(figsize = (5, 5), 
                 dpi = 100) 
    
    canvas = FigureCanvasTkAgg(fig, 
                               master = Home)   
    canvas.draw() 
  
    canvas.get_tk_widget().place(x=50, y=50) 
''')
# --- GUI ---
top = Tk()
top.geometry('600x400')
top.title('Affect of Buildings on Windspeed')

notebook = ttk.Notebook(top)
notebook.pack(pady=15, expand=True)

# create frames
frame1 = ttk.Frame(notebook, width=1920, height=1080)
frame2 = ttk.Frame(notebook, width=1920, height=1080)
frame3 = ttk.Frame(notebook, width=1920, height=1080)
frame4 = ttk.Frame(notebook, width=1920, height=1080)

frame1.pack(fill='both', expand=True)
frame2.pack(fill='both', expand=True)
frame3.pack(fill='both', expand=True)
frame4.pack(fill='both', expand=True)


# add frames to notebook

notebook.add(frame1, text='Home')
notebook.add(frame2, text='Settings')
notebook.add(frame3, text='Live Weather Data')
notebook.add(frame4, text='Help')

def Plot():
    fig = Figure(figsize = (5, 5), 
                 dpi = 100) 
    
def Home():
    print()
    

def Settings():
    #--- Globalise Variables ---
    global ChartColour1, ChartColour2, ChartColour3, DarkMode

    #--- Creating UI Elements ---
    #- Chart Colour 1 -
    ChartColour1Red = Radiobutton(frame2, text="Red", variable=ChartColour1, value='red')
    ChartColour1Yellow = Radiobutton(frame2, text="Yellow", variable=ChartColour1, value='yellow')
    ChartColour1Green = Radiobutton(frame2, text="Green", variable=ChartColour1, value='green')
    ChartColour1Cyan = Radiobutton(frame2, text="Cyan", variable=ChartColour1, value='cyan')
    ChartColour1Blue = Radiobutton(frame2, text="Blue", variable=ChartColour1, value='blue')
    ChartColour1Magenta = Radiobutton(frame2, text="Magenta", variable=ChartColour1, value='magenta')
    ChartColour1Black = Radiobutton(frame2, text="Black", variable=ChartColour1, value='black')

    #- Chart Colour 2 -
    ChartColour2Red = Radiobutton(frame2, text="Red", variable=ChartColour2, value='red')
    ChartColour2Yellow = Radiobutton(frame2, text="Yellow", variable=ChartColour2, value='yellow')
    ChartColour2Green = Radiobutton(frame2, text="Green", variable=ChartColour2, value='green')
    ChartColour2Cyan = Radiobutton(frame2, text="Cyan", variable=ChartColour2, value='cyan')
    ChartColour2Blue = Radiobutton(frame2, text="Blue", variable=ChartColour2, value='blue')
    ChartColour2Magenta = Radiobutton(frame2, text="Magenta", variable=ChartColour2, value='magenta')
    ChartColour2Black = Radiobutton(frame2, text="Black", variable=ChartColour2, value='black')

    #- Chart Colour 3 -
    ChartColour3Red = Radiobutton(frame2, text="Red", variable=ChartColour3, value='red')
    ChartColour3Yellow = Radiobutton(frame2, text="Yellow", variable=ChartColour3, value='yellow')
    ChartColour3Green = Radiobutton(frame2, text="Green", variable=ChartColour3, value='green')
    ChartColour3Cyan = Radiobutton(frame2, text="Cyan", variable=ChartColour3, value='cyan')
    ChartColour3Blue = Radiobutton(frame2, text="Blue", variable=ChartColour3, value='blue')
    ChartColour3Magenta = Radiobutton(frame2, text="Magenta", variable=ChartColour3, value='magenta')
    ChartColour3Black = Radiobutton(frame2, text="Black", variable=ChartColour3, value='black')

    #- Dark Mode -
    DarkMode = Checkbutton(frame2, text = "Dark Mode", font=("Helvetica", 10, "bold"), variable = DarkMode,
    width = 20, )

    #--- Printing UI Elements ---
    tk.Label(frame2, text='Chart Colour: 1', font=("Helvetica", 10, "bold")).place(x=50, y=25)
    ChartColour1Red.place(x=50, y=50)
    ChartColour1Yellow.place(x=50, y=75)
    ChartColour1Green.place(x=50, y=100)
    ChartColour1Cyan.place(x=50, y=125)
    ChartColour1Blue.place(x=50, y=150)
    ChartColour1Magenta.place(x=50, y=175)
    ChartColour1Black.place(x=50, y=200)

    tk.Label(frame2, text='Chart Colour: 2', font=("Helvetica", 10, "bold")).place(x=50, y=250)
    ChartColour2Red.place(x=50, y=275)
    ChartColour2Yellow.place(x=50, y=300)
    ChartColour2Green.place(x=50, y=325)
    ChartColour2Cyan.place(x=50, y=350)
    ChartColour2Blue.place(x=50, y=375)
    ChartColour2Magenta.place(x=50, y=400)
    ChartColour2Black.place(x=50, y=425)

    tk.Label(frame2, text='Chart Colour: 3', font=("Helvetica", 10, "bold")).place(x=50, y=475)
    ChartColour3Red.place(x=50, y=500)
    ChartColour3Yellow.place(x=50, y=525)
    ChartColour3Green.place(x=50, y=550)
    ChartColour3Cyan.place(x=50, y=575)
    ChartColour3Blue.place(x=50, y=600)
    ChartColour3Magenta.place(x=50, y=625)
    ChartColour3Black.place(x=50, y=650)

    DarkMode.place(x=0, y=700)

Settings()

top.mainloop()