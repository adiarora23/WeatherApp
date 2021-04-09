from configparser import ConfigParser  # module used for reading config files
from AppUI import WeatherApp  # import GUI


# ------------------------- Main Loop -------------------------------
if __name__ == "__main__":
    api_url = "https://api.openweathermap.org/data/2.5/onecall?lat={}&lon={}&exclude=minutely,hourly&appid={}"  # api link to search by latitude and longitude
    file = "config.ini"  # config file that contains the key to access the API data
    config = ConfigParser()  # used to parse through config files
    config.read(file)
    api_key = config["testapi_key"]["key"]  # gets the key for API from the file
    app = WeatherApp(api_url, api_key)