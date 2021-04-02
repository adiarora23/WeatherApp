# -*- coding: UTF-8 -*-
# ^ added this since declaration is required ^

# -------- Import Files ---------
import tkinter
from tkinter import *
import tkinter as tk
from main import *
from graph import *
import json
from pytz import timezone
import time
from canada_cities import canada
from tkinter import messagebox, filedialog
from PIL import Image, ImageTk  # Library used for handling images
from configparser import ConfigParser  # Library used for config files
import requests  # Library used to access web data
from typing import Tuple, Optional, Union  # Library used for type hinting
from datetime import datetime


# ------------------------- GUI Classes -------------------------------
class WeatherApp:

    def __init__(self, api: str) -> None:
        self.root = Tk()
        self.root.geometry('950x600')
        self.root.config(bg='#34ABCD')
        self.api = api
        self.initGUI()
        self.initMenu()
        self.root.mainloop()

    def initGUI(self) -> None:
        """ Initializes GUI."""
        self.cityName = StringVar()
        self.cityEntry = Entry(self.root, textvariable=self.cityName)
        self.cityEntry.pack()

        self.space = Label(self.root, bg="#34ABCD")  # adds a space between the entry box and button
        self.space.pack()

        self.searchBtn = Button(self.root, text="Search City", width=12,
                                command=self.search)
        self.searchBtn.pack()

        self.space = Label(self.root, bg="#34ABCD")  # adds a space between button and Location text
        self.space.pack()

        self.locationLbl = Label(self.root, text="Location", bg="#34ABCD", fg="#FFFFFF", font=("Century Gothic", 22, "bold"))
        self.locationLbl.pack()

        self.dayLbl = Label(self.root, text="Date", bg="#34ABCD", fg="#FFFFFF", font=("Century Gothic", 14))
        self.dayLbl.pack()

        self.picture = Label(self.root, bg="#34ABCD", image=None)
        self.picture.pack()

        self.weatherLbl = Label(self.root, bg="#34ABCD", fg="#FFFFFF", text="", font=("Century Gothic", 17, "bold"))
        self.weatherLbl.pack()

        self.desc = Label(self.root, bg="#34ABCD", fg="#FFFFFF", text="", font=("Century Gothic", 12))
        self.desc.pack()

        self.space = Label(self.root, bg="#34ABCD")
        self.space.pack(pady=10)

        self.forecastFrame = Frame(self.root, bg="#34ABCD")
        self.forecastFrame.pack()

        self.weeklyLbl = Label(self.forecastFrame, bg="#34ABCD", fg="#FFFFFF", text="Weekly Forecast:",
                               font=("Century Gothic", 17, "bold"))
        self.weeklyLbl.pack()

        self.space = Label(self.forecastFrame, bg="#34ABCD")
        self.space.pack()

        self.day1Frame = Frame(self.forecastFrame, bg="#34ABCD")
        self.day1Frame.pack(side=LEFT, padx=10)

        self.day1Lbl = Label(self.day1Frame, bg="#34ABCD", fg="#FFFFFF", text="", font=("Century Gothic", 15))
        self.day1Lbl.pack()

        self.day1Img = Label(self.day1Frame, bg="#34ABCD", image=None)
        self.day1Img.pack()

        self.day2Frame = Frame(self.forecastFrame, bg="#34ABCD")
        self.day2Frame.pack(side=LEFT, padx=10)

        self.day2Lbl = Label(self.day2Frame, bg="#34ABCD", fg="#FFFFFF", text="", font=("Century Gothic", 15))
        self.day2Lbl.pack()

        self.day2Img = Label(self.day2Frame, bg="#34ABCD", image=None)
        self.day2Img.pack()

        self.day3Frame = Frame(self.forecastFrame, bg="#34ABCD")
        self.day3Frame.pack(side=LEFT, padx=10)

        self.day3Lbl = Label(self.day3Frame, bg="#34ABCD", fg="#FFFFFF", text="", font=("Century Gothic", 15))
        self.day3Lbl.pack()

        self.day3Img = Label(self.day3Frame, bg="#34ABCD", image=None)
        self.day3Img.pack()

        self.day4Frame = Frame(self.forecastFrame, bg="#34ABCD")
        self.day4Frame.pack(side=LEFT, padx=10)

        self.day4Lbl = Label(self.day4Frame, bg="#34ABCD", fg="#FFFFFF", text="", font=("Century Gothic", 15))
        self.day4Lbl.pack()

        self.day4Img = Label(self.day4Frame, bg="#34ABCD", image=None)
        self.day4Img.pack()

        self.day5Frame = Frame(self.forecastFrame, bg="#34ABCD")
        self.day5Frame.pack(side=LEFT, padx=10)

        self.day5Lbl = Label(self.day5Frame, bg="#34ABCD", fg="#FFFFFF", text="", font=("Century Gothic", 15))
        self.day5Lbl.pack()

        self.day5Img = Label(self.day5Frame, bg="#34ABCD", image=None)
        self.day5Img.pack()

        self.day6Frame = Frame(self.forecastFrame, bg="#34ABCD")
        self.day6Frame.pack(side=LEFT, padx=10)

        self.day6Lbl = Label(self.day6Frame, bg="#34ABCD", fg="#FFFFFF", text="", font=("Century Gothic", 15))
        self.day6Lbl.pack()

        self.day6Img = Label(self.day6Frame, bg="#34ABCD", image=None)
        self.day6Img.pack()

        self.day7Frame = Frame(self.forecastFrame, bg="#34ABCD")
        self.day7Frame.pack(side=LEFT, padx=10)

        self.day7Lbl = Label(self.day7Frame, bg="#34ABCD", fg="#FFFFFF", text="", font=("Century Gothic", 15))
        self.day7Lbl.pack()

        self.day7Img = Label(self.day7Frame, bg="#34ABCD", image=None)
        self.day7Img.pack()

    # TODO: this will be updated constantly with new features as the project continues.
    def initMenu(self):
        menubar = Menu(self.root)
        actions_menu = Menu(menubar, tearoff=0)
        menubar.add_cascade(menu=actions_menu, label='Actions')

        submenu = Menu(actions_menu, tearoff=0)

        # Actions for the user

        actions_menu.add_cascade(label='Change Unit', menu=submenu, underline=0)
        actions_menu.add_command(label='Display Graph', command=self.display_graph)  # TODO: edit this
        actions_menu.add_command(label='Save', command=self.save_weather)
        actions_menu.add_command(label='Quit', command=self.root.destroy)

        submenu.add_command(label='Celsius', command=self.display_celsius, underline=0)
        submenu.add_command(label='Fahrenheit', command=self.display_fahrenheit, underline=0)

        self.root.config(menu=menubar)

    # TODO edit these functions for API to use
    def __celsius_to_fahrenheit(self, celsius):
        """Private Method: converts Celsius into Fahrenheit."""

        fahrenheit = (celsius * 9/5) + 32
        return round(fahrenheit)

    def display_celsius(self):
        """Displays weather in Celsius."""

        city = self.cityName.get()
        weather = get_weather(city)
        self.weatherLbl["text"] = f"Current Temperature: {round(weather[2])}°C, {weather[3]}"
        self.desc["text"] = f"{weather[4]}, feels like {round(weather[6])}°C"

        self.day1Lbl["text"] = f"{weather[22]}: {round(weather[8])}°C"
        self.day2Lbl["text"] = f"{weather[23]}: {round(weather[9])}°C"
        self.day3Lbl["text"] = f"{weather[24]}: {round(weather[10])}°C"
        self.day4Lbl["text"] = f"{weather[25]}: {round(weather[11])}°C"
        self.day5Lbl["text"] = f"{weather[26]}: {round(weather[12])}°C"
        self.day6Lbl["text"] = f"{weather[27]}: {round(weather[13])}°C"
        self.day7Lbl["text"] = f"{weather[28]}: {round(weather[14])}°C"

    def display_fahrenheit(self):
        """Displays weather in Fahrenheit."""

        city = self.cityName.get()
        weather = get_weather(city)
        self.weatherLbl["text"] = f"Current Temperature: {round(self.__celsius_to_fahrenheit(weather[2]))}°F, {weather[3]}"
        self.desc["text"] = f"{weather[4]}, feels like {round(self.__celsius_to_fahrenheit(weather[6]))}°F"

        self.day1Lbl["text"] = f"{weather[22]}: {round(self.__celsius_to_fahrenheit(weather[8]))}°F"
        self.day2Lbl["text"] = f"{weather[23]}: {round(self.__celsius_to_fahrenheit(weather[9]))}°F"
        self.day3Lbl["text"] = f"{weather[24]}: {round(self.__celsius_to_fahrenheit(weather[10]))}°F"
        self.day4Lbl["text"] = f"{weather[25]}: {round(self.__celsius_to_fahrenheit(weather[11]))}°F"
        self.day5Lbl["text"] = f"{weather[26]}: {round(self.__celsius_to_fahrenheit(weather[12]))}°F"
        self.day6Lbl["text"] = f"{weather[27]}: {round(self.__celsius_to_fahrenheit(weather[13]))}°F"
        self.day7Lbl["text"] = f"{weather[28]}: {round(self.__celsius_to_fahrenheit(weather[14]))}°F"

    def display_graph(self):
        pass

    def save_weather(self):
        city = self.cityName.get()
        weather = get_weather(city)
        saved_file = filedialog.asksaveasfile(mode='w', defaultextension='.txt')
        if saved_file is not None:
            saved_file.write(f"The city you chose was: {weather[0]}, {weather[1]}\n")
            saved_file.write(f"The temperature for that city at the time was: {round(weather[2])}°C ({round(self.__celsius_to_fahrenheit(weather[2]))}°F)\n")
            saved_file.write(f"The type of weather for that city at the time was: {weather[3]}\n")
            saved_file.write(f"The time this was saved was at: {weather[30]}\n")
            saved_file.close()

    def search(self) -> None:
        """ Searches the weather for the city entered. """
        city = self.cityName.get()
        weather = get_weather(city)

        if city == "":
            messagebox.showinfo(title=None, message="Please Enter a City")
        elif weather:
            self.locationLbl['text'] = f"{weather[0]}, {weather[1]}"
            self.dayLbl['text'] = f"{weather[29]}, {weather[30]}"
            img = ImageTk.PhotoImage(image=Image.open(f"icons/{weather[5]}.png").resize((115, 115)))
            self.picture["image"] = img
            self.weatherLbl["text"] = f"Current Temperature: {round(weather[2])}°C, {weather[3]}"
            self.desc["text"] = f"{weather[4]}, feels like {round(weather[6])}°C"

            self.day1Frame["highlightbackground"], self.day1Frame["highlightthickness"] = "#FFFFFF", 3
            self.day1Lbl["text"] = f"{weather[22]}: {round(weather[8])}°C"
            day1Pic = ImageTk.PhotoImage(image=Image.open(f"icons/{weather[15]}.png").resize((90, 90)))
            self.day1Img["image"] = day1Pic

            self.day2Frame["highlightbackground"], self.day2Frame["highlightthickness"] = "#FFFFFF", 3
            self.day2Lbl["text"] = f"{weather[23]}: {round(weather[9])}°C"
            day2Pic = ImageTk.PhotoImage(image=Image.open(f"icons/{weather[16]}.png").resize((90, 90)))
            self.day2Img["image"] = day2Pic

            self.day3Frame["highlightbackground"], self.day3Frame["highlightthickness"] = "#FFFFFF", 3
            self.day3Lbl["text"] = f"{weather[24]}: {round(weather[10])}°C"
            day3Pic = ImageTk.PhotoImage(image=Image.open(f"icons/{weather[17]}.png").resize((90, 90)))
            self.day3Img["image"] = day3Pic

            self.day4Frame["highlightbackground"], self.day4Frame["highlightthickness"] = "#FFFFFF", 3
            self.day4Lbl["text"] = f"{weather[25]}: {round(weather[11])}°C"
            day4Pic = ImageTk.PhotoImage(image=Image.open(f"icons/{weather[18]}.png").resize((90, 90)))
            self.day4Img["image"] = day4Pic

            self.day5Frame["highlightbackground"], self.day5Frame["highlightthickness"] = "#FFFFFF", 3
            self.day5Lbl["text"] = f"{weather[26]}: {round(weather[12])}°C"
            day5Pic = ImageTk.PhotoImage(image=Image.open(f"icons/{weather[19]}.png").resize((90, 90)))
            self.day5Img["image"] = day5Pic

            self.day6Frame["highlightbackground"], self.day6Frame["highlightthickness"] = "#FFFFFF", 3
            self.day6Lbl["text"] = f"{weather[27]}: {round(weather[13])}°C"
            day6Pic = ImageTk.PhotoImage(image=Image.open(f"icons/{weather[20]}.png").resize((90, 90)))
            self.day6Img["image"] = day6Pic

            self.day7Frame["highlightbackground"], self.day7Frame["highlightthickness"] = "#FFFFFF", 3
            self.day7Lbl["text"] = f"{weather[28]}: {round(weather[14])}°C"
            day7Pic = ImageTk.PhotoImage(image=Image.open(f"icons/{weather[21]}.png").resize((90, 90)))
            self.day7Img["image"] = day7Pic

            self.root.mainloop()
        else:
            messagebox.showerror("Search Error",
                                 f"Invalid input '{city}': city not found")


