#--- Imports ---
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

#----Global Variables----#
quit = False

#----Setup dataframe and query it here prior to creating visualisation and UI functions----#
Weather_df = pd.read_csv('data/Weather.csv')

#--- Albury ---
Albury_Weather_df = Weather_df[Weather_df.Location == 'Albury']

#--- Gusts ---
#Gusts_Albury_Weather_df = Albury_Weather_df[['Date', 'WindGustSpeed']]

#--- Wind Speed ---
WindSpeed_Albury_Weather_df = Albury_Weather_df[['Date', 'WindSpeed3pm', 'WindGustSpeed']]

print(WindSpeed_Albury_Weather_df)

WindSpeed_Albury_Weather_df.plot(
                    #kind='bar',
                    x='Date',
                    y= 'WindGustSpeed',
                    color='blue',
                    alpha=0.3,
                    label='Gust Wind Speed'
              )

WindSpeed_Albury_Weather_df.plot(
                    #kind='bar',
                    x='Date',
                    y= 'WindSpeed3pm',
                    color='purple',
                    alpha=0.3,
                    label = 'Wind Speed'
              )
plt.legend()
plt.title('Wind Speed vs Gust Speed in Albury')
plt.show()

