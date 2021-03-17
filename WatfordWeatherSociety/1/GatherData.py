from datetime import date, timedelta
from dateutil.relativedelta import *
import requests
import pandas as pd

day_used = date.today() - timedelta(days=2)
#
# year = yesterday.timetuple().tm_year
# month = yesterday.timetuple().tm_mon
# day = yesterday.timetuple().tm_mday
#
# epoch_raw = datetime(year,month,day, 0, 0).timestamp()
# epoch = int(epoch_raw)

# first = today.replace(day=1)
# lastMonthStart = first - relativedelta(months=1)
# lastMonthEnd = first - timedelta(days=1)
# lastMonthLength = (first - lastMonthStart).days

# for i in range(0,lastMonthLength):
# #     url_old = "https://api.weatherbit.io/v2.0/history/daily?lat=51.6734&lon=-0.3911&start_date={}&end_date={}&units=I&key=b2a3acc2c23a4110a0cde018ac1a0966".format(lastMonthStart,lastMonthStart+timedelta(days=1))
#
# # url = "http://api.openweathermap.org/data/2.5/onecall/timemachine?lat=51.6734&lon=-0.3911&dt={}&units=imperial&appid=dc96d3a04813a5bb71329a37bab2fa13".format(epoch)
#
#     url = "https://weather.visualcrossing.com/VisualCrossingWebServices/rest/services/weatherdata/history?&aggregateHours=24&startDateTime={}T00:00:00&endDateTime={}T00:00:00&unitGroup=us&contentType=json&dayStartTime=0:0:00&dayEndTime=0:0:00&location=Watford,UK&key=IC3EZ9NFUC13XYDLW40Y6P4FZ".format(lastMonthStart,lastMonthStart+timedelta(days=1))
#     url = "https://weather.visualcrossing.com/VisualCrossingWebServices/rest/services/weatherdata/history?&aggregateHours=1&startDateTime=2020-12-04T00:00:00&endDateTime=2020-12-05T00:00:00&unitGroup=us&contentType=json&dayStartTime=0:0:00&dayEndTime=0:0:00&location=London,UK&key=IC3EZ9NFUC13XYDLW40Y6P4FZ"

url = "http://api.weatherapi.com/v1/history.json?key=1d4a51e5d61e4b9da91235603200612&q=51.6734,-0.3911&dt={}".format(day_used)

res = requests.get(url)
myData = res.json()
data = myData['forecast']['forecastday'][0]['day']
data_hour = myData['forecast']['forecastday'][0]['hour']

pres = []

for i in range(0,24):
    pres.append(data_hour[i]['pressure_mb'])

avgTemp = data['avgtemp_f']
minTemp = data['mintemp_f']
maxTemp = data['maxtemp_f']
totalPrecip = data['totalprecip_in']
avgPres = sum(pres)/len(pres)


# avgTemp = data['temp']
# minTemp = data['min_temp']
# maxTemp = data['max_temp']
# totalPrecip = data['precip']
# avgPres = data['pres']
#
#
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

pd.DataFrame.to_csv(df,'C:/Users/Alison/Documents/WatfordWeatherSociety/1/Data/{}.csv'.format(day_used))
# lastMonthStart = lastMonthStart + timedelta(days=1)
