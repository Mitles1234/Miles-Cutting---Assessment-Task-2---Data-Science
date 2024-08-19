elif Penrith == True:
        if PenrithWindSpeed == True:
            ax1.plot(
                        WindSpeed_Penrith_Weather_df['Date'],
                        WindSpeed_Penrith_Weather_df['WindSpeed3pm'],
                        color=ChartColour1,
                        alpha=0.3,
                        label = 'Wind Speed'
            )
        elif PenrithGustSpeed == True:
            ax1.plot(
                        Gusts_Penrith_Weather_df['Date'],
                        Gusts_Penrith_Weather_df['WindGustSpeed'],
                        color=ChartColour2,
                        alpha=0.3,
                        label = 'Gust Speed'
            )
            ax1.set_ylabel('Wind Speed (Km/h)', color='black')
            ax1.tick_params(axis='y', labelcolor='black')

        elif PenrithBuildings == True:
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