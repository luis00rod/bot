import requests
from transformers import pipeline
from newsapi import NewsApiClient
import tweepy
import re
import numpy as np


class Connection(object):

    def __init__(self):

        pass

    def twitter_conn(self):
        consumer_key = 'WSbzvk0MmvVCMeHLYWhyepHg6'
        consumer_secret = '7FeUI4FKeA0gtYANDg4WHw5AodQXYTbZ88YydLc9pfnrBx4LgZ'
        access_token = '592854692-VSja6WOJEo9Idi9JVP5xenuehwGt7QFDDaV4ZOjW'
        access_secret = 'wodlFzbEjiJ40ZPvVoV4UwUXjDoDf1lLUOcOjZ7ynuHPr'
        auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
        auth.set_access_token(access_token, access_secret)
        return tweepy.API(auth)

    def get_news(self):
        api_key = "ec1deee45eb64a0a93e6313807943f9e"
        newsapi = NewsApiClient(api_key='ec1deee45eb64a0a93e6313807943f9e')
        query = "bitcoin"
        language = "en"

        url = f"https://newsapi.org/v2/everything?q={query}&language={language}&apiKey={api_key}"
        response = requests.get(url)
        articles = newsapi.get_everything(q='bitcoin',
                                          from_param='2023-04-01',
                                          to='2023-04-11',
                                          language='en',
                                          sort_by='relevancy')["articles"]
        sentiment_pipeline = pipeline('sentiment-analysis', framework='tf',
                                      model='nlptown/bert-base-multilingual-uncased-sentiment')
        sentiments = []
        for article in articles:
            title = article["title"]
            description = article["description"]
            url = article["url"]
            published_at = article["publishedAt"]
            content = article["content"]
            if content:
                content = content.replace("\n", " ")
                sentiment = sentiment_pipeline(content)[0]["label"]
                sentiments.append(sentiment)
                print(f"Title: {title}")
                print(f"Description: {description}")
                print(f"URL: {url}")
                print(f"Published at: {published_at}")
                print(f"Sentiment: {sentiment}\n")

        return article
