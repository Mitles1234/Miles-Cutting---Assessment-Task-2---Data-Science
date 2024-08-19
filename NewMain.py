#--- Imports ---
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.figure import Figure 
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from tkinter import *
import tkinter as tk
from tkinter import ttk

#--- GUI Setup ---
top = Tk()
top.geometry('600x400')
top.title('Affect of Buildings on Windspeed')

#--- Variables ---
Location = 'No Location'
ChoiceLocation = StringVar()
ChoiceWindSpeed = BooleanVar()
ChoiceGustSpeed = BooleanVar()
ChoiceBuildings = BooleanVar()
WindSpeed = False
GustSpeed = False
Buildings = False

#- Albury -
Albury = False

#- CoffsHarbour -
CoffsHarbour = False

#- Newcastle -
Newcastle = False

#- Penrith -
Penrith = False

#- Settings -
ChoiceChartColour1 = StringVar()
ChoiceChartColour2 = StringVar()
ChoiceChartColour3 = StringVar()
ChartColour1 = 'red'
ChartColour2 = 'blue'
ChartColour3 = 'yellow'

#--- Data Frames ---
Weather_df = pd.read_csv('data/Weather.csv')

#--- Albury ---
#--- Albury Weather ---
Albury_Weather_df = Weather_df[Weather_df.Location == 'Albury']
Albury_Weather_df['Date'] = pd.to_datetime(Albury_Weather_df['Date'])
#--- Albury Gusts ---
Gusts_Albury_Weather_df = Albury_Weather_df[['Date', 'WindGustSpeed']]
#--- Albury Wind Speed ---
WindSpeed_Albury_Weather_df = Albury_Weather_df[['Date', 'WindSpeed3pm']]
#--- Albury Buildings ---
Albury_Buildings_df = pd.read_csv('data/Albury Buildings.csv', skiprows=2)
Albury_Buildings_df = Albury_Buildings_df.iloc[:-10]
Albury_Buildings_df = Albury_Buildings_df.iloc[6:]
Albury_Buildings_df['Year (ending June 30)'] = Albury_Buildings_df['Year (ending June 30)'].str[:4]
Albury_Buildings_df['Year (ending June 30)'] = Albury_Buildings_df['Year (ending June 30)'].astype(str) + str('-06-20')
Albury_Buildings_df['Year (ending June 30)'] = pd.to_datetime(Albury_Buildings_df['Year (ending June 30)'])
Albury_Buildings_df.insert(4, 'Complete Total', 0)
Albury_Buildings_df = Albury_Buildings_df.iloc[::-1]
Albury_Buildings_df['Complete Total'] = Albury_Buildings_df['Total'].cumsum()


#--- CoffsHarbour ---
#--- CoffsHarbour Weather ---
CoffsHarbour_Weather_df = Weather_df[Weather_df.Location == 'CoffsHarbour']
CoffsHarbour_Weather_df['Date'] = pd.to_datetime(CoffsHarbour_Weather_df['Date'])
#--- CoffsHarbour Gusts ---
Gusts_CoffsHarbour_Weather_df = CoffsHarbour_Weather_df[['Date', 'WindGustSpeed']]
#--- CoffsHarbour Wind Speed ---
WindSpeed_CoffsHarbour_Weather_df = CoffsHarbour_Weather_df[['Date', 'WindSpeed3pm']]
#--- CoffsHarbour Buildings ---
CoffsHarbour_Buildings_df = pd.read_csv('data/Coffs Harbour Buildings.csv', skiprows=2)
CoffsHarbour_Buildings_df = CoffsHarbour_Buildings_df.iloc[:-10]
CoffsHarbour_Buildings_df = CoffsHarbour_Buildings_df.iloc[6:]
CoffsHarbour_Buildings_df['Year (ending June 30)'] = CoffsHarbour_Buildings_df['Year (ending June 30)'].str[:4]
CoffsHarbour_Buildings_df['Year (ending June 30)'] = CoffsHarbour_Buildings_df['Year (ending June 30)'].astype(str) + str('-06-20')
CoffsHarbour_Buildings_df['Year (ending June 30)'] = pd.to_datetime(CoffsHarbour_Buildings_df['Year (ending June 30)'])
CoffsHarbour_Buildings_df.insert(4, 'Complete Total', 0)
CoffsHarbour_Buildings_df = CoffsHarbour_Buildings_df.iloc[::-1]
CoffsHarbour_Buildings_df['Complete Total'] = CoffsHarbour_Buildings_df['Total'].cumsum()


