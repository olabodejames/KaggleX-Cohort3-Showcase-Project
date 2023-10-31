import pprint
import requests


secret = "e7a28541b2574b2096f501f9d03ebabf"

# Define the endpoint
url = 'https://newsapi.org/v2/everything?'

# Specify the query and
# number of returns
parameters = {
	'q': 'nigeria', # query phrase
	'pageSize': 100, # maximum is 100
	'apiKey': secret # your own API key
}

# Make the request
response = requests.get(url,
						params = parameters)

# Convert the response to
# JSON format and pretty print it
response_json = response.json()
pprint.pprint(response_json)
