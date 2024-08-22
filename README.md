# Weather App

This is a simple desktop application built with Python and Tkinter that fetches and displays the current weather information for a specified city using the OpenWeatherMap API.

## Features

- Fetch Weather Data: Enter the name of a city, and the app will display the current temperature, weather description, humidity, wind speed, and sea level pressure.
- Error Handling: Handles common errors like invalid city names or empty input with appropriate messages.
- Graphical User Interface (GUI): Built using Tkinter, providing a user-friendly interface.

## Usage

1. Clone the repository:

git clone https://github.com/mohammad-javad-0/weather-app.git
cd weather-app
2. Ensure you have installed the required packages:

3. Run the application:

python weather_app.py
4. Enter the name of the city in the input field and press the search button. The weather information will be displayed in a new window.

## Customization

- API Key: The app uses a default API key for OpenWeatherMap. If you want to use your own API key, replace the appid variable in the temperature_show function with your key.

appid = "your_api_key_here"
- Icons: The application uses custom icons for the window and buttons. You can replace these by providing your own image files in the image directory.
