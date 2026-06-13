import requests

class WeatherHandler:
    def __init__(self):
        self.base_url = "https://api.open-meteo.com/v1/forecast"
    
    def get_weather(self, latitude=40.7128, longitude=-74.0060):
        try:
            params = {
                "latitude": latitude,
                "longitude": longitude,
                "current": "temperature_2m,relative_humidity_2m,weather_code,wind_speed_10m",
                "temperature_unit": "celsius"
            }
            
            response = requests.get(self.base_url, params=params, timeout=5)
            response.raise_for_status()
            
            data = response.json()
            current = data.get("current", {})
            
            weather_description = self._get_weather_description(current.get("weather_code", 0))
            
            return {
                "temperature": current.get("temperature_2m", "N/A"),
                "humidity": current.get("relative_humidity_2m", "N/A"),
                "description": weather_description,
                "wind_speed": current.get("wind_speed_10m", "N/A")
            }
        except Exception as e:
            return {"error": f"Unable to fetch weather: {str(e)}"}
    
    def _get_weather_description(self, code):
        descriptions = {
            0: "Clear sky",
            1: "Mainly clear",
            2: "Partly cloudy",
            3: "Overcast",
            45: "Foggy",
            48: "Foggy",
            51: "Light drizzle",
            61: "Slight rain",
            80: "Slight rain showers",
            95: "Thunderstorm"
        }
        return descriptions.get(code, "Unknown conditions")
    
    def format_weather_response(self, weather_data):
        if "error" in weather_data:
            return weather_data["error"]
        
        temp = weather_data.get("temperature", "N/A")
        desc = weather_data.get("description", "Unknown")
        humidity = weather_data.get("humidity", "N/A")
        wind = weather_data.get("wind_speed", "N/A")
        
        return (f"Current conditions: {desc}. Temperature is {temp}°C. "
                f"Humidity at {humidity}%, wind speed {wind} km/h.")