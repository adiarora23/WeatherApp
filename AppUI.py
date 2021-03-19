from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk # Library used for handling images
from configparser import ConfigParser # Library used for config files
import requests # Library used to access web data
from typing import Tuple, Optional, Union # Library used for type hinting

################################ GUI Class ####################################
class WeatherApp:
    
    def __init__(self, api: str) -> None:
        self.root = Tk()
        self.root.geometry('375x450')
        self.root.configure(bg="#34ABCD")
        self.api = api
        self.initGUI()
        self.root.mainloop()
        
    def initGUI(self) -> None:
        self.cityName = StringVar()
        self.cityEntry = Entry(self.root, textvariable=self.cityName)
        self.cityEntry.pack()
        
        self.space = Label(self.root, bg="#34ABCD") # adds a space between the entry box and button
        self.space.pack()        
        
        self.searchBtn = Button(self.root, text="Search City", width=12, 
                                command=self.search)
        self.searchBtn.pack()
        
        self.space = Label(self.root, bg="#34ABCD") # adds a space between button and Location text
        self.space.pack()         
        
        self.locationLbl = Label(self.root, text="Location", bg="#34ABCD", 
                                 fg="#FFFFFF", font=("bold",24))
        self.locationLbl.pack()
        
        self.picture = Label(self.root, bg="#34ABCD", image=None)
        self.picture.pack()
        
        self.weatherLbl = Label(self.root, bg="#34ABCD", fg="#FFFFFF", 
                                text="", font=("bold",17))
        self.weatherLbl.pack()
        
        self.desc = Label(self.root, bg="#34ABCD", fg="#FFFFFF", text="", 
                          font=("bold",10))
        self.desc.pack()
        
    def search(self) -> None:
        city = self.cityName.get()
        weather = get_weather(city)
        
        if city == "":
            messagebox.showinfo(title=None, message="Please Enter a City")
        elif weather:
            self.locationLbl['text'] = f"{weather[0]}, {weather[1]}"
            img = ImageTk.PhotoImage(image=Image.open(f"icons/{weather[5]}.png").resize((115,115)))
            self.picture["image"] = img
            self.weatherLbl["text"] = f"{round(weather[2])}°C, {weather[3]}"
            self.desc["text"] = weather[4]
            self.root.mainloop()
        else:
            messagebox.showerror("Search Error", 
                                 f"Invalid input '{city}': city not found")

################################ Functions ####################################
def get_weather(city: str) -> Tuple[Optional[Union[str, float]]]: # returns a tuple containing strings and float
    data = requests.get(api_url.format(city, api_key))
    
    if data:
        data = data.json()
        city = data["name"]
        country = data["sys"]["country"]
        temp = data["main"]["temp"] - 273.15
        weather = data["weather"][0]["main"]
        desc = data["weather"][0]["description"]
        img = data["weather"][0]["icon"]
        
        return (city, country, temp, weather, desc, img)
        
    else:
        return None
    

if __name__ == "__main__":
    api_url = "https://api.openweathermap.org/data/2.5/weather?q={}&appid={}" # An exmple API I used; we can change this later
    file = "config.ini" # config file that contains the key to access the API data
    config = ConfigParser() # used to parse through config files
    config.read(file)
    api_key = config["testapi_key"]["key"] # gets the key for API from the file
    app = WeatherApp(api_url)