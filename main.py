#--- Imports ---
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.mplot3d import Axes3D

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

