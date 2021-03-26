import http.client
from tkinter import *
import re
import json


# https://www.youtube.com/watch?v=YXPyB4XeYLA
############################ KEEP IN MIND ######################################
# There is a limit of 125 pulls from the API daily. If it occurs that you have
# reached the limit the use the sample data below as it should look the exact
# same as the actual data received from the API.

sample_data = {'rh': 80, 'pod': 'n', 'lon': -80.60091, 'pres': 979.9,
 'timezone': 'America/New_York', 'ob_time': '2021-03-26 04:00',
 'country_code': 'US', 'clouds': 100, 'ts': 1616731200, 'solar_rad': 0,
 'state_code': 'OH', 'city_name': 'Toronto', 'wind_spd': 3.1,
 'wind_cdir_full': 'south-southeast', 'wind_cdir': 'SSE',
 'slp': 1024.2, 'vis': 5, 'h_angle': -90, 'sunset': '23:41',
 'dni': 0, 'dewpt': 10, 'snow': 0, 'uv': 0, 'precip': 0, 'wind_dir': 150,
 'sunrise': '11:15', 'ghi': 0, 'dhi': 0, 'aqi': 32, 'lat': 40.46423,
 'weather': {'icon': 'c04n', 'code': 804, 'description': 'Overcast clouds'},
 'datetime': '2021-03-26:04', 'temp': 13.4, 'station': 'NCUW2',
'elev_angle': -42.93, 'app_temp': 13.4}

################################################################################
''' 
    #TODO
    - Validation doesn't work properly just yet, going to experiment with 
      exceptions 
    - https://stackoverflow.com/questions/9054820/python-requests-exception-handling
    - Current error if user spams an input, running into an error I believe
      decoding the data or something like that
'''
################################################################################


class MyGUI:
    """
    This class represents the UI that is present in the program from the user
    to input the desired city that they wish to know the weather of

    === Attributes ===
    root:
        special item from tkinter

    """
    def __init__(self):
        self.root = Tk()
        self.initGUI()
        self.root.mainloop()

    def initGUI(self):
        """
        Function is used to initialize the overall visual look of the
        application which includes:

        monthLbl:
            Static label that has texting prompting the user a question
        validation:
            Variable used to determine whether the user input is valid using the
            only_letters method
        city_name:
            A StringVar used to take in the user input
        monthEntry:
            An Entry used to take in single-line text strings using city_name
        status:
            A StringVar
        statusLbl:
            A Label used to display the message of whether or not the inputted
            string is a valid city name
        checkBtn:
            A button used that calls upon the validateweather method
        """

        self.monthLbl = Label(self.root, text="What's the city you wish to know the weather of? ")

        validation = self.root.register(self.only_letters)
        self.city_name = StringVar()
        self.monthEntry = Entry(self.root, textvariable=self.city_name, validate='key', validatecommand=(validation, '%S'), invalidcommand=lambda: self.status.set('No Numbers Allowed'))

        self.status = StringVar()
        self.statusLbl = Label(self.root, textvariable=self.status)

        self.checkBtn = Button(self.root, text='Check', command=self.validate_weather)

        self.monthLbl.pack()
        self.monthEntry.pack()
        self.statusLbl.pack()
        self.checkBtn.pack()

    def only_letters(self, char):
        """
        Function to check if the input by the user into the
        StringVar() (city_name) is strictly letters.

        char: the character inputted by the user

        Returns whether <char> is a True valid character
        """

        self.only_letters_pattern = re.compile('[a-zA-Z]')
        return self.only_letters_pattern.match(char) is not None

    def validate_weather(self, event=None):
        """
        Function determines if the inputted city gives a valid set of data.
        If the city returns valid data then the "status" will change, if the
        data is good then its set to "It's a valid city", if not then its
        set to "Invalid city".
        """

        if len(self.city_name.get()) != 0:
            weather_data = Weather(self.city_name.get()).get_weather()
            if weather_data != None: # Figure this out
                print("GOOD CITY")
                self.status.set("It's a valid city")
            else:
                print("BAD CITY")
                self.status.set("Invalid city")


