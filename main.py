#--- Imports ---
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.figure import Figure
import matplotlib
matplotlib.use("TkAgg") 
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg, NavigationToolbar2Tk)
from tkinter import *
import tkinter as tk
from tkinter import ttk
import requests


#--- GUI Setup ---
top = Tk()
top.geometry('600x400')
top.title('Affect of Buildings on Windspeed')

#--- Variables ---
Error = False
#- Location -
Location = 'No Location'
ChoiceLocation = StringVar(value='Albury')

#- Graphing Variables -
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
ChoiceChartColour1 = StringVar(value='red')
ChoiceChartColour2 = StringVar(value='yellow')
ChoiceChartColour3 = StringVar(value='blue')
ChartColour1 = 'red'
ChartColour2 = 'yellow'
ChartColour3 = 'blue'

#--- Data Frames ---
#- Weather -
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
Newcastle_Buildings_df['Total'] = Newcastle_Buildings_df['Total'].str.replace(',','')
Newcastle_Buildings_df['Total'] = Newcastle_Buildings_df['Total'].astype(int)
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
Penrith_Buildings_df['Total'] = Penrith_Buildings_df['Total'].str.replace(',','')
Penrith_Buildings_df['Total'] = Penrith_Buildings_df['Total'].astype(int)
Penrith_Buildings_df.insert(4, 'Complete Total', 0)
Penrith_Buildings_df = Penrith_Buildings_df.iloc[::-1]
Penrith_Buildings_df['Complete Total'] = Penrith_Buildings_df['Total'].cumsum()

notebook = ttk.Notebook(top)
notebook.pack(pady=15, expand=True)

#--- Frames ---
frame1 = ttk.Frame(notebook, width=1920, height=1080)
frame2 = ttk.Frame(notebook, width=1920, height=1080)
frame3 = ttk.Frame(notebook, width=1920, height=1080)

frame1.pack(fill='both', expand=True)
frame2.pack(fill='both', expand=True)
frame3.pack(fill='both', expand=True)

#--- Notebook ---
notebook.add(frame1, text='Home')
notebook.add(frame2, text='Settings')
notebook.add(frame3, text='Live Weather Data')

