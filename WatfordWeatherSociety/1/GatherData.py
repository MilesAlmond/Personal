from datetime import date, timedelta
from dateutil.relativedelta import *
import requests
import pandas as pd

first = today.replace(day=1)
lastMonthStart = first - relativedelta(months=1)
lastMonthEnd = first - timedelta(days=1)
lastMonthLength = (first - lastMonthStart).days

for i in range(0,lastMonthLength):
    url = "https://api.weatherbit.io/v2.0/history/daily?lat=USER_LATITUDEXXX&lon=USER_LONGITUDE&start_date={}&end_date={}&units=I&key=USER_KEYXXX".format(lastMonthStart,lastMonthStart+timedelta(days=1))

    res = requests.get(url)
    myData = res.json()
    data = myData[0]['data']

    avgTemp = data['temp']
    minTemp = data['min_temp']
    maxTemp = data['max_temp']
    totalPrecip = data['precip']
    avgPres = data['pres']


    weather = {'Date': [day_used],
            'AverageTemperature': [avgTemp],
            'MinTemperature': [minTemp],
            'MaxTemperature': [maxTemp],
            'TotalRainfall': [totalPrecip],
            'AveragePressure': [avgPres],
            }

    df = pd.DataFrame(weather, columns = ['Date','AverageTemperature',
                                        'MinTemperature','MaxTemperature',
                                        'TotalRainfall','AveragePressure'
                                        ])

    pd.DataFrame.to_csv(df,'USER_PATHXXX/WatfordWeatherSociety/1/Data/{}.csv'.format(lastMonthStart))
    lastMonthStart = lastMonthStart + timedelta(days=1)
