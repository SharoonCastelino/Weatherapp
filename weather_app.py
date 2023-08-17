# weather_app.py
import requests

def get_weather(api_key, city):
    base_url = "http://api.openweathermap.org/data/2.5/weather"
    params = {
        "q": city,
        "appid": api_key,
        "units": "metric"  # Use "imperial" for Fahrenheit
    }

    response = requests.get(base_url, params=params)
    data = response.json()

    if data["cod"] == 200:
        weather_description = data["weather"][0]["description"]
        temperature = data["main"]["temp"]
        humidity = data["main"]["humidity"]
        return f"Weather in {city}: {weather_description}\nTemperature: {temperature}°C\nHumidity: {humidity}%"
    else:
        return "City not found."

def main():
    api_key = "317a3a0d5f61685551a7760b2b7a3bcd"  # Replace with your OpenWeatherMap API key
    city = input("Enter city name: ")
    weather_info = get_weather(api_key, city)
    print(weather_info)

if __name__ == "__main__":
    main()
