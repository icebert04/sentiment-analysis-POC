import React, { useState } from 'react';
import axios from 'axios';
import Link from 'next/link';

function SentimentAnalysis() {
  const [keyword, setKeyword] = useState('');
  const [results, setResults] = useState([]);
  const [isLoading, setIsLoading] = useState(false);
  const [noMatches, setNoMatches] = useState(false);

  const handleAnalyze = async () => {
    setIsLoading(true);
    try {
      const response = await axios.post('http://localhost:5000/analyze_sentiment_endpoint', {
        keyword: keyword,
        url: 'https://news.ycombinator.com/',
      });
      const sentimentResults = response.data;

      if (sentimentResults.length === 0) {
        setNoMatches(true);
      } else {
        setNoMatches(false);
        setResults((prevResults) => [...prevResults, ...sentimentResults]);
      }
    } catch (error) {
      if (error.response && error.response.status === 404) {
        setNoMatches(true);
      } else {
        console.error('Error analyzing sentiment:', error);
      }
    } finally {
      setIsLoading(false);
    }
  };

  const handleClearResults = () => {
    setResults([]);
    setNoMatches(false);
  };

  return (
    <div className="container mt-20 mx-auto">
      <h1 className="text-3xl mx-auto mb-4 w-3/4 text-center">Sentiment Analysis</h1>
      <div className='mx-auto mb-4 w-3/4 flex justify-center items-center'>
        <input
          type="text"
          placeholder="Enter a keyword"
          value={keyword}
          onChange={(e) => setKeyword(e.target.value)}
          className="border-2 border-gray-300 rounded-md w-3/4 p-2 mr-2"
        />
        <button
          onClick={handleAnalyze}
          className="bg-indigo-600 text-white rounded-md w-3/4 p-2 mx-2"
        >
          Analyze
        </button>
        <button
          onClick={handleClearResults}
          className="bg-red-600 text-white rounded-md w-3/4 p-2 ml-2"
        >
          Clear Results
        </button>
      </div>
      {isLoading ? (
        <div className="text-center border-2 border-gray-300 rounded-md p-4 text-lg">Loading...</div>
      ) : (
        <div className="mt-4 mx-auto mb-4 w-3/4 justify-center items-center">
          {noMatches ? (
            <div className="text-center border-2 border-gray-300 rounded-md p-4 text-lg">
              No keywords matched.
            </div>
          ) : null}
          {results.map((result, index) => (
            <div key={index} className="border-2 border-gray-300 rounded-md p-4">
              <p>Keyword: {result.keyword}</p>
              <p>Article: {result.article_title}</p>
              <p>Sentiment: {result.sentiment}</p>
            </div>
          ))}
        </div>
      )}
      <div>
        <h3 className='w-3/4 text-right mx-auto'>
          Data from <Link href="https://news.ycombinator.com/" target="_blank" rel="noopener noreferrer" className='font-bold'>Hacker News</Link>
        </h3>
      </div>
    </div>
  );
}

export default SentimentAnalysis;
