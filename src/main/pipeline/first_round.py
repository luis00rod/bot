class FirstRound(object):

    def __init__(self, sentiment_analysis, conf):
        self.sentiment_analysis = sentiment_analysis
        pass

    def run(self):
        sentiment_scores = self.sentiment_analysis.apply()

        pass
