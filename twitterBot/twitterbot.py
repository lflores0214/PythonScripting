import tweepy
from decouple import config
import time


consumer_key = config("TWITTER_API_KEY")
consumer_secret = config("API_KEY_SECRET")
access_token = config("ACCESS_TOKEN")
access_token_secret = config("ACCESS_TOKEN_SECRET")


auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

public_tweets = api.home_timeline()
user = api.me()
followers = api.followers()

def limit_handler(cursor):
    try:
        while True:
            yield cursor.next
    except tweepy.RateLimitError:
        time.sleep(1000)


search_string = 'python'

number_of_tweets = 2

for tweet in tweepy.Cursor(api.search, search_string).items(number_of_tweets):
    try:
        # print(tweet)
        tweet.favorite()
        print("I liked that tweet")
    except tweepy.TweepError as e:
        print(e.reason)
    except StopIteration:
        break

