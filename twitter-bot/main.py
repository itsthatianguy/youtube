import tweepy
import os
import sched, time
from datetime import date


auth = tweepy.OAuthHandler(os.getenv("CONSUMER_KEY"), os.getenv("CONSUMER_SECRET"))
auth.set_access_token(os.getenv("ACCESS_TOKEN"), os.getenv("ACCESS_TOKEN_SECRET"))
api = tweepy.API(auth)

s = sched.scheduler(time.time, time.sleep)

tweet_ids = []
tweets_per_query = 20
account_names = []

def run_bot(sc):
    query = f"python -from:ericidle -from:johncleese -from:terrygilliam -monty min_faves:2 min_retweets:5 -filter:nativeretweets since:{date.today()} lang:en"
    for tweet in tweepy.Cursor(api.search, q=query, tweet_mode="extended").items(tweets_per_query):
        if tweet.id in tweet_ids:
            continue

        if len(tweet.entities['hashtags']) <= 3:
            api.retweet(tweet.id)
            api.create_favorite(tweet.id)
            tweet_ids.append(tweet.id)
            if tweet.author.screen_name not in account_names:
                api.create_friendship(screen_name = tweet.author.screen_name)
                account_names.append(tweet.author.screen_name)

    s.enter(60, 1, run_bot, (sc,))

s.enter(60, 1, run_bot, (s,))
s.run()
