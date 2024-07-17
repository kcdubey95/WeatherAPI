
import aiohttp
from config import config

async def weather_api(location: str):
    url = f"http://api.weatherapi.com/v1/current.json?key={config.API_KEY}={location}&aqi=no"

    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            if response.status == 200:
                data = await response.json()
                return data
            else:
                response_text = await response.text()
                raise Exception(f"Error fetching data from weather API: {response.status}, {response_text}")
