from yaweather import Russia, YaWeather


def get_weather():
    y = YaWeather(api_key='ab6df7ab-f952-497a-98fe-93d3ef1d0b34')
    res = y.forecast(Russia.Moscow, lang="ru_RU")

    return f'Сейчас: {res.fact.temp} градусов, ощущается как {res.fact.feels_like} градусов' #, f'Небо: {res.fact.condition}'

# print(get_weather())
