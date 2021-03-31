# -*- coding: UTF-8 -*-
# ^ added this since declaration is required ^

from tkinter import *
import tkinter as tk
from main import *
import json
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
        self.root.configure(bg="#34ABCD")
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

        self.locationLbl = Label(self.root, text="Location", bg="#34ABCD", fg="#FFFFFF", font=("bold", 22))
        self.locationLbl.pack()
        
        self.dayLbl = Label(self.root, text="Date", bg="#34ABCD", fg="#FFFFFF", font=("bold", 14))
        self.dayLbl.pack()

        self.picture = Label(self.root, bg="#34ABCD", image=None)
        self.picture.pack()

        self.weatherLbl = Label(self.root, bg="#34ABCD", fg="#FFFFFF", text="", font=("bold", 17))
        self.weatherLbl.pack()

        self.desc = Label(self.root, bg="#34ABCD", fg="#FFFFFF", text="", font=("bold", 10))
        self.desc.pack()

        self.space = Label(self.root, bg="#34ABCD")
        self.space.pack(pady=10)
        
        self.forecastFrame = Frame(self.root,bg="#34ABCD")
        self.forecastFrame.pack()
        
        self.weeklyLbl = Label(self.forecastFrame, bg="#34ABCD", fg="#FFFFFF", text="Weekly Forecast:", font=("bold", 17))
        self.weeklyLbl.pack()
        
        self.space = Label(self.forecastFrame, bg="#34ABCD")
        self.space.pack()        

        self.day1Frame = Frame(self.forecastFrame,bg="#34ABCD")
        self.day1Frame.pack(side=LEFT, padx=10)

        self.day1Lbl = Label(self.day1Frame, bg="#34ABCD", fg="#FFFFFF", text="", font=("bold", 15))
        self.day1Lbl.pack()

        self.day1Img = Label(self.day1Frame, bg="#34ABCD", image=None)
        self.day1Img.pack()

        self.day2Frame = Frame(self.forecastFrame,bg="#34ABCD")
        self.day2Frame.pack(side=LEFT, padx=10)

        self.day2Lbl = Label(self.day2Frame, bg="#34ABCD", fg="#FFFFFF", text="", font=("bold", 15))
        self.day2Lbl.pack()

        self.day2Img = Label(self.day2Frame, bg="#34ABCD", image=None)
        self.day2Img.pack()

        self.day3Frame = Frame(self.forecastFrame,bg="#34ABCD")
        self.day3Frame.pack(side=LEFT, padx=10)

        self.day3Lbl = Label(self.day3Frame, bg="#34ABCD", fg="#FFFFFF", text="", font=("bold", 15))
        self.day3Lbl.pack()

        self.day3Img = Label(self.day3Frame, bg="#34ABCD", image=None)
        self.day3Img.pack()

        self.day4Frame = Frame(self.forecastFrame,bg="#34ABCD")
        self.day4Frame.pack(side=LEFT, padx=10)        

        self.day4Lbl = Label(self.day4Frame, bg="#34ABCD", fg="#FFFFFF", text="", font=("bold", 15))
        self.day4Lbl.pack()

        self.day4Img = Label(self.day4Frame, bg="#34ABCD", image=None)
        self.day4Img.pack()

        self.day5Frame = Frame(self.forecastFrame,bg="#34ABCD")
        self.day5Frame.pack(side=LEFT, padx=10) 

        self.day5Lbl = Label(self.day5Frame, bg="#34ABCD", fg="#FFFFFF", text="", font=("bold", 15))
        self.day5Lbl.pack()

        self.day5Img = Label(self.day5Frame, bg="#34ABCD", image=None)
        self.day5Img.pack()

        self.day6Frame = Frame(self.forecastFrame,bg="#34ABCD")
        self.day6Frame.pack(side=LEFT, padx=10) 

        self.day6Lbl = Label(self.day6Frame, bg="#34ABCD", fg="#FFFFFF", text="", font=("bold", 15))
        self.day6Lbl.pack()

        self.day6Img = Label(self.day6Frame, bg="#34ABCD", image=None)
        self.day6Img.pack()

        self.day7Frame = Frame(self.forecastFrame,bg="#34ABCD")
        self.day7Frame.pack(side=LEFT, padx=10) 

        self.day7Lbl = Label(self.day7Frame, bg="#34ABCD", fg="#FFFFFF", text="", font=("bold", 15))
        self.day7Lbl.pack()

        self.day7Img = Label(self.day7Frame, bg="#34ABCD", image=None)
        self.day7Img.pack()

        
    # TODO: this will be updated constantly with new features as the project continues.
    def initMenu(self):
        menubar = Menu(self.root)
        actions_menu = Menu(menubar, tearoff=0)

        menubar.add_cascade(menu=actions_menu, label='Actions')

        # Actions for the user:
        # TODO edit this after real API is installed
        actions_menu.add_command(label='Display Graph', command=self.display_graph)  # TODO: edit this
        actions_menu.add_command(label='Change Unit', command=self.celsius_to_fahrenheit)  # TODO: edit this
        actions_menu.add_command(label='Save', command=self.save_weather)
        actions_menu.add_command(label='Quit', command=self.root.destroy)

        self.root.config(menu=menubar)

    # TODO edit these functions for API to use
    def celsius_to_fahrenheit(self):
        pass

    def display_graph(self):
        pass

    def save_weather(self):
        city = self.cityName.get()
        weather = get_weather(city)
        saved_file = filedialog.asksaveasfile(mode='w', defaultextension='.txt')
        if saved_file is not None:
            saved_file.write(f"The city you chose was: {weather[0]}, {weather[1]}\n")
            saved_file.write(f"The temperature for that city at the time was: {round(weather[2])}°C\n")
            saved_file.write(f"The type of weather for that city at the time was: {weather[3]}\n")
            saved_file.close()

    def search(self) -> None:
        """ Searches the weather for the city entered. """
        city = self.cityName.get()
        weather = get_weather(city)

        if city == "":
            messagebox.showinfo(title=None, message="Please Enter a City")
        elif weather:
            self.locationLbl['text'] = f"{weather[0]}, {weather[1]}"
            self.dayLbl['text'] = f"{weather[29]}"
            img = ImageTk.PhotoImage(image=Image.open(f"icons/{weather[5]}.png").resize((115, 115)))
            self.picture["image"] = img
            self.weatherLbl["text"] = f"Current Temperature: {round(weather[2])}°C, {weather[3]}"
            self.desc["text"] = f"{weather[4]}, feels like {round(weather[6])}°C"
            
            self.day1Frame["highlightbackground"],self.day1Frame["highlightthickness"] = "#FFFFFF",3
            self.day1Lbl["text"] = f"{weather[22]}: {round(weather[8])}°C"
            day1Pic = ImageTk.PhotoImage(image=Image.open(f"icons/{weather[15]}.png").resize((90, 90)))
            self.day1Img["image"] = day1Pic

            self.day2Frame["highlightbackground"],self.day2Frame["highlightthickness"] = "#FFFFFF",3
            self.day2Lbl["text"] = f"{weather[23]}: {round(weather[9])}°C"
            day2Pic = ImageTk.PhotoImage(image=Image.open(f"icons/{weather[16]}.png").resize((90, 90)))
            self.day2Img["image"] = day2Pic

            self.day3Frame["highlightbackground"],self.day3Frame["highlightthickness"] = "#FFFFFF",3
            self.day3Lbl["text"] = f"{weather[24]}: {round(weather[10])}°C"
            day3Pic = ImageTk.PhotoImage(image=Image.open(f"icons/{weather[17]}.png").resize((90, 90)))
            self.day3Img["image"] = day3Pic

            self.day4Frame["highlightbackground"],self.day4Frame["highlightthickness"] = "#FFFFFF",3
            self.day4Lbl["text"] = f"{weather[25]}: {round(weather[11])}°C"
            day4Pic = ImageTk.PhotoImage(image=Image.open(f"icons/{weather[18]}.png").resize((90, 90)))
            self.day4Img["image"] = day4Pic
            
            self.day5Frame["highlightbackground"],self.day5Frame["highlightthickness"] = "#FFFFFF",3
            self.day5Lbl["text"] = f"{weather[26]}: {round(weather[12])}°C"
            day5Pic = ImageTk.PhotoImage(image=Image.open(f"icons/{weather[19]}.png").resize((90, 90)))
            self.day5Img["image"] = day5Pic

            self.day6Frame["highlightbackground"],self.day6Frame["highlightthickness"] = "#FFFFFF",3
            self.day6Lbl["text"] = f"{weather[27]}: {round(weather[13])}°C"
            day6Pic = ImageTk.PhotoImage(image=Image.open(f"icons/{weather[20]}.png").resize((90, 90)))
            self.day6Img["image"] = day6Pic

            self.day7Frame["highlightbackground"],self.day7Frame["highlightthickness"] = "#FFFFFF",3
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
    """ Returns the coordinates of the city the user entered"""
    for place in canada:
        if place['name'].lower() == city.lower():
            if place['country'] == 'CA':
                lat = round(place['coord']['lat'], 2)
                lon = round(place['coord']['lon'], 2)
                return (place['name'], place['country'], lat, lon)
    return ("", "", "", "")


