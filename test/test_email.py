from app.functions import *

def test_Kelvin():
	k = KelvinToFahrenheit(298)
	assert k == 77