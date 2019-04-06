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
    'source1':"The Wall Street Journal",
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
  	'source2':"The New York Times",
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