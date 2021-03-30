#object for validate methods

#i don't even think we need the folowing import statements, I just put them here jic loll we can take them out later
import pandas as pd   
import matplotlib.pyplot as plt 
import numpy as np
import random

class Validate: #we can add the method for mispelled city in this class when we get the time
    
    def __init__(self):
        pass
    
    def only_letters(self, char): #so far i've just coy and pasted the followung code from main.py
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
