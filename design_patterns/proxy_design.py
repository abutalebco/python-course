import time

# API cache middleware system

class WeatherAPI:
    dt = {
        "Cairo": 2.33,
        "Alexandria": 1.22,
        "Portsaid": 1.66,
        "Rosetta": 2.71,
        "Tanta": 2.54,
        "Banha": 2.44,
        "Mansoura": 1.23,
        "Monofiya": 1.82
    }
    def get_temp(self, city: str) -> float:
        print(f"[API] fetching live temprature data for {city}")
        return self.dt[city]
    

class CachedWeatherProxy:
    TTL = 60 # time to live in seconds

    def __init__(self):
        self._api = WeatherAPI()
        self._cache = {}
    
    def get_temp(self, city: str) -> float:
        entry = self._cache.get(city)
        if entry and time.time() - entry["ts"] < self.TTL:
            print(f"[cache] hit for {city}")
            return entry["value"]
        
        temp = self._api.get_temp(city)
        self._cache[city] = {"value": temp, "ts": time.time()}
        return temp


api = CachedWeatherProxy()

print(api.get_temp("Cairo"))
print(api.get_temp("Portsaid"))
print(api.get_temp("Cairo"))
print(api.get_temp("Alexandria"))
print(api.get_temp("Banha"))
print(api.get_temp("Portsaid"))
print(api.get_temp("Alexandria"))