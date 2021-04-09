import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import time
from datetime import datetime
import os


class Graph:

    def __init__(self):
        self.isDfSet = False
        self.dataframe = {}

    def data_frame(self, all_data):
        overview_dict = {}

        daily_stats_df = ['date', 'sunrise time', 'sunset time', 'pressure', 'humidity', 'dew point', 'wind speed',
                          'clouds', 'uvi']
        daily_ds_keys = ['dt', 'sunrise', 'sunset', 'pressure', 'humidity', 'dew_point', 'wind_speed', 'clouds', 'uvi']
        date = []

        temp_stats = ['day', 'min', 'max', 'night', 'eve', 'morn']  # for the temp keys in dataset
        time_of_day = ['day', 'night', 'eve', 'morn']  # for feels like keys in dataset

        temps_avg = ['daily_avg', 'daily_min', 'daily_max', 'night_avg', 'eve_avg',
                     'morn_avg']  # key names for overview_dict
        temps_fl = ['daily_fl', 'night_fl', 'eve_fl', 'morn_fl']  # key names for overview_dict

        for key_name in daily_stats_df:
            overview_dict[key_name] = []

        for x in range(0, 8):  # for loop for daily weather stats
            for ds_key, df_key_name in zip(daily_ds_keys, daily_stats_df):

                if ds_key == 'dt':
                    overview_dict[df_key_name].append(time.ctime(all_data['daily'][x][ds_key])[:10])

                elif ds_key == 'sunrise' or ds_key == 'sunset':
                    overview_dict[df_key_name].append(time.ctime(all_data['daily'][x][ds_key])[11:16])

                elif ds_key == 'dew_point':
                    value = (all_data['daily'][x][ds_key] - 273.15)
                    overview_dict[df_key_name].append(round(value))

                elif ds_key == 'wind_speed':  # formula from https://www.checkyourmath.com/convert/speed/per_second_hour/m_per_second_km_per_hour.php
                    value = ((all_data['daily'][x][ds_key]) * 3.6)
                    overview_dict[df_key_name].append(round(value))

                else:
                    overview_dict[df_key_name].append(all_data['daily'][x][ds_key])

        for key_name in temps_avg:
            overview_dict[key_name] = []

        for x in range(0, 8):  # for loop for the temp_avg's
            for data_key, key_name in zip(temp_stats,
                                          temps_avg):  # code help from https://www.oreilly.com/library/view/python-cookbook/0596001673/ch01s15.html
                value = (all_data['daily'][x]['temp'][data_key] - 273.15)
                overview_dict[key_name].append(round(value))

        for key_name in temps_fl:
            overview_dict[key_name] = []

        for x in range(0, 8):  # for loop for the temp_avg's
            for data_key, key_name in zip(time_of_day,
                                          temps_fl):  # code help from https://www.oreilly.com/library/view/python-cookbook/0596001673/ch01s15.html
                value = (all_data['daily'][x]['temp'][data_key] - 273.15)
                overview_dict[key_name].append(round(value))

        df = pd.DataFrame.from_dict(overview_dict)
        self.isDfSet = True
        pd.set_option('display.max_columns',
                      None)  # https://thispointer.com/python-pandas-how-to-display-full-dataframe-i-e-print-all-rows-columns-without-truncation/
        self.dataframe = df

    # //////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

    def chart_temp_overview(self, cityName):
        plt.figure(figsize=(10, 8))
        x = self.dataframe['date'].values
        y1 = self.dataframe['daily_avg'].values
        y2 = self.dataframe['daily_fl'].values
        y3 = self.dataframe['daily_max'].values
        y4 = self.dataframe['daily_min'].values

        plt.plot(x, y1, color='yellow', label='Daily Averages', lw=5,
                 marker='*', markersize=10, markerfacecolor='blue', markeredgecolor='blue')
        plt.plot(x, y2, color='blue', label='Daily feels like', ls='--')
        plt.plot(x, y3, color='green', label='Daily max')
        plt.plot(x, y4, color='red', label='Daily min')

        # for visiual neatness
        plt.tick_params(axis='x', rotation=45)
        plt.grid()
        plt.axhline(y=0, color='black', label='Freezing Point')

        plt.title(f'Temperature Overview For the Next 7 Days in {cityName}, ON')
        plt.legend()

        # code help below from https://stackoverflow.com/questions/11373610/save-matplotlib-file-to-a-directory
        code_path = os.path.abspath(
            'graphs library')  # Figures out the absolute path for you in case your working directory moves around.
        graph_name = 'temp_overview.png'
        plt.savefig(os.path.join(code_path, graph_name), pad_inches=0.5)
        plt.show()

    def custom(self, y_val, cityName, y_lab):
        if self.isDfSet == False:
            print('df needs to be set')

        else:
            plt.figure(figsize=(10, 8)) 
            x = self.dataframe['date'].values
            y = self.dataframe[y_val].values
            plt.plot(x, y, color='red', label=y_val)

            plt.tick_params(axis='x', rotation=45)
            plt.grid()
            plt.title(y_lab + ' in ' + cityName + ' for the next 7 days')
            plt.xlabel('Date')
            plt.ylabel(y_lab + ' in °C')
            plt.tight_layout()
            plt.show()    
