import tweepy
import re
import numpy as np


class Connection(object):

    def __init__(self):

        pass

    def twitter_conn(self):
        apy_key = "WSbzvk0MmvVCMeHLYWhyepHg6"
        apy_key_secret = "7FeUI4FKeA0gtYANDg4WHw5AodQXYTbZ88YydLc9pfnrBx4LgZ"
        apy_key_openai = "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"
        consumer_key = 'WSbzvk0MmvVCMeHLYWhyepHg6'
        consumer_secret = '7FeUI4FKeA0gtYANDg4WHw5AodQXYTbZ88YydLc9pfnrBx4LgZ'
        access_token = '592854692-VSja6WOJEo9Idi9JVP5xenuehwGt7QFDDaV4ZOjW'
        access_secret = 'wodlFzbEjiJ40ZPvVoV4UwUXjDoDf1lLUOcOjZ7ynuHPr'
        auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
        auth.set_access_token(access_token, access_secret)
        return tweepy.API(auth)

    def get_news(self):
        pass