class Weather:
    """
    This class represents weather API. Takes in the inputted city name
    and attempts to get the data from the API.

    API: https://rapidapi.com/weatherbit/api/weather

    === Attributes ===
    city_name:
        string inputted into the class
    con:
        uses methods from htt.client to connect to the API
    refine_data:
        the data that will be returned
    """
    def __init__(self, city_name=''):
        self.city_name = city_name
        self.conn = http.client.HTTPSConnection("weatherbit-v1-mashape.p.rapidapi.com")
        self.headers = {
            'x-rapidapi-key': "7074916a96mshed85e07f0dc6e11p1ff717jsn38b199c89b6f",
            'x-rapidapi-host': "weatherbit-v1-mashape.p.rapidapi.com"
        }
        self.refine_data = {}
        if self.city_name != '':
            self.get_weather()
        else:
            return None

    def get_weather(self):
        """
        Function requests from the API the data of the desired city. If possible
        then decodes it and strips it down to an dictionary and returns it
        """
        self.conn.request("GET", "/current?city="+self.city_name, headers=self.headers)
        res = self.conn.getresponse()
        data = res.read()
        self.refine_data = json.loads(data.decode("utf-8"))['data'][0]
        print(self.refine_data)
        return self.refine_data


if __name__ == '__main__':
    app = MyGUI()

############################## API DOCUMENTATION ##############################
"""
city_name (string, optional):
    City name (closest),
    
state_code (string, optional):
    State abbreviation ,
    
country_code (string, optional):
    Country abbreviation ,
    
timezone (string, optional):
    Local IANA time zone ,
    
lat (number, optional):
    Latitude ,
    
lon (number, optional):
    Longitude ,
    
station (string, optional):
    Source Station ID ,
    
vis (integer, optional):
    Visibility - default (M) ,
    
rh (integer, optional):
    Relative humidity (%) ,
    
dewpt (number, optional):
    Dew point temperature - default (C) ,
    
wind_dir (integer, optional):
    Wind direction (degrees) ,
    
wind_cdir (string, optional):
    Cardinal wind direction ,
    
wind_cdir_full (string, optional):
    Cardinal wind direction (text) ,
    
wind_speed (number, optional):
    Wind speed - Default (m/s) ,
    
temp (number, optional):
    Temperature - Default (C) ,
    
app_temp (number, optional):
    Apparent temperature - Default (C) ,
    
clouds (integer, optional):
    Cloud cover (%) ,
    
weather (inline_model_2, optional),

datetime (string, optional):
    Cycle Hour (UTC) of observation ,
    
ob_time (string, optional):
    Full time (UTC) of observation (YYYY-MM-DD HH:MM) ,
    
ts (number, optional):
    Unix Timestamp ,
    
sunrise (string, optional):
    Time (UTC) of Sunrise (HH:MM) ,
    
sunset (string, optional):
    Time (UTC) of Sunset (HH:MM) ,
    
slp (number, optional):
    Mean sea level pressure in millibars (mb) ,
    
pres (number, optional):
    Pressure (mb) ,
    
aqi (number, optional):
    Air quality index (US EPA standard 0 to +500) ,
    
uv (number, optional):
    UV Index ,
    
solar_rad (number, optional):
    Estimated solar radiation (W/m^2) ,
    
ghi (number, optional):
    Global horizontal irradiance (W/m^2) ,
    
dni (number, optional):
    Direct normal irradiance (W/m^2) ,
    
dhi (number, optional):
    Diffuse horizontal irradiance (W/m^2) ,
    
elev_angle (number, optional):
    Current solar elevation angle (Degrees) ,
    
hour_angle (number, optional):
    Current solar hour angle (Degrees) ,
    
pod (string, optional):
    Part of the day (d = day, n = night) ,
    
precip (number, optional):
    Precipitation in last hour - Default (mm) ,
    
snow (number, optional):
    Snowfall in last hour - Default (mm) 
"""