#--- Newcastle ---
#--- Newcastle Weather ---
Newcastle_Weather_df = Weather_df[Weather_df.Location == 'Newcastle']
Newcastle_Weather_df['Date'] = pd.to_datetime(Newcastle_Weather_df['Date'])
#--- Newcastle Gusts ---
Gusts_Newcastle_Weather_df = Newcastle_Weather_df[['Date', 'WindGustSpeed']]
#--- Newcastle Wind Speed ---
WindSpeed_Newcastle_Weather_df = Newcastle_Weather_df[['Date', 'WindSpeed3pm']]
#--- Newcastle Buildings ---
Newcastle_Buildings_df = pd.read_csv('data/Newcastle Buildings.csv', skiprows=2)
Newcastle_Buildings_df = Newcastle_Buildings_df.iloc[:-10]
Newcastle_Buildings_df = Newcastle_Buildings_df.iloc[6:]
Newcastle_Buildings_df['Year (ending June 30)'] = Newcastle_Buildings_df['Year (ending June 30)'].str[:4]
Newcastle_Buildings_df['Year (ending June 30)'] = Newcastle_Buildings_df['Year (ending June 30)'].astype(str) + str('-06-20')
Newcastle_Buildings_df['Year (ending June 30)'] = pd.to_datetime(Newcastle_Buildings_df['Year (ending June 30)'])
Newcastle_Buildings_df.insert(4, 'Complete Total', 0)
Newcastle_Buildings_df = Newcastle_Buildings_df.iloc[::-1]
Newcastle_Buildings_df['Complete Total'] = Newcastle_Buildings_df['Total'].cumsum()


#--- Penrith ---
#--- Penrith Weather ---
Penrith_Weather_df = Weather_df[Weather_df.Location == 'Penrith']
Penrith_Weather_df['Date'] = pd.to_datetime(Penrith_Weather_df['Date'])
#--- Penrith Gusts ---
Gusts_Penrith_Weather_df = Penrith_Weather_df[['Date', 'WindGustSpeed']]
#--- Penrith Wind Speed ---
WindSpeed_Penrith_Weather_df = Penrith_Weather_df[['Date', 'WindSpeed3pm']]
#--- Penrith Buildings ---
Penrith_Buildings_df = pd.read_csv('data/Penrith Buildings.csv', skiprows=2)
Penrith_Buildings_df = Penrith_Buildings_df.iloc[:-10]
Penrith_Buildings_df = Penrith_Buildings_df.iloc[6:]
Penrith_Buildings_df['Year (ending June 30)'] = Penrith_Buildings_df['Year (ending June 30)'].str[:4]
Penrith_Buildings_df['Year (ending June 30)'] = Penrith_Buildings_df['Year (ending June 30)'].astype(str) + str('-06-20')
Penrith_Buildings_df['Year (ending June 30)'] = pd.to_datetime(Penrith_Buildings_df['Year (ending June 30)'])
Penrith_Buildings_df.insert(4, 'Complete Total', 0)
Penrith_Buildings_df = Penrith_Buildings_df.iloc[::-1]
Penrith_Buildings_df['Complete Total'] = Penrith_Buildings_df['Total'].cumsum()

notebook = ttk.Notebook(top)
notebook.pack(pady=15, expand=True)

#--- Frames ---
frame1 = ttk.Frame(notebook, width=1920, height=1080)
frame2 = ttk.Frame(notebook, width=1920, height=1080)
frame3 = ttk.Frame(notebook, width=1920, height=1080)
frame4 = ttk.Frame(notebook, width=1920, height=1080)

frame1.pack(fill='both', expand=True)
frame2.pack(fill='both', expand=True)
frame3.pack(fill='both', expand=True)
frame4.pack(fill='both', expand=True)


#--- Notebook ---
notebook.add(frame1, text='Home')
notebook.add(frame2, text='Settings')
notebook.add(frame3, text='Live Weather Data')
notebook.add(frame4, text='Help')

