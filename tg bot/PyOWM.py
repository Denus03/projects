from pyowm import OWM

owm = OWM('c21634f76b5a9a6f1618d84281e65f38')
place = input("Введіть назву міста")
mgr = owm.weather_manager()
observation = mgr.weather_at_place('place')
w = observation.weather

t = w.temperature("celsius")
t1 = t['temp']
t2 = t['feels_like']
t3 = t['temp_max']
t4 = t['temp_min']

print(f"В місті {'place'} температура {t1}, відчувається як {t2}, максимальна {t3}, мінімальна {t4}")
