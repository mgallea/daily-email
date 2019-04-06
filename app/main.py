#import the required packages and modules
import requests
import os
from dotenv import load_dotenv
import sendgrid
from sendgrid.helpers.mail import *
from newsapi import NewsApiClient
import json
from functions import *

#Load the .env file with appropriate variables
load_dotenv()

SENDGRID_API_KEY = os.environ.get("SENDGRID_API_KEY", "OOPS, please set env var called 'SENDGRID_API_KEY'")
MY_EMAIL_ADDRESS = os.environ.get("MY_EMAIL_ADDRESS", "OOPS, please set env var called 'MY_EMAIL_ADDRESS'")
NEWS_API_KEY = os.environ.get("NEWS_API_KEY", "OOPS, please set env var called 'MY_EMAIL_ADDRESS'")
SENDGRID_TEMPLATE_ID = os.environ.get("SENDGRID_TEMPLATE_ID", "OOPS, please set env var called 'SENDGRID_TEMPLATE_ID'" )

#Authenticate into News API
newsapi = NewsApiClient(api_key=NEWS_API_KEY)

#Get Top Headlines
wsj_top_headlines = newsapi.get_top_headlines(sources='the-wall-street-journal')
nyt_top_headlines = newsapi.get_top_headlines(sources='the-new-york-times')

wTitle = FormatTopHeadlines(wsj_top_headlines,"title")
wBody = FormatTopHeadlines(wsj_top_headlines,"description")
wURL = FormatTopHeadlines(wsj_top_headlines, "url")
nTitle = FormatTopHeadlines(nyt_top_headlines,"title")
nBody = FormatTopHeadlines(nyt_top_headlines, "description")
nURL = FormatTopHeadlines(nyt_top_headlines, "url")



#Prepare the email
message = Mail(
    from_email = MY_EMAIL_ADDRESS,
    subject ='Daily Email Blast',
    to_emails = MY_EMAIL_ADDRESS
    )
message.dynamic_template_data ={
    'source1':'Test Publication',
  	'l-1':'http://google.com',
 	'h1-1':'Test Headline 1.1',
 	'b1-1':'Test Body 1.1',
  	'l-2':'http://google.com',
  	'h1-2':'Test Headline 1.2',
  	'b1-2':'Test Body 1.2',
  	'l-3':'http://google.com',
  	'h1-3':'Test Headline 1.3',
 	'b1-3':'Test Body 1.3',
  	'l-4':'http://google.com',
  	'h1-4':'Test Headline 1.4',
  	'b1-4':'Test Body 1.4',
  	'l-5':'http://google.com',
 	'h1-5':'Test Headline 1.5',
  	'b1-5':'Test Body 1.5'
    }
message.template_id = SENDGRID_TEMPLATE_ID

#Send the email
sendgrid_client = sendgrid.SendGridAPIClient(SENDGRID_API_KEY)
response = sendgrid_client.send(message)
print(response)


#from_email = Email(MY_EMAIL_ADDRESS)
#to_email = Email(MY_EMAIL_ADDRESS)
#subject = "Example Notification"
#message_text = 
#content = Content("text/plain", message_text)
#mail = Mail(from_email, subject, to_email, content)

#Send the email
#response = sg.client.mail.send.post(request_body=mail.get())