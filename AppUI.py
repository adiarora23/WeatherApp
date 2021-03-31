# -*- coding: UTF-8 -*-
# ^ added this since declaration is required ^

from tkinter import *
import tkinter as tk
from main import *
import json
from canada_cities import canada
from tkinter import messagebox, filedialog
from PIL import Image, ImageTk  # Library used for handling images
from configparser import ConfigParser  # Library used for config files
import requests  # Library used to access web data
from typing import Tuple, Optional, Union  # Library used for type hinting


# ------------------------- GUI Classes -------------------------------
class WeatherApp:

    def __init__(self, api: str) -> None:
        self.root = Tk()
        self.root.geometry('950x550')
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

        self.mondayFrame = Frame(self.forecastFrame,bg="#34ABCD")
        self.mondayFrame.pack(side=LEFT, padx=10)

        self.mondayLbl = Label(self.mondayFrame, bg="#34ABCD", fg="#FFFFFF", text="", font=("bold", 15))
        self.mondayLbl.pack()

        self.mondayImg = Label(self.mondayFrame, bg="#34ABCD", image=None)
        self.mondayImg.pack()

        self.tuesdayFrame = Frame(self.forecastFrame,bg="#34ABCD")
        self.tuesdayFrame.pack(side=LEFT, padx=10)

        self.tuesdayLbl = Label(self.tuesdayFrame, bg="#34ABCD", fg="#FFFFFF", text="", font=("bold", 15))
        self.tuesdayLbl.pack()

        self.tuesdayImg = Label(self.tuesdayFrame, bg="#34ABCD", image=None)
        self.tuesdayImg.pack()

        self.wednesdayFrame = Frame(self.forecastFrame,bg="#34ABCD")
        self.wednesdayFrame.pack(side=LEFT, padx=10)

        self.wednesdayLbl = Label(self.wednesdayFrame, bg="#34ABCD", fg="#FFFFFF", text="", font=("bold", 15))
        self.wednesdayLbl.pack()

        self.wednesdayImg = Label(self.wednesdayFrame, bg="#34ABCD", image=None)
        self.wednesdayImg.pack()

        self.thursdayFrame = Frame(self.forecastFrame,bg="#34ABCD")
        self.thursdayFrame.pack(side=LEFT, padx=10)        

        self.thursdayLbl = Label(self.thursdayFrame, bg="#34ABCD", fg="#FFFFFF", text="", font=("bold", 15))
        self.thursdayLbl.pack()

        self.thursdayImg = Label(self.thursdayFrame, bg="#34ABCD", image=None)
        self.thursdayImg.pack()

        self.fridayFrame = Frame(self.forecastFrame,bg="#34ABCD")
        self.fridayFrame.pack(side=LEFT, padx=10) 

        self.fridayLbl = Label(self.fridayFrame, bg="#34ABCD", fg="#FFFFFF", text="", font=("bold", 15))
        self.fridayLbl.pack()

        self.fridayImg = Label(self.fridayFrame, bg="#34ABCD", image=None)
        self.fridayImg.pack()

        self.saturdayFrame = Frame(self.forecastFrame,bg="#34ABCD")
        self.saturdayFrame.pack(side=LEFT, padx=10) 

        self.saturdayLbl = Label(self.saturdayFrame, bg="#34ABCD", fg="#FFFFFF", text="", font=("bold", 15))
        self.saturdayLbl.pack()

        self.saturdayImg = Label(self.saturdayFrame, bg="#34ABCD", image=None)
        self.saturdayImg.pack()

        self.sundayFrame = Frame(self.forecastFrame,bg="#34ABCD")
        self.sundayFrame.pack(side=LEFT, padx=10) 

        self.sundayLbl = Label(self.sundayFrame, bg="#34ABCD", fg="#FFFFFF", text="", font=("bold", 15))
        self.sundayLbl.pack()

        self.sundayImg = Label(self.sundayFrame, bg="#34ABCD", image=None)
        self.sundayImg.pack()

        
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
            img = ImageTk.PhotoImage(image=Image.open(f"icons/{weather[5]}.png").resize((115, 115)))
            self.picture["image"] = img
            self.weatherLbl["text"] = f"Current Temperature: {round(weather[2])}°C, {weather[3]}"
            self.desc["text"] = f"{weather[4]}, feels like {round(weather[6])}°C"
            
            self.mondayFrame["highlightbackground"],self.mondayFrame["highlightthickness"] = "#FFFFFF",3
            self.mondayLbl["text"] = f"Mon: {round(weather[8])}°C"
            mondayPic = ImageTk.PhotoImage(image=Image.open(f"icons/{weather[15]}.png").resize((90, 90)))
            self.mondayImg["image"] = mondayPic

            self.tuesdayFrame["highlightbackground"],self.tuesdayFrame["highlightthickness"] = "#FFFFFF",3
            self.tuesdayLbl["text"] = f"Tue: {round(weather[9])}°C"
            tuesdayPic = ImageTk.PhotoImage(image=Image.open(f"icons/{weather[16]}.png").resize((90, 90)))
            self.tuesdayImg["image"] = tuesdayPic

            self.wednesdayFrame["highlightbackground"],self.wednesdayFrame["highlightthickness"] = "#FFFFFF",3
            self.wednesdayLbl["text"] = f"Wed: {round(weather[10])}°C"
            wednesdayPic = ImageTk.PhotoImage(image=Image.open(f"icons/{weather[17]}.png").resize((90, 90)))
            self.wednesdayImg["image"] = wednesdayPic

            self.thursdayFrame["highlightbackground"],self.thursdayFrame["highlightthickness"] = "#FFFFFF",3
            self.thursdayLbl["text"] = f"Thurs: {round(weather[11])}°C"
            thursdayPic = ImageTk.PhotoImage(image=Image.open(f"icons/{weather[18]}.png").resize((90, 90)))
            self.thursdayImg["image"] = thursdayPic
            
            self.fridayFrame["highlightbackground"],self.fridayFrame["highlightthickness"] = "#FFFFFF",3
            self.fridayLbl["text"] = f"Fri: {round(weather[12])}°C"
            fridayPic = ImageTk.PhotoImage(image=Image.open(f"icons/{weather[19]}.png").resize((90, 90)))
            self.fridayImg["image"] = fridayPic

            self.saturdayFrame["highlightbackground"],self.saturdayFrame["highlightthickness"] = "#FFFFFF",3
            self.saturdayLbl["text"] = f"Sat: {round(weather[13])}°C"
            saturdayPic = ImageTk.PhotoImage(image=Image.open(f"icons/{weather[20]}.png").resize((90, 90)))
            self.saturdayImg["image"] = saturdayPic

            self.sundayFrame["highlightbackground"],self.sundayFrame["highlightthickness"] = "#FFFFFF",3
            self.sundayLbl["text"] = f"Sun: {round(weather[14])}°C"
            sundayPic = ImageTk.PhotoImage(image=Image.open(f"icons/{weather[21]}.png").resize((90, 90)))
            self.sundayImg["image"] = sundayPic

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

        monday_temp = data['daily'][1]['temp']['day'] - 273.15
        monday_img = data['daily'][1]['weather'][0]['icon']

        tuesday_temp = data['daily'][2]['temp']['day'] - 273.15
        tuesday_img = data['daily'][2]['weather'][0]['icon']

        wednesday_temp = data['daily'][3]['temp']['day'] - 273.15
        wednesday_img = data['daily'][3]['weather'][0]['icon']

        thursday_temp = data['daily'][4]['temp']['day'] - 273.15
        thursday_img = data['daily'][4]['weather'][0]['icon']

        friday_temp = data['daily'][5]['temp']['day'] - 273.15
        friday_img = data['daily'][5]['weather'][0]['icon']

        saturday_temp = data['daily'][6]['temp']['day'] - 273.15
        saturday_img = data['daily'][6]['weather'][0]['icon']

        sunday_temp = data['daily'][7]['temp']['day'] - 273.15
        sunday_img = data['daily'][7]['weather'][0]['icon']

        desc = data['current']['weather'][0]['description']
        img = data['current']['weather'][0]['icon']

        return (city, country, temp, current_weather, desc, img, feels_like,
                weekly_forecast, monday_temp, tuesday_temp, wednesday_temp, thursday_temp, friday_temp, saturday_temp,
                sunday_temp, monday_img, tuesday_img, wednesday_img, thursday_img, friday_img, saturday_img, sunday_img)

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