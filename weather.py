import requests

#Ask for a city name
city_name = input("Enter the City name:  ".capitalize())

# Define your API key
api = "your API key"

# Make the API request
s_request = requests.get(
    f"https://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={api}&units=metric"
)
s_request = s_request.json()  # Convert JSON response to dictionary

# Extract relevant data
country = s_request['sys']['country']  
city = s_request['name']
temp = s_request['main']['temp']
wind = s_request['wind']['speed']
weather = s_request['weather'][0]['description']

# Print results
print(f"Country name  : {country}")
print(f"City name     : {city}")
print(f"Temperature   : {temp} °C")
print(f"Wind speed    : {wind} km/h")
print(f"Weather       : {weather.capitalize()}")
