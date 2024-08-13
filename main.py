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
Gusts_Albury_Weather_df = Albury_Weather_df[['Date', 'WindGustSpeed']]

#--- Wind Speed ---
WindSpeed_Albury_Weather_df = Albury_Weather_df[['Date', 'WindSpeed3pm']]

print(WindSpeed_Albury_Weather_df)

'''Gusts_Albury_Weather_df.plot(
                    #kind='bar',
                    x='Date',
                    y= 'WindGustSpeed',
                    color='blue',
                    alpha=0.3,
                    title='Gust Wind Speed in Albury'
              )'''

WindSpeed_Albury_Weather_df.plot(
                    #kind='bar',
                    x='Date',
                    y= 'WindSpeed3pm',
                    color='blue',
                    alpha=0.3,
                    title='Wind Speed in Albury'
              )

plt.show()