def get_weather(city: str) -> Tuple[Optional[Union[str, float]]]:
    """ Returns a tuple containing strings and float """
    cityID = get_cityID(city)
    data = requests.get(api_url.format(cityID[2], cityID[3], api_key))

    if data:
        data = data.json()
        city = cityID[0]
        country = cityID[1]
        temp = data['current']['temp'] - 273.15
        feels_like = data['current']['feels_like'] - 273.15
        weekly_forecast = data['daily']  # will be used for displaying other days' weather,
        # will also be useful in providing data for graphing (i.e. change in temp throughout the week, etc.)
        # Isha can use this info to extract data and make appropriate graphs
        current_weather = data['current']['weather'][0]['main']
        current_day = time.ctime(data['current']['dt'])[:3] + ", " + time.ctime(data['current']['dt'])[4:11]
        #current_time = data['current']['dt']
        #current_time_form = datetime.utcfromtimestamp(int(current_time)).strftime('%Y-%m-%d %H:%M:%S')
        #print(current_time_form)

        day1_temp = data['daily'][1]['temp']['day'] - 273.15
        day1_img = data['daily'][1]['weather'][0]['icon']
        day1_day = time.ctime(data['daily'][1]['dt'])[:3]
        #monday_time = data['daily'][1]['dt']
        #monday_time_form = datetime.utcfromtimestamp(int(monday_time)).strftime('%Y-%m-%d %H:%M:%S')        
        
        
        day2_temp = data['daily'][2]['temp']['day'] - 273.15
        day2_img = data['daily'][2]['weather'][0]['icon']
        day2_day = time.ctime(data['daily'][2]['dt'])[:3]
        #tuesday_time = data['daily'][2]['dt']
        #tuesday_time_form = datetime.utcfromtimestamp(int(tuesday_time)).strftime('%Y-%m-%d %H:%M:%S') 


        day3_temp = data['daily'][3]['temp']['day'] - 273.15
        day3_img = data['daily'][3]['weather'][0]['icon']
        day3_day = time.ctime(data['daily'][3]['dt'])[:3]
        #wednesday_time = data['daily'][3]['dt']
        #wednesday_time_form = datetime.utcfromtimestamp(int(wednesday_time)).strftime('%Y-%m-%d %H:%M:%S')          

        day4_temp = data['daily'][4]['temp']['day'] - 273.15
        day4_img = data['daily'][4]['weather'][0]['icon']
        day4_day = time.ctime(data['daily'][4]['dt'])[:3]
        #thursday_time = data['daily'][4]['dt']
        #thursday_time_form = datetime.utcfromtimestamp(int(thursday_time)).strftime('%Y-%m-%d %H:%M:%S')              


        day5_temp = data['daily'][5]['temp']['day'] - 273.15
        day5_img = data['daily'][5]['weather'][0]['icon']
        day5_day = time.ctime(data['daily'][5]['dt'])[:3]
        #friday_time = data['daily'][5]['dt']
        #friday_time_form = datetime.utcfromtimestamp(int(friday_time)).strftime('%Y-%m-%d %H:%M:%S')         

        day6_temp = data['daily'][6]['temp']['day'] - 273.15
        day6_img = data['daily'][6]['weather'][0]['icon']
        day6_day = time.ctime(data['daily'][6]['dt'])[:3]
        #saturday_time = data['daily'][3]['dt']
        #saturday_time_form = datetime.utcfromtimestamp(int(saturday_time)).strftime('%Y-%m-%d %H:%M:%S')         

        day7_temp = data['daily'][7]['temp']['day'] - 273.15
        day7_img = data['daily'][7]['weather'][0]['icon']
        day7_day = time.ctime(data['daily'][7]['dt'])[:3]
        #sunday_time = data['daily'][3]['dt']
        #sunday_time_form = datetime.utcfromtimestamp(int(sunday_time)).strftime('%Y-%m-%d %H:%M:%S')        

        desc = data['current']['weather'][0]['description']
        img = data['current']['weather'][0]['icon']

        return (city, country, temp, current_weather, desc, img, feels_like,
                weekly_forecast, day1_temp, day2_temp, day3_temp, day4_temp, day5_temp, day6_temp,
                day7_temp, day1_img, day2_img, day3_img, day4_img, day5_img, day6_img, day7_img,
                day1_day, day2_day, day3_day, day4_day, day5_day, day6_day, day7_day, current_day)

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