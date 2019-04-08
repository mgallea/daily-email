#import the required packages and modules
import requests
import os
from dotenv import load_dotenv
import sendgrid
from sendgrid.helpers.mail import *
from newsapi import NewsApiClient
import json
from functions import *
import datetime

#Load the .env file with appropriate variables
load_dotenv()

SENDGRID_API_KEY = os.environ.get("SENDGRID_API_KEY", "OOPS, please set env var called 'SENDGRID_API_KEY'")
MY_EMAIL_ADDRESS = os.environ.get("MY_EMAIL_ADDRESS", "OOPS, please set env var called 'MY_EMAIL_ADDRESS'")
NEWS_API_KEY = os.environ.get("NEWS_API_KEY", "OOPS, please set env var called 'MY_EMAIL_ADDRESS'")
SENDGRID_TEMPLATE_ID = os.environ.get("SENDGRID_TEMPLATE_ID", "OOPS, please set env var called 'SENDGRID_TEMPLATE_ID'" )
OPENWEATHER_API_KEY = os.env.get("OPENWEATHER_API_KEY", "OOPS, please set env var valled 'OPENWEATHER_API_KEY'")

#Authenticate into News API
newsapi = NewsApiClient(api_key=NEWS_API_KEY)

#Get the current date
now = datetime.datetime.now()
day = now.day
month = now.month
year = now.year
date = str(year) + "-" + str(month) + "-" + str(day)

#Get Top Headlines
wsj_top_headlines = newsapi.get_top_headlines(sources='the-wall-street-journal')
nyt_top_headlines = newsapi.get_top_headlines(sources='the-new-york-times')
donald_top_headlines = newsapi.get_top_headlines(q='Donald Trump')

wTitle = FormatTopHeadlines(wsj_top_headlines,"title")
wBody = FormatTopHeadlines(wsj_top_headlines,"description")
wURL = FormatTopHeadlines(wsj_top_headlines, "url")
nTitle = FormatTopHeadlines(nyt_top_headlines,"title")
nBody = FormatTopHeadlines(nyt_top_headlines, "description")
nURL = FormatTopHeadlines(nyt_top_headlines, "url")
dTitle = FormatTopHeadlines(donald_top_headlines,"title")
dBody = FormatTopHeadlines(donald_top_headlines, "description")
dURL = FormatTopHeadlines(donald_top_headlines, "url")


#Get Weather Data

#Prepare the email
message = Mail(
    from_email = MY_EMAIL_ADDRESS,
    subject ='Daily Email Blast',
    to_emails = MY_EMAIL_ADDRESS
    )
message.dynamic_template_data ={
    'source1':"THE WALL STREET JOURNAL",
  	'l1-1': wURL[0],
 	'h1-1': wTitle[0],
 	'b1-1': wBody[0],
  	'l1-2': wURL[1],
  	'h1-2': wTitle[1],
  	'b1-2': wBody[1],
  	'l1-3': wURL[2],
  	'h1-3': wTitle[2],
 	'b1-3': wBody[2],
  	'l1-4': wURL[3],
  	'h1-4': wTitle[3],
  	'b1-4': wBody[3],
  	'l1-5': wURL[4],
 	'h1-5': wTitle[4],
  	'b1-5': wBody[4],
  	'source2':"THE NEW YORK TIMES",
  	'l2-1': nURL[0],
 	'h2-1': nTitle[0],
 	'b2-1': nBody[0],
  	'l2-2': nURL[1],
  	'h2-2': nTitle[1],
  	'b2-2': nBody[1],
  	'l2-3': nURL[2],
  	'h2-3': nTitle[2],
 	'b2-3': nBody[2],
  	'l2-4': nURL[3],
  	'h2-4': nTitle[3],
  	'b2-4': nBody[3],
  	'l2-5': nURL[4],
 	'h2-5': nTitle[4],
  	'b2-5': nBody[4],
  	'source3':'WHAT DID TRUMP DO THIS TIME?',
  	'l3-1': dURL[0],
 	'h3-1': dTitle[0],
 	'b3-1': dBody[0],
  	'l3-2': dURL[1],
  	'h3-2': dTitle[1],
  	'b3-2': dBody[1],
  	'l3-3': dURL[2],
  	'h3-3': dTitle[2],
 	'b3-3': dBody[2],
  	'l3-4': dURL[3],
  	'h3-4': dTitle[3],
  	'b3-4': dBody[3],
  	'l3-5': dURL[4],
 	'h3-5': dTitle[4],
  	'b3-5': dBody[4],
    }
message.template_id = SENDGRID_TEMPLATE_ID

#Send the email
sendgrid_client = sendgrid.SendGridAPIClient(SENDGRID_API_KEY)
response = sendgrid_client.send(message)


#print(response)
#from_email = Email(MY_EMAIL_ADDRESS)
#to_email = Email(MY_EMAIL_ADDRESS)
#subject = "Example Notification"
#message_text = 
#content = Content("text/plain", message_text)
#mail = Mail(from_email, subject, to_email, content)

#Send the email
#response = sg.client.mail.send.post(request_body=mail.get())