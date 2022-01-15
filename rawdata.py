# Reference : https://stackoverflow.com/questions/56995350/best-practices-python-where-to-store-api-keys-tokens
import tweepy
import constants
import csv


# Initialise API authentication for Twitter Developer access
twit_api_key = constants.api_key
twit_api_secret = constants.api_secret
access_token = constants.access_token
access_token_secret = constants.access_secret

auth = tweepy.OAuthHandler(twit_api_key, twit_api_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth,wait_on_rate_limit=True)

from bs4 import BeautifulSoup
import requests as req

# Initialise list to contain Malaysia cities
city = []

# Add city into the list from the following website
page = req.get("https://worldpopulationreview.com/countries/cities/malaysia")
soup = BeautifulSoup(page.content,'html.parser')
for idx, link in enumerate(soup.find_all('td')):
        if idx % 2 == 0:
            city.append(link.string)

# Reference 1: https://dev.to/twitterdev/a-comprehensive-guide-for-using-the-twitter-api-v2-using-tweepy-in-python-15d9 
# Reference 2: https://developer.twitter.com/en/docs/twitter-api/tweets/search/api-reference/get-tweets-search-recent
from datetime import datetime, timedelta
import os.path

# Initialise permission to allow requests to scrape
client = tweepy.Client(bearer_token = constants.bearer_token)

# Initialise query to get recent tweets from users
query = '#daruratbanjir OR #banjir2021 OR banjir Malaysia OR flood Malaysia'

# Intialise time period of raw data wish to be extracted
# 10 seconds due to Twitter API limitation - must be a minimum of 10 seconds prior to the request time.
now = datetime.utcnow() - timedelta(seconds = 10)
start_time = (now - timedelta(days = 1)).strftime('%Y-%m-%dT%H:%M:%SZ')
end_time = now.strftime('%Y-%m-%dT%H:%M:%SZ')

# Initalise an array to get tweets context which is returned as an array object
d = []

if os.path.exists('tweets.csv'):
    # Open CSV file in append mode
    with open('tweets.csv', 'a', encoding='UTF8', newline='') as f:

        writer = csv.writer(f, delimiter = ',')
    
        # Use Paginator to get more than the max limits set by the search_recent_tweets function,excluding retweets
        for tweet in tweepy.Paginator(client.search_recent_tweets, query=query,
                                  tweet_fields=['context_annotations', 'created_at', 'geo'], 
                                  start_time=start_time, end_time=end_time,max_results=100).flatten(limit=10000):
            if tweet.text.startswith("RT @") == False:
                # Intialise variables and write into CSV file    
                a = tweet.text
                b = tweet.created_at
                c = tweet.geo
                if len(tweet.context_annotations)>0:
                    d = tweet.context_annotations
                e = [ele for ele in city if(ele in a)]
                writer.writerow([a,b,c,d,e])
else:
    # Open CSV file in write mode
    with open('tweets.csv', 'w', encoding='UTF8', newline='') as f:
        writer = csv.writer(f, delimiter = ',')
    
        # Initialise header
        writer.writerow(['tweet_text', 'created_at','place','context_annotations','city'])
    
        # Use Paginator to get more than the max limits set by the search_recent_tweets function,excluding retweets
        for tweet in tweepy.Paginator(client.search_recent_tweets, query=query,
                                  tweet_fields=['context_annotations', 'created_at', 'geo'], 
                                  start_time=start_time, end_time=end_time,max_results=100).flatten(limit=10000):
             if tweet.text.startswith("RT @") == False:
                # Intialise variables and write into CSV file    
                a = tweet.text
                b = tweet.created_at
                c = tweet.geo
                if len(tweet.context_annotations)>0:
                    d = tweet.context_annotations
                e = [ele for ele in city if(ele in a)]
                writer.writerow([a,b,c,d,e])

# For adding the city to header because previously we did not add in

# with open('tweets.csv',encoding='UTF8', newline='') as f:
#     r = csv.reader(f)
#     lines = list(r)

# lines[0] = ['tweet_text', 'created_at','place','context_annotations','city']

# with open('tweets.csv','w',encoding='UTF8', newline='') as f:
#     w = csv.writer(f)
#     w.writerows(lines)