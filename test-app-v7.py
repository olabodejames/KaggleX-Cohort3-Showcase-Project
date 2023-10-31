# Import packages
from newspaper import newspaper # Corrected import statement
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
import pandas as pd
from flask import Flask, render_template

# Create a newspaper object with the URL of the news website
news = newspaper('https://www.bbc.com/news')

# Get a list of article objects from the newspaper object
articles = news.articles

# Create a sentiment analyzer object
analyzer = SentimentIntensityAnalyzer()

# Create an empty list to store the article data
data = []

# Loop through each article object
for article in articles:
    # Get the title and URL of the article
    title = article.title
    url = article.url

    # Download and parse the article
    article.download()
    article.parse()

    # Get the text of the article
    text = article.text

    # Perform sentiment analysis on the text and get the compound score
    sentiment = analyzer.polarity_scores(text)['compound']

    # Append the title, URL, and sentiment score to the data list
    data.append([title, url, sentiment])

# Create a pandas data frame from the data list
df = pd.DataFrame(data, columns=['Title', 'URL', 'Sentiment'])

# Create a flask app object
app = Flask(__name__)

# Define a route for the home page
@app.route('/')
def home():
    # Render the home page template with the data frame as an argument
    return render_template('home.html', df=df)

# Run the app
if __name__ == '__main__':
    app.run(debug=True)