# TODO: update weather app with new API.
# ------------------------- Function class -------------------------------
def get_cityID(city: str) -> Tuple[Union[str, float]]:
    """Returns the coordinates of the city the user entered"""
    for place in canada:
        if place['name'].lower() == city.lower():
            if place['country'] == 'CA':
                lat = round(place['coord']['lat'], 2)
                lon = round(place['coord']['lon'], 2)
                return (place['name'], place['country'], lat, lon)
    return ("", "", "", "")


def get_current_time():
    """Returns the current time in a 12-hour scale."""
    current_time = datetime.now(timezone('US/Eastern'))
    get_hour = current_time.strftime('%I')
    if int(get_hour) < 10:
        t = current_time.strftime('%I %p')[1:]
    else:
        t = current_time.strftime('%I %p')
    return t


def get_weather(city: str) -> Tuple[Optional[Union[str, float]]]:
    """Returns a tuple containing strings and float"""
    cityID = get_cityID(city)
    data = requests.get(api_url.format(cityID[2], cityID[3], api_key))

    if data:
        data = data.json()
        city = cityID[0]
        country = cityID[1]
        temp = data['current']['temp'] - 273.15  # convertion of K to C*
        feels_like = data['current']['feels_like'] - 273.15
        weekly_forecast = data['daily'] # used to extract data for graphs
        current_weather = data['current']['weather'][0]['main']
        current_day = time.ctime(data['current']['dt'])[:3] + ", " + time.ctime(data['current']['dt'])[4:11]
        current_time = get_current_time()

        g = Graph()
        g.temp_overview(data)

        day1_temp = data['daily'][1]['temp']['day'] - 273.15
        day1_img = data['daily'][1]['weather'][0]['icon']
        day1_day = time.ctime(data['daily'][1]['dt'])[:3]

        day2_temp = data['daily'][2]['temp']['day'] - 273.15
        day2_img = data['daily'][2]['weather'][0]['icon']
        day2_day = time.ctime(data['daily'][2]['dt'])[:3]

        day3_temp = data['daily'][3]['temp']['day'] - 273.15
        day3_img = data['daily'][3]['weather'][0]['icon']
        day3_day = time.ctime(data['daily'][3]['dt'])[:3]

        day4_temp = data['daily'][4]['temp']['day'] - 273.15
        day4_img = data['daily'][4]['weather'][0]['icon']
        day4_day = time.ctime(data['daily'][4]['dt'])[:3]

        day5_temp = data['daily'][5]['temp']['day'] - 273.15
        day5_img = data['daily'][5]['weather'][0]['icon']
        day5_day = time.ctime(data['daily'][5]['dt'])[:3]

        day6_temp = data['daily'][6]['temp']['day'] - 273.15
        day6_img = data['daily'][6]['weather'][0]['icon']
        day6_day = time.ctime(data['daily'][6]['dt'])[:3]

        day7_temp = data['daily'][7]['temp']['day'] - 273.15
        day7_img = data['daily'][7]['weather'][0]['icon']
        day7_day = time.ctime(data['daily'][7]['dt'])[:3]

        desc = data['current']['weather'][0]['description']
        img = data['current']['weather'][0]['icon']

        return (city, country, temp, current_weather, desc, img, feels_like,
                weekly_forecast, day1_temp, day2_temp, day3_temp, day4_temp, day5_temp, day6_temp,
                day7_temp, day1_img, day2_img, day3_img, day4_img, day5_img, day6_img, day7_img,
                day1_day, day2_day, day3_day, day4_day, day5_day, day6_day, day7_day, current_day, current_time)

    else:
        return None


# ------------------------- Main Loop -------------------------------
if __name__ == "__main__":
    # TODO: Justin will update API for this.
    api_url = "https://api.openweathermap.org/data/2.5/onecall?lat={}&lon={}&exclude=minutely,hourly&appid={}"
    file = "config.ini"  # config file that contains the key to access the API data
    config = ConfigParser()  # used to parse through config files
    config.read(file)
    api_key = config["testapi_key"]["key"]  # gets the key for API from the file
    app = WeatherApp(api_url)
