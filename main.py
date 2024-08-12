#--- Imports ---
import pandas as pd
import matplotlib.pyplot as plt

#----Global Variables----#
quit = False

#----Setup dataframe and query it here prior to creating visualisation and UI functions----#
Weather_df = pd.read_csv('data/Weather.csv')

#--- Albury ---
Albury_Weather_df = Weather_df[Weather_df.Location == 'Albury']
Gusts_Albury_Weather_df = Albury_Weather_df.filter('WindGustSpeed')
WindSpeed_Albury_Weather_df = Albury_Weather_df.filter('WindSpeed3pm')

print(WindSpeed_Albury_Weather_df)

'''WindSpeed_Albury_Weather_df.plot(
                    kind='bar',
                    x='Time',
                    y='Speed',
                    color='blue',
                    alpha=0.3,
                    title='Cost of a Big Mac in AUD')
plt.show()'''