def Graph():
    global Location, ChartColour1, ChartColour2, ChartColour3, Albury, CoffsHarbour, Newcastle, Penrith, WindSpeed, ChoiceWindSpeed, GustSpeed, ChoiceGustSpeed, Buildings, ChoiceBuildings
    
    fig, ax1 = plt.subplots()

    Location = ChoiceLocation.get()

    if Location == 'Albury':
        Albury = True
        CoffsHarbour = False
        Newcastle = False
        Penrith = False
    elif Location == 'Coffs Harbour':
        Albury = False
        CoffsHarbour = True
        Newcastle = False
        Penrith = False
    elif Location == 'Newcastle':
        Albury = False
        CoffsHarbour = False
        Newcastle = True
        Penrith = False
    elif Location == 'Penrith':
        Albury = False
        CoffsHarbour = False
        Newcastle = False
        Penrith = True

    WindSpeed = ChoiceWindSpeed.get()
    GustSpeed = ChoiceWindSpeed.get()
    Buildings = ChoiceBuildings.get()

    if Albury == True:
        if WindSpeed == True:
            ax1.plot(
                        WindSpeed_Albury_Weather_df['Date'],
                        WindSpeed_Albury_Weather_df['WindSpeed3pm'],
                        color=ChartColour1,
                        alpha=0.3,
                        label = 'Wind Speed'
            )
        if GustSpeed == True:
            ax1.plot(
                        Gusts_Albury_Weather_df['Date'],
                        Gusts_Albury_Weather_df['WindGustSpeed'],
                        color=ChartColour2,
                        alpha=0.3,
                        label = 'Gust Speed'
            )
            ax1.set_ylabel('Wind Speed (Km/h)', color='black')
            ax1.tick_params(axis='y', labelcolor='black')

        if Buildings == True:
            ax2 = ax1.twinx()
            ax2.plot(
                        Albury_Buildings_df['Year (ending June 30)'],
                        Albury_Buildings_df['Complete Total'],
                        color=ChartColour3,
                        alpha=0.3,
                        label = 'Qty of Buildings'
            )
            ax2.set_ylabel('Quantity of Buildings', color=ChartColour3)
            ax2.tick_params(axis='y', labelcolor=ChartColour3)

    elif CoffsHarbour == True:
        if WindSpeed == True:
            ax1.plot(
                        WindSpeed_CoffsHarbour_Weather_df['Date'],
                        WindSpeed_CoffsHarbour_Weather_df['WindSpeed3pm'],
                        color=ChartColour1,
                        alpha=0.3,
                        label = 'Wind Speed'
            )
        if GustSpeed == True:
            ax1.plot(
                        Gusts_CoffsHarbour_Weather_df['Date'],
                        Gusts_CoffsHarbour_Weather_df['WindGustSpeed'],
                        color=ChartColour2,
                        alpha=0.3,
                        label = 'Gust Speed'
            )
            ax1.set_ylabel('Wind Speed (Km/h)', color='black')
            ax1.tick_params(axis='y', labelcolor='black')

        if Buildings == True:
            ax2 = ax1.twinx()
            ax2.plot(
                        CoffsHarbour_Buildings_df['Year (ending June 30)'],
                        CoffsHarbour_Buildings_df['Complete Total'],
                        color=ChartColour3,
                        alpha=0.3,
                        label = 'Qty of Buildings'
            )
            ax2.set_ylabel('Quantity of Buildings', color=ChartColour3)
            ax2.tick_params(axis='y', labelcolor=ChartColour3)

    elif Newcastle == True:
        if WindSpeed == True:
            ax1.plot(
                        WindSpeed_Newcastle_Weather_df['Date'],
                        WindSpeed_Newcastle_Weather_df['WindSpeed3pm'],
                        color=ChartColour1,
                        alpha=0.3,
                        label = 'Wind Speed'
            )
        if GustSpeed == True:
            ax1.plot(
                        Gusts_Newcastle_Weather_df['Date'],
                        Gusts_Newcastle_Weather_df['WindGustSpeed'],
                        color=ChartColour2,
                        alpha=0.3,
                        label = 'Gust Speed'
            )
            ax1.set_ylabel('Wind Speed (Km/h)', color='black')
            ax1.tick_params(axis='y', labelcolor='black')

        if Buildings == True:
            ax2 = ax1.twinx()
            ax2.plot(
                        Newcastle_Buildings_df['Year (ending June 30)'],
                        Newcastle_Buildings_df['Complete Total'],
                        color=ChartColour3,
                        alpha=0.3,
                        label = 'Qty of Buildings'
            )
            ax2.set_ylabel('Quantity of Buildings', color=ChartColour3)
            ax2.tick_params(axis='y', labelcolor=ChartColour3)

    elif Penrith == True:
        if WindSpeed == True:
            ax1.plot(
                        WindSpeed_Penrith_Weather_df['Date'],
                        WindSpeed_Penrith_Weather_df['WindSpeed3pm'],
                        color=ChartColour1,
                        alpha=0.3,
                        label = 'Wind Speed'
            )
        if GustSpeed == True:
            ax1.plot(
                        Gusts_Penrith_Weather_df['Date'],
                        Gusts_Penrith_Weather_df['WindGustSpeed'],
                        color=ChartColour2,
                        alpha=0.3,
                        label = 'Gust Speed'
            )
            ax1.set_ylabel('Wind Speed (Km/h)', color='black')
            ax1.tick_params(axis='y', labelcolor='black')

        if Buildings == True:
            ax2 = ax1.twinx()
            ax2.plot(
                        Penrith_Buildings_df['Year (ending June 30)'],
                        Penrith_Buildings_df['Complete Total'],
                        color=ChartColour3,
                        alpha=0.3,
                        label = 'Qty of Buildings'
            )
            ax2.set_ylabel('Quantity of Buildings', color=ChartColour3)
            ax2.tick_params(axis='y', labelcolor=ChartColour3)

    plt.title(f'Wind Speed vs Gust Speed in {Location}')
      

    #fig = Figure(figsize = (5, 5), 
    #             dpi = 100) 
    
    #canvas = FigureCanvasTkAgg(fig, frame1 = Home)   

    #canvas.draw() 
  
    #canvas.get_tk_widget().place(x=50, y=50) 
    plt.show()

