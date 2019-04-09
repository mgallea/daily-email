#Format the top headlines into a more easily usable setup
def FormatTopHeadlines(top_headlines,component):
	articles = top_headlines['articles']
	components = []
	i = 0
	for y in articles:
		article = articles[i]
		#print(article['title'])
		typeVal = "title"
		components.append(article[component])
		i = i + 1
	return(components)

def KelvinToFahrenheit(temp_kelvin):
	tempFahrenheit = (temp_kelvin - 273) * 1.8 + 32
	tempFahrenheit = round(tempFahrenheit, 2)
	return tempFahrenheit

def TemperatureParser(full_weather_object):
	#Parse out the JSON Response
	fullWeather = full_weather_object.json()
	parsedWeather = fullWeather['list']
	dailyForcast = parsedWeather[0:11]
	
	#Calculate Min and Max Temps
	minTemp = []
	maxTemp = []
	y = 0

	for x in dailyForcast:
		minTemp.append(dailyForcast[y]['main']['temp_min'])
		maxTemp.append(dailyForcast[y]['main']['temp_max'])
		y = y + 1

	globalMinTemp = min(minTemp)
	globalMaxTemp = max(maxTemp)

	#Convert Kelvin Temperatures to Fahrenheit
	globalMaxTemp = KelvinToFahrenheit(globalMaxTemp)
	globalMinTemp = KelvinToFahrenheit(globalMinTemp)

	dailyTemperature = [globalMaxTemp, globalMinTemp]

	return dailyTemperature


