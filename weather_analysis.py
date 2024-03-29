#from retry_requests import retry
#from geopy.geocoders import Nominatim
import requests
import datetime

#geolocator = Nominatim(user_agent="MyApp")
apikey:str = 'f6e2abf6d1b2b030187c12b6254c374c'

#import weather_UI as w_UI
def get_weather_data(city):    #openweatherAPI  #PART2
    weather_data = requests.get(f"https://api.openweathermap.org/data/2.5/weather?q={city}&units=metric&APPID={apikey}")
    if weather_data.json()['cod'] == '404':
        print("there is no such city bruh")
    else:
        weather:str = weather_data.json()['weather'][0]['main']
        temp:int = round(weather_data.json()['main']['temp'])
        #humidity = round(weather_data.json()['main']['json'])
        return weather,temp
'''
def cityToCOORD(city): #part 1
    location = geolocator.geocode(city)
    lat:float = location.latitude
    lon:float = location.longitude
    address:str = location
    return lat, lon, address '''

def main():
    print("please enter a city name to get live weather data")
    city:str = input()
    '''
    lat:float
    lon:float  
    lat, lon, address = cityToCOORD(city)'''
    
    address:str
    weather:str
    temp:int
    
    address, weather, temp = get_weather_data(city)
    print("address: ", address)
    print("Weather status: ", weather)
    print("temperature: ",temp)
    
if __name__ == "__main__":
    main()
