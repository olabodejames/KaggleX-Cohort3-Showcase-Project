# https://newspaper.readthedocs.io/en/latest/
#$ pip3 install newspaper3k


from newspaper import Article

url = 'http://fox13now.com/2013/12/30/new-year-new-laws-obamacare-pot-guns-and-drones/'
article = Article(url)

article.download()

article.html
'<!DOCTYPE HTML><html itemscope itemtype="http://...'

article.parse()

article.authors
['Leigh Ann Caldwell', 'John Honway']

article.publish_date
datetime.datetime(2013, 12, 30, 0, 0)

article.text
'Washington (CNN) -- Not everyone subscribes to a New Year's resolution...'

article.top_image
'http://someCDN.com/blah/blah/blah/file.png'

article.movies
['http://youtube.com/path/to/link.com', ...]

article.nlp()

article.keywords
['New Years', 'resolution', ...]

article.summary
'The study shows that 93% of people ...'

import newspaper

cnn_paper = newspaper.build('http://cnn.com')

for article in cnn_paper.articles:
print(article.url)
http://www.cnn.com/2013/11/27/justice/tucson-arizona-captive-girls/
http://www.cnn.com/2013/12/11/us/texas-teen-dwi-wreck/index.html
...

for category in cnn_paper.category_urls():
print(category)

http://lifestyle.cnn.com
http://cnn.com/world
http://tech.cnn.com
...

cnn_article = cnn_paper.articles[0]
cnn_article.download()
cnn_article.parse()
cnn_article.nlp()
...

from newspaper import fulltext

html = requests.get(...).text
text = fulltext(html)