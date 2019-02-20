import requests
import  os


class weather:
    def __init__(self, city):
        self.city_name = city
        self.api_url = 'http://api.openweathermap.org/data/2.5/weather'
        self.appid = '68883ee95492b1c8af099d173269dea6'

    def weather(self):
        response = requests.get(url=self.api_url, params=dict(q=self.city_name, APPID=self.appid))
        self.weather_data = response.json()

        if self.weather_data["cod"] != "404":
            temp_key = self.weather_data["main"]
            self.current_temperature = temp_key["temp"]

            self.current_pressure = temp_key["pressure"]

            self.current_humidiy = temp_key["humidity"]

            weather_key = self.weather_data["weather"]
            self.weather_description = weather_key[0]["description"]

            weather.weather_info(self)   # call to weather info function to print weather
        else:
            print("*********************************************************")
            print("Your Location cannot be found!")
            print("********************* NEXT ENTRY ************************")


    def weather_info(self):
        file = open("weather.txt", "w+")
        msg = ("*********************************************************"
            + "\n City name = "
            + str(self.city_name)
            +  "\n Temperature (in kelvin unit) = "
            +  str(self.current_temperature)
            + "\n atmospheric pressure (in hPa unit) = "
            +  str(self.current_pressure)
            + "\n humidity (in percentage) = "
            +  str(self.current_humidiy)
            +  "\n description = "
            +  str(self.weather_description)
            +  "\n********************* NEXT ENTRY ************************")
        file.write(msg)
        file.close()
        print(msg)



def main():
    while(True):
        city_name = input("Enter city name:")
        location_weather = weather(city_name)
        location_weather.weather()              # call to find the weather

if __name__ == "__main__":
   try:
      main()
   except KeyboardInterrupt:
      # do nothing here
      print("\nProgram exited Sucessfully!")
      pass