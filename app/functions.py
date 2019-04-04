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