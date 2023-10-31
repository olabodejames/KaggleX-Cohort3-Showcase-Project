#URL - https://newsapi.org/docs/get-started
#URL - https://newspaper.readthedocs.io/en/latest/

import newspaper
#pip install newspaper3k
import feedparser
import pandas as pd
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
from flask import Flask, render_template

# Create a sentiment analyzer object
analyzer = SentimentIntensityAnalyzer()


def scrape_news_from_feed(feed_url):
	articles = []
	feed = feedparser.parse(feed_url)
	for entry in feed.entries:
		# create a newspaper article object
		article = newspaper.Article(entry.link)
		# download and parse the article
		article.download()
		article.parse()
		# extract relevant information
		articles.append({
			'title': article.title,
			'author': article.authors,
			'publish_date': article.publish_date,
			'content': article.text,
            'url': article.url
		})
	return articles

# Function to analyze sentiment of news content
def classify_sentiment(compound_score):
    if -1 <= compound_score <= -0.6:
        return "Depressing"
    elif -0.6 < compound_score <= -0.2:
        return "Sad"
    elif -0.2 < compound_score <= 0.2:
        return "Neutral"
    elif 0.2 < compound_score <= 0.6:
        return "Good"
    elif 0.6 < compound_score <= 1:
        return "Uplifting"
    else:
        return "Out of Range"



feed_url = 'http://feeds.bbci.co.uk/news/rss.xml'
articles = scrape_news_from_feed(feed_url)

resultList = []

# print the extracted articles
for article in articles:
    
     # Get the text of the article
    text = article['content']

    # Perform sentiment analysis on the text and get the compound score
    sentiment = analyzer.polarity_scores(text)['compound']
    classified = classify_sentiment(sentiment)

    # Create a new row as a dictionary
    new_row = [article['title'], article['author'], article['publish_date'], sentiment, classified, article['content'],article['url']]

    # Append the new row to the DataFrame
    resultList.append(new_row)

# Convert the DataFrame to a CSV file
result = result = pd.DataFrame(resultList, columns=['Title', 'Author', 'Publish Date', 'sentiment','Classification','Content', 'url'])
result.to_csv('news_data_5.csv', index=False)

# Create a pandas data frame from the data list# Create a pandas DataFrame from specific columns of the result DataFrame
df = pd.DataFrame({
    'Title': result['Title'],
    'URL': result['url'],
    'Sentiment': result['sentiment'],
    'Classification': result['Classification']
})

# Create a flask app object
app = Flask(__name__)

df.head()

# Define a route for the home page
@app.route('/')
def home():
    # Render the home page template with the data frame as an argument
    return render_template('home.html', df=df)

# Run the app
if __name__ == '__main__':
    app.run(debug=True)