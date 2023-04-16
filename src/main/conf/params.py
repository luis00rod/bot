class Params:

    def __init__(self):
        self.general_params = self.general_params()
        self.sentiment_analysis_params = self.get_binance_keys()
        self.bollinger_params = self.get_news_key()
        pass

    def get_twitter_keys(self) -> dict:
        params_dict = {
            "api_key": "WSbzvk0MmvVCMeHLYWhyepHg6",
            "api_secret": "7FeUI4FKeA0gtYANDg4WHw5AodQXYTbZ88YydLc9pfnrBx4LgZ",
            "access_token": "592854692-VSja6WOJEo9Idi9JVP5xenuehwGt7QFDDaV4ZOjW",
            "access_secret": 'wodlFzbEjiJ40ZPvVoV4UwUXjDoDf1lLUOcOjZ7ynuHPr'
        }
        return params_dict

    def get_binance_keys(self) -> dict:
        params_dict = {
            "api_key": "dNC0absMhm1yaOQ5dlG9xQabyqIzpNdJo9PJ6l7snb7O17DVWWPtHvQ5GUpgm0Tq",
            "api_secret": "Xs5Lo26gAAJrAN6Lg4FS9KBkJvKl7zjMP5JRxwTs9IKt1drdLopug6TS8h1asuc9"
        }
        return params_dict

    def get_news_key(self) -> dict:
        params_dict = {
            "api_key": "ec1deee45eb64a0a93e6313807943f9e"
        }
        return params_dict

