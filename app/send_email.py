#import the required packages and modules
import requests
import os
from dotenv import load_dotenv
import sendgrid
from sendgrid.helpers.mail import *
from newsapi import NewsApiClient
import json

#Load the .env file with appropriate variables
load_dotenv()

SENDGRID_API_KEY = os.environ.get("SENDGRID_API_KEY", "OOPS, please set env var called 'SENDGRID_API_KEY'")
MY_EMAIL_ADDRESS = os.environ.get("MY_EMAIL_ADDRESS", "OOPS, please set env var called 'MY_EMAIL_ADDRESS'")
NEWS_API_KEY = os.environ.get("NEWS_API_KEY", "OOPS, please set env var called 'MY_EMAIL_ADDRESS'")

#Authenticate into News API
newsapi = NewsApiClient(api_key=NEWS_API_KEY)

#Get Top Headlines
wsj_top_headlines = newsapi.get_top_headlines(sources='the-wall-street-journal')

#Format News Articles
wsjArticles = wsj_top_headlines['articles']
wsjHeadlines = []
wsjBody = []
wsjURL = []
i=0
for y in wsjArticles:
	article = wsjArticles[i]
	headline = article['title']
	body = article['description']
	url = article['url']
	wsjHeadlines.append(headline)
	wsjBody.append(body)
	wsjURL.append(url)
	print("* " + headline)
	print("      " + body)
	print("      " + url)
	print("")
	i = i+1
#print(wsjHeadlines)

#Authenticate into Sendgrid
sg = sendgrid.SendGridAPIClient(apikey=SENDGRID_API_KEY)

#Prepare the email
from_email = Email(MY_EMAIL_ADDRESS)
to_email = Email(MY_EMAIL_ADDRESS)
subject = "Example Notification"
message_text = str(wsj_top_headlines)
content = Content("text/plain", message_text)
mail = Mail(from_email, subject, to_email, content)

#Send the email
#response = sg.client.mail.send.post(request_body=mail.get())