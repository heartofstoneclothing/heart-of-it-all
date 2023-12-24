import requests

def get_weather(api_key, city):
    base_url = "http://api.openweathermap.org/data/2.5/weather"
    params = {
        "q": city,
        "appid": api_key,
        "units": "metric"  # You can change this to "imperial" for Fahrenheit
    }

    response = requests.get(base_url, params=params)

    if response.status_code == 200:
        data = response.json()
        return data
    else:
        print(f"Error fetching weather data for {city}")
        print(response.text)  # Print the response content for debugging
        return None

def display_weather(data):
    if data:
        print(f"Weather in {data['name']}, {data['sys']['country']}:")
        print(f"Temperature: {data['main']['temp']}°C")
        print(f"Description: {data['weather'][0]['description']}")
        print(f"Humidity: {data['main']['humidity']}%")
        print(f"Wind Speed: {data['wind']['speed']} m/s")
    else:
        print("Weather data not available.")

if __name__ == "__main__":
    api_key = "d2ce2fc9b602c9e1e5f78c495ad47572"
    city = input("Enter city name: ")

    weather_data = get_weather(api_key, city)

    display_weather(weather_data)
