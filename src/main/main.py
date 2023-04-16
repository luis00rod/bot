from common.connection import Connection
from conf.params import Params
from interactor.sentiment_analysis import SentimentAnalysis
from pipeline.first_round import FirstRound


class Controller(object):

    def __init__(self, conf):
        conn = Connection()
        pipeline = FirstRound(SentimentAnalysis(conn.twitter_conn()), conf)
        pipeline.run()


if __name__ == "__main__":
    Controller(Params)