def Graph():
    global Location, ChoiceChartColour1, ChartColour1, ChoiceChartColour2, ChartColour2, ChoiceChartColour3, ChartColour3, Albury, CoffsHarbour, Newcastle, Penrith, WindSpeed, ChoiceWindSpeed, GustSpeed, ChoiceGustSpeed, Buildings, ChoiceBuildings, fig, canvas
    
    #Setting Up Graph
    fig = Figure(figsize= (6.5, 5), dpi=100)
    fig, ax1 = plt.subplots()
    
    #Sets Location from List into a Format that can be understood better by the rest of the program
    Title = f'{Location}: '

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
    GustSpeed = ChoiceGustSpeed.get()
    Buildings = ChoiceBuildings.get()

    ChartColour1 = ChoiceChartColour1.get()
    ChartColour2 = ChoiceChartColour2.get()
    ChartColour3 = ChoiceChartColour3.get()

    # Adds the selected variables all to the same graph
    if Albury == True:
        if WindSpeed == True:
            ax1.plot(
                        WindSpeed_Albury_Weather_df['Date'],
                        WindSpeed_Albury_Weather_df['WindSpeed3pm'],
                        color=ChartColour1,
                        alpha=0.3,
                        label = 'Wind Speed'
            )
            ax1.set_ylabel('Wind Speed (Km/h)', color='black')
            ax1.tick_params(axis='y', labelcolor='black')
            plt.legend(loc='upper left')
            Title = str(Title) + str(' Wind Speed')

        if GustSpeed == True:
            plt.plot(
                        Gusts_Albury_Weather_df['Date'],
                        Gusts_Albury_Weather_df['WindGustSpeed'],
                        color=ChartColour2,
                        alpha=0.3,
                        label = 'Gust Speed'
            )
            ax1.set_ylabel('Wind Speed (Km/h)', color='black')
            ax1.tick_params(axis='y', labelcolor='black')
            plt.legend(loc='upper left')
            Title = str(Title) + str(' Gust Speed')

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
            plt.legend(loc='upper right')
            Title = str(Title) + str(' Buildings')

    if CoffsHarbour == True:
        if WindSpeed == True:
            ax1.plot(
                        WindSpeed_CoffsHarbour_Weather_df['Date'],
                        WindSpeed_CoffsHarbour_Weather_df['WindSpeed3pm'],
                        color=ChartColour1,
                        alpha=0.3,
                        label = 'Wind Speed'
            )
            ax1.set_ylabel('Wind Speed (Km/h)', color='black')
            ax1.tick_params(axis='y', labelcolor='black')
            plt.legend(loc='upper left')
            Title = str(Title) + str(' Wind Speed')

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
            plt.legend(loc='upper left')
            Title = str(Title) + str(' Gust Speed')

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
            plt.legend(loc='upper right')
            Title = str(Title) + str(' Buildings')

    if Newcastle == True:
        if WindSpeed == True:
            ax1.plot(
                        WindSpeed_Newcastle_Weather_df['Date'],
                        WindSpeed_Newcastle_Weather_df['WindSpeed3pm'],
                        color=ChartColour1,
                        alpha=0.3,
                        label = 'Wind Speed'
            )
            ax1.set_ylabel('Wind Speed (Km/h)', color='black')
            ax1.tick_params(axis='y', labelcolor='black')
            plt.legend(loc='upper left')
            Title = str(Title) + str(' Wind Speed')

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
            plt.legend(loc='upper left')
            Title = str(Title) + str(' Gust Speed')

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
            plt.legend(loc='upper right')
            Title = str(Title) + str(' Buildings')

    if Penrith == True:
        if WindSpeed == True:
            ax1.plot(
                        WindSpeed_Penrith_Weather_df['Date'],
                        WindSpeed_Penrith_Weather_df['WindSpeed3pm'],
                        color=ChartColour1,
                        alpha=0.3,
                        label = 'Wind Speed'
            )
            ax1.set_ylabel('Wind Speed (Km/h)', color='black')
            ax1.tick_params(axis='y', labelcolor='black')
            plt.legend(loc='upper left')
            Title = str(Title) + str(' Wind Speed')
            
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
            plt.legend(loc='upper left')
            Title = str(Title) + str(' Gust Speed')

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
            plt.legend(loc='upper right')
            Title = str(Title) + str(' Buildings')

    plt.title(Title)

    canvas = FigureCanvasTkAgg(fig, master = frame1)
    canvas.draw()
    canvas.get_tk_widget().place(x=50, y=50)

def Home():
    global Albury, CoffsHarbour, Newcastle, Penrith, Location, Windspeed, Gustspeed, Buildings, fig
    
    Albury = Radiobutton(frame1, text='Albury', variable=ChoiceLocation, value='Albury', cursor="hand2", command=Graph)
    CoffsHarbour = Radiobutton(frame1, text='Coffs Harbour', variable=ChoiceLocation, value='Coffs Harbour', cursor="hand2", command=Graph)
    Newcastle = Radiobutton(frame1, text='Newcastle', variable=ChoiceLocation, value='Newcastle', cursor="hand2", command=Graph)
    Penrith = Radiobutton(frame1, text='Penrith', variable=ChoiceLocation, value='Penrith', cursor="hand2", command=Graph)

    Albury.place(x=750, y=50)
    CoffsHarbour.place(x=750, y=75)
    Newcastle.place(x=750, y=100)
    Penrith.place(x=750, y=125)


    RefreshGraph = tk.Button(frame1, 
                   text="↻ Refresh Graph", 
                   command=Graph,
                   anchor="center",
                   bd=3,
                   cursor="hand2",
                   fg="black",
                   font=("Arial", 12),
                   height=2,
                   justify="center",
                   pady=5,
                   width=15,
                   wraplength=300)
    RefreshGraph.place(x=300, y=600)
        
    WindSpeedCheck = Checkbutton(frame1, text = "Wind Speed", font=("Helvetica", 10, "bold"), 
                                 variable=ChoiceWindSpeed, onvalue=True, offvalue=False, width = 20, anchor='w')
    GustSpeedCheck = Checkbutton(frame1, text = "Gust Speed", font=("Helvetica", 10, "bold"), 
                                 variable=ChoiceGustSpeed, onvalue=True, offvalue=False, width = 20, anchor='w')
    BuildingsCheck = Checkbutton(frame1, text = "Buildings", font=("Helvetica", 10, "bold"), 
                                 variable=ChoiceBuildings, onvalue=True, offvalue=False, width = 20, anchor='w')

    WindSpeedCheck.place(x=750, y=200)
    GustSpeedCheck.place(x=750, y=225)
    BuildingsCheck.place(x=750, y=250)

    toolbar = NavigationToolbar2Tk(canvas, 
                                   frame1)
    
    toolbar.update()

    canvas.get_tk_widget().place(x=50, y=50)

