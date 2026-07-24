# python task 4 weather app


import requests

# Enter your OpenWeatherMap API Key here
API_KEY = "62bf5a606d3d654b2dc336a2ba1d19a6"

# Ask the user to enter a city name
city = input("Enter city name: ")

# Check if the input is empty
if city.strip() == "":
    print("City name cannot be empty!")
    exit()

# API URL with city name and API key
url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"

try:
    # Send request to the weather API
    response = requests.get(url)

    # Convert response into JSON format
    data = response.json()

    # Check if request is successful
    if response.status_code == 200:

        # Display weather information
        print("\n------ Weather Report ------")
        print("City:", data["name"])
        print("Temperature:", data["main"]["temp"], "°C")
        print("Humidity:", data["main"]["humidity"], "%")
        print("Weather:", data["weather"][0]["description"])
        print("Wind Speed:", data["wind"]["speed"], "m/s")

    else:
        # Display API error message
        print("Error:", data.get("message", "Something went wrong"))

except requests.exceptions.RequestException:
    # Handle network-related errors
    print("Network Error! Please check your internet connection.")