def Home():
    global Albury, CoffsHarbour, Newcastle, Penrith, Location, Windspeed, Gustspeed, Buildings
    
    Albury = Radiobutton(frame1, text='Albury', variable=ChoiceLocation, value='Albury', cursor="hand2", command=Graph)
    CoffsHarbour = Radiobutton(frame1, text='Coffs Harbour', variable=ChoiceLocation, value='Coffs Harbour', cursor="hand2", command=Graph)
    Newcastle = Radiobutton(frame1, text='Newcastle', variable=ChoiceLocation, value='Newcastle', cursor="hand2", command=Graph)
    Penrith = Radiobutton(frame1, text='Penrith', variable=ChoiceLocation, value='Penrith', cursor="hand2", command=Graph)

   
    Albury.place(x=700, y=50)
    CoffsHarbour.place(x=700, y=75)
    Newcastle.place(x=700, y=100)
    Penrith.place(x=700, y=125)

    RefreshGraph = tk.Button(frame1, 
                   text="↻ Refresh Graph", 
                   command=Graph,
                   activebackground="blue", 
                   activeforeground="white",
                   anchor="center",
                   bd=3,
                   bg="lightgray",
                   cursor="hand2",
                   fg="black",
                   font=("Arial", 12),
                   height=2,
                   highlightcolor="green",
                   justify="center",
                   pady=5,
                   width=20,
                   wraplength=300)
    
    WindSpeedCheck = Checkbutton(frame1, text = "Wind Speed", font=("Helvetica", 10, "bold"), 
                                 variable=ChoiceWindSpeed, onvalue=True, offvalue=False, width = 20)
    GustSpeedCheck = Checkbutton(frame1, text = "Gust Speed", font=("Helvetica", 10, "bold"), 
                                 variable=ChoiceGustSpeed, onvalue=True, offvalue=False, width = 20)
    BuildingsCheck = Checkbutton(frame1, text = "Buildings", font=("Helvetica", 10, "bold"), 
                                 variable=ChoiceBuildings, onvalue=True, offvalue=False, width = 20)

    WindSpeedCheck.place(x=700, y=200)
    GustSpeedCheck.place(x=700, y=225)
    BuildingsCheck.place(x=700, y=250)

    RefreshGraph.place(x=350, y=700)

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


Settings()
Home()

top.mainloop()