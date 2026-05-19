from flask import Flask, request
import requests
from datetime import datetime

app = Flask(__name__)

user_api = "YOUR_API_KEY"

@app.route('/')
def home():

    location = request.args.get('city')

    if not location:
        return '''
        <h2>Weather App</h2>

        <form>
            <input type="text" name="city" placeholder="Enter city name">
            <button type="submit">Get Weather</button>
        </form>
        '''

    complete_api_link = "https://api.openweathermap.org/data/2.5/weather?q=" + location + "&appid=" + user_api

    api_link = requests.get(complete_api_link)
    api_data = api_link.json()

    if api_data['cod'] == '404':
        return f"Invalid City: {location}"

    temp_city = ((api_data['main']['temp']) - 273.15)
    weather_desc = api_data['weather'][0]['description']
    hmdt = api_data['main']['humidity']
    wind_spd = api_data['wind']['speed']

    date_time = datetime.now().strftime("%d %b %Y | %I:%M:%S %p")

    return f"""
    <pre>
-------------------------------------------------------------
Weather Stats for - {location.upper()} || {date_time}
-------------------------------------------------------------

Current temperature is: {temp_city:.2f} deg C
Current weather desc  : {weather_desc}
Current Humidity      : {hmdt} %
Current wind speed    : {wind_spd} kmph
    </pre>

    <a href="/">Search Again</a>
    """

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
