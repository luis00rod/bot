import tweepy
import re
import numpy as np


class Connection(object):

    def __init__(self):
        self.apy_key = "WSbzvk0MmvVCMeHLYWhyepHg6"
        self.apy_key_secret = "7FeUI4FKeA0gtYANDg4WHw5AodQXYTbZ88YydLc9pfnrBx4LgZ"
        self.apy_key_openai = "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"
        self.consumer_key = 'WSbzvk0MmvVCMeHLYWhyepHg6'
        self.consumer_secret = '7FeUI4FKeA0gtYANDg4WHw5AodQXYTbZ88YydLc9pfnrBx4LgZ'
        self.access_token = '592854692-VSja6WOJEo9Idi9JVP5xenuehwGt7QFDDaV4ZOjW'
        self.access_secret = 'wodlFzbEjiJ40ZPvVoV4UwUXjDoDf1lLUOcOjZ7ynuHPr'
        self.auth = tweepy.OAuthHandler(self.consumer_key, self.consumer_secret)
        self.auth.set_access_token(self.access_token, self.access_secret)
        pass

    def connect_to(self, auth):
        return tweepy.API(auth)

