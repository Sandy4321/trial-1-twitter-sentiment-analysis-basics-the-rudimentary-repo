from tweepy import Stream
from tweepy import OAuthHandler
from tweepy.streaming import StreamListener
import json
from twitter_app_login import *

class listener(StreamListener):

    def on_data(self, data):
        all_data = json.loads(data)
        
        tweet = all_data["text"]
        print(tweet)
        tweets = str(tweet.encode("utf-8"))
        with open("tweets.json","a") as f:
            f.write(tweets)
            f.close()
        return True

    def on_error(self, status):
        print status

auth = OAuthHandler(ckey, csecret)
auth.set_access_token(atoken, asecret)

twitterStream = Stream(auth, listener())
twitterStream.filter(track=["India"])
