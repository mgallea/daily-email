from app.functions_file import *
from app.main import (
	SENDGRID_API_KEY,
	MY_EMAIL_ADDRESS,
	NEWS_API_KEY,
	SENDGRID_TEMPLATE_ID,
	OPENWEATHER_API_KEY
	)
from newsapi.newsapi_client import NewsApiClient

CI_ENV = os.environ.get("CI", "OOPS") == "true" # expect default environment variable setting of "CI=true" on Travis CI, see: https://docs.travis-ci.com/user/environment-variables/#default-environment-variables
SKIP_REASON = "to avoid issuing requests from the CI server"
	

def test_Kelvin():
	k = KelvinToFahrenheit(298)
	assert k == 77

@pytest.mark.skipif(CI_ENV==True, reason=SKIP_REASON)
def test_Get_Top_Headlines():
	newsapi = NewsApiClient(api_key=NEWS_API_KEY)
	wsj_top_headlines = newsapi.get_top_headlines(sources='the-wall-street-journal')
	assert len(wsj_top_headlines) == 3