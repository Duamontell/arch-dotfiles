#!/usr/bin/env python3
import json
import urllib.request

WEATHER_ICONS = {
    "113": "󰖙", # Ясно
    "116": "󰖕", # Переменная облачность
    "119": "󰖐", # Облачно
    "122": "󰖐", # Пасмурно
    "143": "󰖑", # Туман
    "248": "󰖑",
    "260": "󰖑",
    "176": "󰖖", # Небольшой дождь
    "293": "󰖖",
    "296": "󰖖",
    "302": "󰖖",
    "308": "󰖖",
    "200": "󰙾", # Гроза
    "386": "󰙾",
    "389": "󰙾",
    "227": "󰼶", # Снег
    "326": "󰼶",
    "332": "󰼶",
}

def get_weather():
    try:
        # Укажите ваш город вместо пустой строки, например: wttr.in/Moscow?format=j1
        url = "https://wttr.in/?format=j1"
        req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
        with urllib.request.urlopen(req, timeout=5) as response:
            data = json.loads(response.read().decode('utf-8'))

        current = data['current_condition'][0]
        temp = current['temp_C']
        code = current['weatherCode']
        desc = current['weatherDesc'][0]['value']
        feels = current['FeelsLikeC']
        humidity = current['humidity']
        wind = current['windspeedKmph']

        icon = WEATHER_ICONS.get(code, "󰖐")
        
        # Отображаемый текст в Waybar
        text = f"{icon}  {temp}°C"
        
        # Подробности при наведении курсора
        tooltip = (
            f"<b>{desc}</b>\n"
            f"Ощущается как: {feels}°C\n"
            f"Влажность: {humidity}%\n"
            f"Ветер: {wind} км/ч"
        )

        return json.dumps({"text": text, "tooltip": tooltip})
    except Exception:
        # Fallback при отсутствии интернета
        return json.dumps({"text": "󰖐 --°C", "tooltip": "Погода недоступна"})

if __name__ == "__main__":
    print(get_weather())
