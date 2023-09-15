import requests
from bs4 import BeautifulSoup
import time
import nltk
from nltk.sentiment.vader import SentimentIntensityAnalyzer
from flask import Flask, request, jsonify
from flask_cors import CORS

# Initialize NLTK and download the VADER lexicon (only need to do this once)
nltk.download('vader_lexicon')

# Initialize Flask app
app = Flask(__name__)
CORS(app, resources={r"/analyze_sentiment_endpoint": {"origins": "http://localhost:3000"}}, methods=["DELETE", "POST", "GET", "OPTIONS"])
# CORS(app)
# Initialize the VADER sentiment analyzer
sia = SentimentIntensityAnalyzer()

# Function to truncate text to fit within a specified length
def truncate_text(text, max_length):
    if len(text) > max_length:
        return text[:max_length]
    return text

# Function to scrape comments, analyze sentiment, and classify
def analyze_brand_comments(url, keyword=None):
    # Send an HTTP request to the target URL
    response = requests.get(url)

    # Check if the request was successful
    if response.status_code == 200:
        # Parse the HTML content
        soup = BeautifulSoup(response.content, "html.parser")

        # Extract article titles from the titleline class
        article_titles = [a.text for a in soup.select(".titleline > a:first-child")]

        # Process and analyze comments from each article title
        results = []

        for article_title in article_titles:
            title_text = article_title

            # Check if the keyword is in the article title
            if keyword is not None and keyword.lower() in title_text.lower():
                # Perform sentiment analysis on the article title
                title_text = truncate_text(title_text, 100)  # Truncate for display
                sentiment_scores = sia.polarity_scores(title_text)

                # Determine sentiment based on compound score
                compound_score = sentiment_scores['compound']

                if compound_score >= 0.05:
                    sentiment = "positive"
                elif compound_score <= -0.05:
                    sentiment = "negative"
                else:
                    sentiment = "neutral"

                # Add the result to the list
                results.append({"keyword": keyword, "article_title": title_text, "sentiment": sentiment})

        # Return the list of results
        return results

    # Return an empty list when no matching articles are found
    return []

@app.route('/analyze_sentiment_endpoint', methods=['POST'])
def analyze_sentiment_endpoint():
    data = request.get_json()
    keyword = data.get('keyword', '')
    url = data.get('url', '')

    # Call the analyze_brand_comments function to perform sentiment analysis
    result = analyze_brand_comments(url, keyword)

    if result:
        return jsonify(result)
    else:
        return jsonify({"error": "No matching articles found."}), 404

if __name__ == '__main__':
    app.run(debug=True)
