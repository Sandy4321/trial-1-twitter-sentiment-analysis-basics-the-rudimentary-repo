from tweepy import Stream
from tweepy import OAuthHandler
from tweepy.streaming import StreamListener
import json

#consumer key, consumer secret, access token, access secret.
from twitter_app_login import *

class listener(StreamListener):

    def on_data(self, data):
        all_data = json.loads(data)
        
        
        tweet = all_data["text"]
        tweets= str(tweet.encode("utf-8"))
        print(tweet)
        with open('tweet.txt','a') as f:
            f.write(tweets)
            #f.write('\n')
            f.close()
        return True

    def on_error(self, status):
        print status

auth = OAuthHandler(ckey, csecret)
auth.set_access_token(atoken, asecret)

twitterStream = Stream(auth, listener())
twitterStream.filter(track=["India"])
