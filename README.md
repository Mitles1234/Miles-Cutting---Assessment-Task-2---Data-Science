# Miles Cutting - Assessment Task 2 - Data Science
# Affect of Buildings on Wind Speed Accross Australia

This program creates a graph on data relating to the wind speed, gust speed, and amount of buildings in locations accross Australa. The data show can be chosen by the user by toggling on and off settings in the home page and in the settings page. The live weather page uses an API to show live weather data of any given location.

To launch the software, simply run the main.py file, after this, a new window will appear showing the home page.

Their are 3 main pages the user can use to interact with the software, the home page, the settings page, and the live weather data page. The fourth help page just shows this document. 

# --- Using the Software ---
# Home Page
The home page shows the graph, and has quick settings for interacting with the graph. The first 4 options are the 4 different locations the user can choose to show the data from, they are Albury, Coffs Harbour, Newcastle, and Penrith. The next 3 options show what data can be shown about the location onto the graph. These are the wind speed of a location, the gust speed of a location, and the amount of new buildings compounding from the begining of the graph timeline to the end. (This is designed to show the average trend of new buildings being built rather that being used as pure facts and figures). The refresh button on this page refreshes the graph to show any updates to the settings of the graph. The final object on the page is the graph's toolbar which allows the user to interact with the graph by preforming functions such as zooming in, or exporting it as a png.

# Settings Page
The settings page allows the user to choose what colours to use for each of the data show, i.e Wind Speed, Gust Speed, and Qty of Buildings. To show these colours on the graph, the refresh button on the home page must be pressed.

# Live Weather Data
The live weather data uses the openweather api to show the weather conditions i.e Sunny, Cloudy, Raining, to show the temperature, and the current wind speed (in Knots) and direction. To interact with this page, simply type in a location to the text box, and press the print button to print off the information. If there is an error or the location the user has entered is not recognised, the software will print out an error message in the GUI informing the user.

# --- Notes ---
# Missing Data:

