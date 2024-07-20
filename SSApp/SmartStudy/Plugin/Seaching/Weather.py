import requests

def weather(city):
        text = city
        try:
            if city.lower() in ["phan rang", "phan rang tháp chàm"]:
                city, text = ["phan rang - tháp chàm"]*2
            elif city.lower() in ["sài gòn", "sai gon", "saigon"]:
                city = "saigon"  #ở đây bằng "ho chi minh" được nhé!
                text = "thành phố - hồ chí minh"
            else:
                city = city.replace(' ', '%20')

            api_weather = requests.get(
            f'https://api.openweathermap.org/data/2.5/weather?q={city.lower()}&units=metric&appid=a0999c58e5d99ab8bed47d4119f5f099'
            ).json()

            dic_weather = {"Rain": "Mưa", "Clouds": "Có mây", "Sunny": "Nắng", "clear sky": "Yên tĩnh"}
            weather = dic_weather.get(api_weather['weather'][0]['main'])
            nhiet_do = api_weather["main"]["temp"]
            do_am = api_weather["main"]["humidity"]
            wind_speed = f'{round(float(api_weather["wind"]["speed"])/3.6, 2)} (km/h)'
            wind_gust = "(không có)" if len(
            api_weather["wind"]
            ) < 3 else f'{round(float(api_weather["wind"]["gust"])/3.6,2)} (km/h)'
            clouds = int(api_weather["clouds"]["all"])

            data = {
                'weather': weather, # thời tiết hiện tại
                'temperature': nhiet_do, # nhiệt độ
                'humidity': do_am, # độ ẩm
                'wind_speed': wind_speed, # tốc độ gió
                'wind_gust': wind_gust, # giật tốc độ gió lên 
                'cloud_density': clouds, #mật độ mây
            }
            return data
        
        except:
            return

def content(city:str) -> str|None:
    data = weather(city=city)
    if data:

        return f'''◆ Dự báo thời tiết ở {city.title()} là:
        - Thời tiết: {data['weather']}
        - Nhiệt độ: {data['temperature']}°C
        - Tốc độ gió: {data['wind_speed']} 
            → Có thể giật: {data['wind_gust']}
        - Độ ẩm: {data['humidity']}%
        - Mật độ mây: {data['cloud_density']}% '''
    return

            