import requests
from bs4 import BeautifulSoup
from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app, resources={r"/search": {"origins": "http://localhost:3000"}}, methods=["POST"])

# Function to perform the search
def perform_search(keyword):
    try:
        # Construct the search URL with the user's keyword
        search_url = f'https://hn.algolia.com/?q={keyword}'

        response = requests.get(search_url)
        if response.status_code == 200:
            print("Request successful. Parsing HTML...")
            soup = BeautifulSoup(response.text, 'html.parser')

            # Now you can parse the search results page using BeautifulSoup
            # Your scraping logic here

            # Return the extracted data
            # return extracted_data
        else:
            print(f'Failed to fetch search results. Status code: {response.status_code}')
            return None
    except Exception as e:
        print(f'Error: {e}')
        return None
        
# Function to scrape comments, analyze sentiment, and classify
def analyze_brand_comments(url, keyword=None):
    # Send an HTTP request to the target URL
    response = requests.get(url)

    # Check if the request was successful
    if response.status_code == 200:
        # Parse the HTML content
        soup = BeautifulSoup(response.content, "html.parser")

        # Extract article titles from the specified class ("Story_title")
        article_titles = [a.text for a in soup.select(".Story_title span")]

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

@app.route('/search', methods=['POST'])
def search_endpoint():
    data = request.get_json()
    keyword = data.get('keyword', '')

    print(f"Performing search for keyword: {keyword}")

    # Call the perform_search function to perform the search
    search_results = perform_search(keyword)

    if search_results:
        print("Search successful.")
        return jsonify(search_results)
    else:
        print("Search failed.")
        return jsonify([])

if __name__ == '__main__':
    app.run(debug=True)
