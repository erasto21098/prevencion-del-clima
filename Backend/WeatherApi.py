import requests


url_api_weather = "https://wttr.in/{location}?format=j1"

def get_ip_address():
    try:
        response = requests.get("https://api.ipify.org?format=json")
        response.raise_for_status()
        ip_data = response.json()
        return ip_data.get("ip", None)
    except requests.RequestException as e:
        print(f"????: {e}")
        return None

def get_ip_location(ip_address):
    try:
        response = requests.get(f"https://ipinfo.io/{ip_address}/json")
        response.raise_for_status()
        data = response.json()
        location = data.get("loc", "0,0").split(",")
        return {
            "latitud": float(location[0]),
            "longitud": float(location[1]),
            "ciudad": data.get("city", ""),
            "region": data.get("region", ""),
            "pais": data.get("country", "")
        }
    except requests.RequestException as e:
        print(f"????{e}")
        return None
    
def get_weather_by_location(location):
    try:
        response = requests.get(url_api_weather.format(location=location))
        response.raise_for_status()
        weather_data = response.json()
        return weather_data
    except requests.RequestException as e:
        print(f"???? {e}")
        return None