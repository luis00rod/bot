import re

from transformers import pipeline


class SentimentAnalysis(object):

    def __init__(self, api):
        self.api = api
        pass

    def apply(self):
        tweets = self.api.search_tweets(q="bitcoin OR BTC", count=100)

        processed_tweets = []
        for tweet in tweets:
            text = tweet.text
            text = re.sub(r'http\S+', '', text)
            text = re.sub(r'@\w+', '', text)
            processed_tweets.append(text)

        sentiments = []
        sentiment_pipeline = pipeline('sentiment-analysis', framework='tf',
                                      model='nlptown/bert-base-multilingual-uncased-sentiment')
        for tweet in processed_tweets:
            sentiment = sentiment_pipeline(tweet)[0]['label']
            sentiments.append(sentiment)

        sentiment_scores = []
        for sentiment in sentiments:
            if '1 star' in sentiment or '2 stars' in sentiment:
                sentiment_scores.append(-1)
            elif '4 stars' in sentiment or '5 stars' in sentiment:
                sentiment_scores.append(1)
            else:
                sentiment_scores.append(0)
        return sentiment_scores
