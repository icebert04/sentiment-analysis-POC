# Sentiment-analysis-POC

This is a proof-of-concept for a Sentiment Analysis Bot

**NOTE** This is still a work in progress so some functions won't properly work. 
_______

## Description

The user can Type in a keyword for the bot to scrape [Hacker News](https://news.ycombinator.com/), and then it will rate the article titles that match the keyword and rate it with (positive, negative, & neutral).

![one input next to two buttons, analyze, & clear results with some results at the bottom](/public/SentimentFrontend.png)

Here we typed "Cannabis" as this was the only Noun with an understandable subject for the bot to score.

As you can see the bot recognizes this as a negative sentence.

In the future, the next function to make is a search function that scrapes data after the search is used.

____

Here is the Jupyter Notebook where the bot runs

![Two python files in a Jupyter Notebook App](/public/SentimentJupyter.png)

The Bot uses the NLTK Vader for the Sentiment Analysis

____

Here is what I used to build it:

## The Frontend

* Next.js
* React.js
* Axios
* Tailwind.css

## The Backend

* Python
* CORS
* BeautifulSoup
* NLTK
* Vader
* Flask

___

> **Disclaimer**
> This repo is for demonstration purposes only. It is not yet complete and it still needs to expand features. 

> Anyone is free to contribute to this dApp. 

Hope you can learn a lot from this.
Feel free to fork, and send your feedback on this Project

Thanks!
