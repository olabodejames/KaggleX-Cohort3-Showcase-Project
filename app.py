# Import necessary libraries
import requests
from bs4 import BeautifulSoup
from textblob import TextBlob
from flask import Flask, render_template, request

##The data - 

# Sample aggregated news data (replace this with actual data)
aggregated_news = [
    {"headline": "News Headline 1", "summary": "Summary 1"},
    {"headline": "News Headline 2", "summary": "Summary 2"},
    {"headline": "News Headline 3", "summary": "Summary 3"},
    # Add more news articles
]




# Function to scrape news articles
def scrape_news(websites):
    news_data = []

    for website in websites:
        response = requests.get(website)
        soup = BeautifulSoup(response.content, 'html.parser')

        # Extract news articles and their content
        articles = soup.find_all('article')  # Adjust this based on the HTML structure
        for article in articles:
            title = article.find('h2').text
            content = article.find('p').text
            sentiment = analyze_sentiment(content)

            news_data.append({'title': title, 'content': content, 'sentiment': sentiment})

    return news_data

# Function to analyze sentiment of news content
def analyze_sentiment(text):
    blob = TextBlob(text)
    sentiment_score = blob.sentiment.polarity

    if sentiment_score > 0.3:
        return 'Good'
    elif sentiment_score < -0.3:
        return 'Sad'
    else:
        return 'Neutral'

def analyze_sentiment(article_text):
    analysis = TextBlob(article_text)
    sentiment = analysis.sentiment.polarity

    if sentiment > 0.3:
        return "Positive"
    elif sentiment > 0:
        return "Slightly Positive"
    elif sentiment == 0:
        return "Neutral"
    elif sentiment > -0.2:
        return "Slightly Negative"
    else:
        return "Negative"

# Define your Flask routes and API endpoints
@app.route('/')
def index():
    news_data = scrape_news(news_websites)
    return render_template('index.html', news_data=news_data)

if __name__ == '__main__':
    app.run(debug=True)

@app.route('/api/news', methods=['GET'])
def get_news():
    # Retrieve and return the aggregated news

if __name__ == '__main__':
    app.run(debug=True)





