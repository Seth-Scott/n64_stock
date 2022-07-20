import tweepy
import os


class Twitter:
    def __init__(self):
        self.consumer_key = os.environ.get("consumer_key")
        self.consumer_secret = os.environ.get("consumer_secret")
        self.access_token = os.environ.get("access_token")
        self.access_token_secret = os.environ.get("access_token_secret")
        self.auth = tweepy.OAuth1UserHandler(
            self.consumer_key, self.consumer_secret, self.access_token, self.access_token_secret
        )
        self.api = tweepy.API(self.auth)

    def tweet(self, message):
        self.api.update_status(message)


twitter = Twitter()
twitter.tweet("test")