# https://github.com/Alp-0zturk/Weather_APP.git
import requests
import datetime
apikey:str = 'f6e2abf6d1b2b030187c12b6254c374c'

#import weather_UI as 
def get_weather_data(city):    #openweatherAPI
    weather_data = requests.get(f"https://api.openweathermap.org/data/2.5/weather?q={city}&units=metric&APPID={apikey}")
    if weather_data.json()['cod'] == '404':
        print("there is no such city bruh")
    else:
        weather:str = weather_data.json()['weather'][0]['main']
        temp:int = round(weather_data.json()['main']['temp'])
        name:str = weather_data.json()['name']
        humidity:int = round(weather_data.json()['main']['humidity'])
        desc:str = weather_data.json()['weather'][0]['description']
        feel:int = round(weather_data.json()['main']['feels_like'])
        
        return feel,desc,name,humidity,weather,temp

def main():
    city:str
    name:str
    humidity:int
    weather:str
    desc:str
    temp:int
    feel:int
    print("please insert city name")
    city:str = input()
    feel, desc,name, humidity, weather, temp = get_weather_data(city)
    print("location,city: ", city, "\t countryID: ", name)
    print("Weather status: ", weather, ",", desc)
    print("temperature: ",temp, "C")
    print("humidity: ", humidity)
    print("feel temp: ", feel)
    print("date: ",datetime.date.today())
    
if __name__ == "__main__":
    main()