#Format the top headlines into a more easily usable setup
def FormatTopHeadlines(top_headlines):
	articles = top_headlines['articles']
	headlines = []
	bodies = []
	urls = []
	i = 0
	for y in articles:
		article = articles[i]
		headline = article['title']
		body = article['description']
		url = article['url']
		headlines.append(headline)
		bodies.append(body)
		urls.append(url)
		i = i + 1
	return(headlines,bodies,urls)