def Settings():
    #--- Globalise Variables ---
    global ChartColour1, ChartColour2, ChartColour3, DarkMode

    #--- Creating UI Elements ---
    #- Chart Colour 1 -
    ChartColour1Red = Radiobutton(frame2, text="Red", variable=ChoiceChartColour1, value='red')
    ChartColour1Yellow = Radiobutton(frame2, text="Yellow", variable=ChoiceChartColour1, value='yellow')
    ChartColour1Green = Radiobutton(frame2, text="Green", variable=ChoiceChartColour1, value='green')
    ChartColour1Cyan = Radiobutton(frame2, text="Cyan", variable=ChoiceChartColour1, value='cyan')
    ChartColour1Blue = Radiobutton(frame2, text="Blue", variable=ChoiceChartColour1, value='blue')
    ChartColour1Magenta = Radiobutton(frame2, text="Magenta", variable=ChoiceChartColour1, value='magenta')
    ChartColour1Black = Radiobutton(frame2, text="Black", variable=ChoiceChartColour1, value='black')

    #- Chart Colour 2 -
    ChartColour2Red = Radiobutton(frame2, text="Red", variable=ChoiceChartColour2, value='red')
    ChartColour2Yellow = Radiobutton(frame2, text="Yellow", variable=ChoiceChartColour2, value='yellow')
    ChartColour2Green = Radiobutton(frame2, text="Green", variable=ChoiceChartColour2, value='green')
    ChartColour2Cyan = Radiobutton(frame2, text="Cyan", variable=ChoiceChartColour2, value='cyan')
    ChartColour2Blue = Radiobutton(frame2, text="Blue", variable=ChoiceChartColour2, value='blue')
    ChartColour2Magenta = Radiobutton(frame2, text="Magenta", variable=ChoiceChartColour2, value='magenta')
    ChartColour2Black = Radiobutton(frame2, text="Black", variable=ChoiceChartColour2, value='black')

    #- Chart Colour 3 -
    ChartColour3Red = Radiobutton(frame2, text="Red", variable=ChoiceChartColour3, value='red')
    ChartColour3Yellow = Radiobutton(frame2, text="Yellow", variable=ChoiceChartColour3, value='yellow')
    ChartColour3Green = Radiobutton(frame2, text="Green", variable=ChoiceChartColour3, value='green')
    ChartColour3Cyan = Radiobutton(frame2, text="Cyan", variable=ChoiceChartColour3, value='cyan')
    ChartColour3Blue = Radiobutton(frame2, text="Blue", variable=ChoiceChartColour3, value='blue')
    ChartColour3Magenta = Radiobutton(frame2, text="Magenta", variable=ChoiceChartColour3, value='magenta')
    ChartColour3Black = Radiobutton(frame2, text="Black", variable=ChoiceChartColour3, value='black')

    #--- Printing UI Elements ---
    tk.Label(frame2, text='Chart Colour: Wind Speed', font=("Helvetica", 10, "bold")).place(x=50, y=25)
    ChartColour1Red.place(x=50, y=50)
    ChartColour1Yellow.place(x=50, y=75)
    ChartColour1Green.place(x=50, y=100)
    ChartColour1Cyan.place(x=50, y=125)
    ChartColour1Blue.place(x=50, y=150)
    ChartColour1Magenta.place(x=50, y=175)
    ChartColour1Black.place(x=50, y=200)

    tk.Label(frame2, text='Chart Colour: Gust Speed', font=("Helvetica", 10, "bold")).place(x=50, y=250)
    ChartColour2Red.place(x=50, y=275)
    ChartColour2Yellow.place(x=50, y=300)
    ChartColour2Green.place(x=50, y=325)
    ChartColour2Cyan.place(x=50, y=350)
    ChartColour2Blue.place(x=50, y=375)
    ChartColour2Magenta.place(x=50, y=400)
    ChartColour2Black.place(x=50, y=425)

    tk.Label(frame2, text='Chart Colour: Buildings', font=("Helvetica", 10, "bold")).place(x=50, y=475)
    ChartColour3Red.place(x=50, y=500)
    ChartColour3Yellow.place(x=50, y=525)
    ChartColour3Green.place(x=50, y=550)
    ChartColour3Cyan.place(x=50, y=575)
    ChartColour3Blue.place(x=50, y=600)
    ChartColour3Magenta.place(x=50, y=625)
    ChartColour3Black.place(x=50, y=650)

