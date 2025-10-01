import os
import re
import json
import tweepy
from dotenv import load_dotenv
from collections import Counter

from oauthlib.uri_validate import query

load_dotenv()
Bearer_token = os.getenv("bearer_token")
client = tweepy.Client(bearer_token=Bearer_token)

coin_format = r"\$[A-Za-z]{2,10}"
coint_counter = Counter()

query = "#memecoin -is:retweet lang:en"

tweets = client.search_recent_tweets(query=query, max_results=100, tweet_fields=['text'])
for tweet in tweets.data:
    coins_in_tweet = re.findall(coin_format, tweet.text)
    for coin in coins_in_tweet:
        coint_counter[coin.upper()] += 1

print("trending coins under #memecoin")
for coin, count in coint_counter.most_common(10):
    print(coin,count)
