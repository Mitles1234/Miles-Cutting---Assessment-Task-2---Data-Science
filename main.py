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

print(Albury_Buildings_df)

#Albury_Buildings_df.insert(4, 'Complete Total', [Albury_Buildings_df['Total'] + ], True)
fig, ax1 = plt.subplots()

ax1.set_ylabel('Wind Speed', color='blue')

ax2 = ax1.twinx()  # instantiate a second Axes that shares the same x-axis

ax2.set_ylabel('sin', color='purple')  # we already handled the x-label with ax1

ax1.plot(
                    Gusts_Albury_Weather_df['Date'],
                    Gusts_Albury_Weather_df['WindGustSpeed'],
                    color='blue',
                    alpha=0.3,
                    label='Gust Wind Speed'
              )
ax1.tick_params(axis='y', labelcolor='blue')


ax2.plot(
                    Albury_Buildings_df['Year (ending June 30)'],
                    Albury_Buildings_df['Complete Total'],
                    color='purple',
                    alpha=0.3,
                    label = 'Buildings'
              )

ax2.tick_params(axis='y', labelcolor='purple')

plt.legend()
plt.xlabel("Date")
plt.ylabel("Wind Speed (Km/h)")
plt.title('Wind Speed vs Gust Speed in Albury')
plt.tight_layout()
plt.show()