def LiveWeather():
      
    
    def printInput(): 
        global weather_data, api_key, weather, temp, wind, wind_direction_abr
        api_key = 'a3a62c3dd107f25e273aca6be5877882' 
        location = inputtxt.get(1.0, "end-1c") 
        lbl.config(text = "Location: "+ location) 
        weather_data = requests.get(
        f"https://api.openweathermap.org/data/2.5/weather?q={location}&units=metric&APPID={api_key}"
        )
        def weather():
            global weather, temp, weather_data
            weather = str(weather_data.json()['weather'][0]['main'])
            temp = round(weather_data.json()['main']['temp'])

        def wind():
            global wind, wind_direction_abr, weather_data
            wind = round((weather_data.json()['wind']['speed'] * 1.944))
            wind_direction_deg = weather_data.json()['wind']['deg']
            if wind == 0:
                wind_direction_abr = 'No Wind'
            elif 0 <= wind_direction_deg <= 22.5 or 337.5 <= wind_direction_deg <= 360:
                wind_direction_abr = 'N'
            elif 22.5 <= wind_direction_deg <= 67.5:
                wind_direction_abr = 'NE'
            elif 67.5 <= wind_direction_deg <= 112.5:
                wind_direction_abr = 'E'
            elif 112.5 <= wind_direction_deg <= 157.5:
                wind_direction_abr = 'SE'
            elif 157.5 <= wind_direction_deg <= 202.5:
                wind_direction_abr = 'S'
            elif 202.5 <= wind_direction_deg <= 247.5:
                wind_direction_abr = 'SW'
            elif 247.5 <= wind_direction_deg <= 292.5:
                wind_direction_abr = 'W'
            elif 292.5 <= wind_direction_deg <= 337.5:
                wind_direction_abr = 'NW'
            else:
                wind_direction_abr = 'Error'

        if weather_data.json()['cod'] == '404':
            LocationNotFound = tk.Label(text = "Location Not Found")
            LocationNotFound.place(x=10, y=50)
        else:
            weather()
            wind()

            weatherprint = tk.Label(frame3, text = f"The weather in {location} is: {weather}                                                ")
            tempprint = tk.Label(frame3, text = f"The temperature in {location} is: {temp}ºC                                                ")
            windspeedprint = tk.Label(frame3, text = f"Wind: {wind} Knots                                                                   ")
            winddirectionprint = tk.Label(frame3, text = f"Wind Direction: {wind_direction_abr}                                             ")

            weatherprint.place(x=10, y=50)
            tempprint.place(x=10, y=75)
            windspeedprint.place(x=10, y=100)
            winddirectionprint.place(x=10, y=125)

    # TextBox Creation 
    inputtxt = tk.Text(frame3, 
                    height = 5, 
                    width = 20) 
    
    inputtxt.place(x=10, y=180) 
    
    # Button Creation 
    printButton = tk.Button(frame3, 
                            text = "Print",  
                            command = printInput) 
    printButton.place(x=72.5, y=280) 
    
    # Label Creation 
    lbl = tk.Label(frame3, text = "Enter Location: ") 
    lbl.place(x=10, y=155) 
    frame3.mainloop() 

    

Graph()
Settings()
Home()
LiveWeather()


top.mainloop()