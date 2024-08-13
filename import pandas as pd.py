import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from sklearn import linear_model

#----Global Variables----#
quit = False

#----Setup dataframe and query it here prior to creating visualisation and UI functions----#
Weather_df = pd.read_csv('data/Weather.csv')

#--- Albury ---
Albury_Weather_df = Weather_df[Weather_df.Location == 'Albury']

#--- Wind Speed ---
WindSpeed_Albury_Weather_df = Albury_Weather_df[['Date', 'WindSpeed3pm']]

# Convert 'Date' column to datetime format if it's not already
WindSpeed_Albury_Weather_df['Date'] = pd.to_datetime(WindSpeed_Albury_Weather_df['Date'])

# Separate data for linear regression
dates = WindSpeed_Albury_Weather_df['Date'].values.reshape(-1, 1)  # Reshape for the model
wind_speeds = WindSpeed_Albury_Weather_df['WindSpeed3pm'].values

# Create linear regression model
reg = linear_model.LinearRegression()
reg.fit(Date, WindSpeed3pm)  # Train the model

# Get coefficients for the line equation (y = mx + b)
m = reg.coef_[0]  # Slope
b = reg.intercept_  # y-intercept

# Generate dates for the fitted line
predicted_dates = np.linspace(dates.min(), dates.max(), 100)[:, np.newaxis]  # Create array for plotting line

# Predicted wind speeds based on the line equation
predicted_wind_speeds = m * predicted_dates + b 

WindSpeed_Albury_Weather_df.plot(
    kind='scatter',
    x='Date',
    y='WindSpeed3pm',
    color='blue',
    alpha=0.3,
    title='Wind Speed in Albury'
)

# Plot the line of best fit
plt.plot(predicted_dates, predicted_wind_speeds, color='red')

plt.show()