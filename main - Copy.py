#--- Imports ---
import pandas as pd
import matplotlib.pyplot as plt
matplotlib.use("TkAgg")
import numpy as np
from mpl_toolkits.mplot3d import Axes3D

from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2TkAgg
from matplotlib.figure import Figure

import tkinter as tk
from tkinter import ttk

#--- Global Variables ---
quit = False

#--- Setting Up DataFrames---
#--- Main Weather Dataframe ---
Weather_df = pd.read_csv('data/Weather.csv')

#--- Albury ---
#--- Albury Weather ---
Albury_Weather_df = Weather_df[Weather_df.Location == 'Albury']
#--- Albury Gusts ---
Gusts_Albury_Weather_df = Albury_Weather_df[['Date', 'WindGustSpeed']]
#--- Albury Wind Speed ---
WindSpeed_Albury_Weather_df = Albury_Weather_df[['Date', 'WindSpeed3pm']]
#--- Albury Buildings ---
Albury_Buildings_df = pd.read_csv('data/Albury Buildings.csv', skiprows=2)
Albury_Buildings_df = Albury_Buildings_df.iloc[:-3]

#Albury_Buildings_df.insert(4, 'Complete Total', [Albury_Buildings_df['Total'] + Albury_Buildings_df['Other']], 0)
#Albury_Buildings_df['Complete Total'] = Albury_Buildings_df['Total'] + 
Albury_Buildings_df.sum()

print(Albury_Buildings_df)

'''
plt.plot(
                    Gusts_Albury_Weather_df['Date'],
                    Gusts_Albury_Weather_df['WindGustSpeed'],
                    color='blue',
                    alpha=0.3,
                    label='Gust Wind Speed'
              )

plt.plot(
                    WindSpeed_Albury_Weather_df['Date'],
                    WindSpeed_Albury_Weather_df['WindSpeed3pm'],
                    color='purple',
                    alpha=0.3,
                    label = 'Wind Speed'
              )
plt.legend()
plt.xlabel("Date")
plt.ylabel("Wind Speed (Km/h)")
plt.title('Wind Speed vs Gust Speed in Albury')
plt.tight_layout()
plt.show()

'''