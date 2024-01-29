from fastapi import FastAPI, HTTPException
import requests

app = FastAPI()

API_KEY = "38f9264b8e345e5059d64b5e08c19663"
BASE_URL = "http://api.openweathermap.org/data/2.5/weather?appid=" + API_KEY + "&q="

def get_weather_data(city):
    try:
        url = BASE_URL + city
        response = requests.get(url)
        response.raise_for_status() 
        weather_data = response.json()
        return weather_data
    except requests.RequestException as e:
        raise HTTPException(status_code=500, detail=f"Failed to retrieve weather data: {str(e)}")

@app.get("/weather/{city}")
async def read_weather(city: str):
    weather_data = get_weather_data(city)
    
    description = weather_data["weather"][0]["description"]
    temperature = weather_data["main"]["temp"]
    humidity = weather_data["main"]["humidity"]

    return {
        "description": description,
        "temperature": temperature,
        "humidity": humidity
    }
