from app.functions import *
import requests
import os
from dotenv import load_dotenv
import sendgrid
from sendgrid.helpers.mail import *
from newsapi.newsapi_client import NewsApiClient
import json
import datetime
import pytest


CI_ENV = os.environ.get("CI", "OOPS") == "true" # expect default environment variable setting of "CI=true" on Travis CI, see: https://docs.travis-ci.com/user/environment-variables/#default-environment-variables
SKIP_REASON = "to avoid issuing requests from the CI server"

#Load from .env file
load_dotenv()
SENDGRID_API_KEY = os.environ.get("SENDGRID_API_KEY", "OOPS, please set env var called 'SENDGRID_API_KEY'")
MY_EMAIL_ADDRESS = os.environ.get("MY_EMAIL_ADDRESS", "OOPS, please set env var called 'MY_EMAIL_ADDRESS'")
NEWS_API_KEY = os.environ.get("NEWS_API_KEY", "OOPS, please set env var called 'NEWS_API_KEY'")
SENDGRID_TEMPLATE_ID = os.environ.get("SENDGRID_TEMPLATE_ID", "OOPS, please set env var called 'SENDGRID_TEMPLATE_ID'" )
OPENWEATHER_API_KEY = os.environ.get("OPENWEATHER_API_KEY", "OOPS, please set env var valled 'OPENWEATHER_API_KEY'")

def test_Kelvin():
	k = KelvinToFahrenheit(298)
	assert k == 77

@pytest.mark.skipif(CI_ENV==True, reason=SKIP_REASON)
def test_Get_Headlines():
	newsapi = NewsApiClient(api_key=NEWS_API_KEY)
	wsj_top_headlines = newsapi.get_top_headlines(sources='the-wall-street-journal')
	assert len(wsj_top_headlines) == 3