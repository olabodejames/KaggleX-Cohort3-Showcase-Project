import pprint
import requests
from wordcloud import WordCloud
import matplotlib.pyplot as plt

secret = "e7a28541b2574b2096f501f9d03ebabf"

# Define the endpoint
url = 'https://newsapi.org/v2/everything?'

# Specify the query and
# number of returns
parameters = {
	'q': 'spain', # query phrase
	'pageSize': 100, # maximum is 100
	'apiKey': secret # your own API key
}

text_combined = ''

# Make the request
response = requests.get(url,
						params = parameters)

# Convert the response to
# JSON format and pretty print it
response_json = response.json()
pprint.pprint(response_json)

for i in response_json['articles']:

	if i['description'] != None:
		text_combined += i['description'] + ' '

wordcount={}
for word in text_combined.split():
	if word not in wordcount:
		wordcount[word] = 1
	else:
		wordcount[word] += 1

# initializing bad_chars_list
bad_words = ["a", "the" , "of", "in", "to", "and", "on", "de", "with",
			"by", "at", "dans", "ont", "été", "les", "des", "au", "et",
			"après", "avec", "qui", "par", "leurs", "ils", "a", "pour",
			"les", "on", "as", "france", "eux", "où", "son", "le", "la",
			"en", "with", "is", "has", "for", "that", "an", "but", "be",
			"are", "du", "it", "à", "had", "ist", "Der", "um", "zu", "den",
			"der", "-", "und", "für", "Die", "von", "als",
			"sich", "nicht", "nach", "auch" ]


r = text_combined.replace('\s+',
						' ').replace(',',
									' ').replace('.',
													' ')
words = r.split()
rst = [word for word in words if
	( word.lower() not in bad_words
		and len(word) > 3) ]

rst = ' '.join(rst)

wordcount={}

for word in rst.split():

	if word not in wordcount:
		wordcount[word] = 1
	else:
		wordcount[word] += 1

for k,v, in sorted(wordcount.items(),
				key=lambda words: words[1],
				reverse = True):
	print(k,v)

word = WordCloud(max_font_size = 40).generate(rst)
plt.figure(figsize=(15, 8))
plt.imshow(word, interpolation ="bilinear")
plt.axis("off")
plt.show()