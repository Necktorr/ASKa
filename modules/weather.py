from yaweather import UnitedKingdom, YaWeather


y = YaWeather(api_key='ab6df7ab-f952-497a-98fe-93d3ef1d0b34')
res = y.forecast(UnitedKingdom.London)


f1 = (f'Now: {res.fact.temp} °C, feels like {res.fact.feels_like} °C')
f2 = (f'Condition: {res.fact.condition}')
print (f1, f2)