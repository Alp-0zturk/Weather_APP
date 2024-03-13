import requests_cache
import pandas as pd
import time
from retry_requests import retry
from openmeteo_requests import Client
from requests.adapters import HTTPAdapter
from geopy.geocoders import Nominatim
from requests.packages.urllib3.util.retry import Retry
geolocator = Nominatim(user_agent="MyApp")

#import weather_UI as w_UI
def get_weather_data(lat, lon):    #open-meteo API  # PART2
    url = "https://api.open-meteo.com/v1/forecast"
    params = {
	"latitude": lat,
	"longitude": lon,
    }
    try:
        responses = openmeteo.weather_api(url, params=params)
        response = responses[0]
    except Exception as e:
        print(f"Error fetching weather data: {e}")
        return None
    
    retry_strategy = Retry(
    total=5,
    backoff_factor=0.2,
    status_forcelist=[429, 500, 502, 503, 504],
    method_whitelist=["GET"],
    )
    adapter = HTTPAdapter(max_retries=retry_strategy)
    retry_session = requests_cache.CachedSession('.cache', expire_after=3600)
    retry_session.mount("https://", adapter)
    openmeteo = Client(session=retry_session)

def get_hourly_temperature(lat, lon):
    url = "https://api.open-meteo.com/v1/forecast"
    params = {
        "latitude": lat,
        "longitude": lon,
    }
    for i in range(5):  # Retry 5 times
        try:
            cache_session = requests_cache.CachedSession('.cache', expire_after=3600)
            retry_session = retry(cache_session, retries=5, backoff_factor=0.2)
            openmeteo = Client(session=retry_session)
            responses = openmeteo.weather_api(url, params=params)

        # Process first location. Add a for-loop for multiple locations or weather models
            response = responses[0]

        # Check if the response has the attribute 'hourly_data'
            if hasattr(response, 'hourly_data'):
                hourly_temperatures = response.hourly_data('temperature_2m')
                # Print hourly temperature data
                for hour, temp in hourly_temperatures.items():
                    print(f"Hour: {hour}, Temperature: {temp}°C")
                    break  # If the request is successful, break the loop
            else:
                print("The response object does not have the 'hourly_data' attribute.")
        except:
            time.sleep(5)

def cityToCOORD(city):
    location = geolocator.geocode(city)
    lat:float = location.latitude
    lon:float = location.longitude
    address:str = location
    return lat, lon, address

def main():
    print("please enter a city name to get live weather data")
    city:str = input()
    lat:float
    lon:float
    address:str
    lat, lon, address = cityToCOORD(city)
    lat = round(lat, 2)
    lon = round(lon, 2)
    print("address:\n", address, "\n", "latitude:\n", lat, "°N\n", "longitude:\n", lon, "°E\n")

    weather_data = get_weather_data(lat, lon)
    temper = get_hourly_temperature(lat, lon)
    print("The address:", "\n", address)
    print(weather_data)
    print(temper)

if __name__ == "__main__":
    main()