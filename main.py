#--- Imports ---
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.mplot3d import Axes3D

#----Global Variables----#
quit = False

#----Setup dataframe and query it here prior to creating visualisation and UI functions----#
Weather_df = pd.read_csv('data/Weather.csv')

#--- Albury ---
Albury_Weather_df = Weather_df[Weather_df.Location == 'Albury']

#--- Gusts ---
Gusts_Albury_Weather_df = Albury_Weather_df[['Date', 'WindGustSpeed']]

#--- Wind Speed ---
WindSpeed_Albury_Weather_df = Albury_Weather_df[['Date', 'WindSpeed3pm']]

#print(WindSpeed_Albury_Weather_df)

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

