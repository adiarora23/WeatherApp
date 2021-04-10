# WeatherApp #

A Weather Application that displays the current weather and 7-day forecast of the user's city of choice (limited to Ontario cities only).

# Table of Contents #

* [Dependencies](#dependencies)
* [Important](#important)
* [Installation](#installation)
* [Documentation](#documentation)
* [Addendums](#addendums)
* [References](#references)

# Dependencies: #
In order to use our weather application, you will need to install/import the following programs/modules:
- Python 3.6 or above
- TKinter package
- pytz package
- time module
- PIL package
- requests package
- typing module
- datetime module
- pickle module
- json package
- configparser module
- pandas module
- matplotlib package

# Important: #

This weather application only works and runs with the following combinations:

Windows:
- IDLE
- PyCharm

macOS:
- IDLE
- PyCharm
- Wing

(Due to some unknown issue, the Windows version of Wing IDE DOES NOT allow our application to run.)

# Installation: #

1. Install Python from [here](https://www.python.org/downloads/). You may skip this step if you already have Python 3.6 or above installed

2. Click on the green button that says "Code"

3. Click on "Download ZIP"

4. Extract the ZIP folder to some directory in your computer

5. Click on the main.py file and run it

When you run the application, you will be greeted with a welcome window with the ability to type in an Ontario city.

### How To Use ###

* Use the mouse to click on the welcome window entry, and use the keyboard to type in an Ontario city.
* Use the "Actions" bar at the top to display options you can use.
* "Change Unit" will allow you to display the weather degrees in either Celsius or Fahrenheit.
* "Display Graph" will allow you to choose between either seeing a general temperature graph of the city you chose, or a specific graph based on your choice.
* "Find Another City" allows you to search for another Ontario city of your choice.
* "Search History" displays the search history of Ontario cities you entered.
* "Save" allows you to save information of the current weather in a .txt file.
* "Quit" allows you to quit the application.

# Documentation: #

### Code Documentation: ###

#### `AppUI.py` ####
The `AppUI.py` file consists of all the GUI components visible to the user. This includes the starting frame, the main frame, and the graphs being displayed on screen.

The `AppUI.py` file also contains helper functions that pull the weather data from the API used, which is then assigned to specific values that are used for the main frame.

#### `canada_cities.py` ####
The `canada_cities.py` file takes all the cities of the world pulled from the API and filters them down to Ontario cities only.

The first loop goes through all cities and filters the cities down to Canada-only cities, then the second loop filters it down further to Ontario-only cities.

#### `city.list.json` ####
The `city.list.json` file contains all the cities across the world from the API, but in a json format (used for `canada_cities.py`).

#### `config.ini` ####
The `config.ini` file contains the API key. 

This is used in the API URL to collect real-time data for the current and 7-day forecast of the city you want.

#### `graph.py` ####
The `graph.py` file consists of all the graph functions that are used in `AppUI.py` in order to show the graphs of your choice.

This file consists of three functions: 
1. The data_frame function which is used to grab all the data from the API and turn it into a dataframe for plotting graphs
2. The chart_temp_overview function which is used to display the general temperature overview of the city of choice
3. The custom function which is used ot display the specific graph of the your choice

#### `history.pkl` ####
The `history.pkl` file contains the history of cities searched for on the application (stored in this file).

#### `main.py` ####
The `main.py` file is used to run the entire application.

#### `icons` ####
The `icons` folder contains all the icons used for both the starting frame and the main frame.

These icons can be found on the same website used for our API (link will be in code comments).


# Addendums: #

### Aditya Arora: ###

For this project, I worked with Muhammad, Justin and Isha to help setup the application (specifically, extracting the correct API data needed for this app), as well as handle most of the documentation needed (includes README.md file). I also contributed to the project by maintaining the Github repo to limit merge conflict issues, along with using the API data to display the 7-day weather on the main GUI. 

### Muhammad Hassan: ###

For this project, I teamed up with Aditya, Justin and Isha to create a Weather App, which provides weather information for cities across Ontario. When it comes to individual contribution, I helped with setting up the API, and setting the layouts of AppUI and the welcome window. I also contributed to adding the persistence element (history.pkl). In general, I worked mostly with the API data and the main GUI of the app.

### Justin Sousa: ###

For this project, I changed the overall UI from different roots to all seperate frames. Along side with that I worked with Muhammed and Aditya in the overall UI of the application. In terms of UI, I completed the welcome screen, setting up the menus as there were some problems with that. Also general error checking, primarily in the search function, and passing data between the two frames. 

### Isha Joshi: ###

(TODO: add addendum)

# References: #

All references that were used for this project can be found in the `.py` files of this repository (written with comments `#`). 
