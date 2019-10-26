
import json
import re
import tweepy
from tweepy import Stream
from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
import urllib
import re
import time
import csv
from bson import json_util
import pandas as pd

CONSUMER_KEY=""
CONSUMER_SECRET=""
ACCESS_KEY=""
ACCESS_SECRET=""

auth = OAuthHandler(CONSUMER_KEY,CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
api = tweepy.API(auth,wait_on_rate_limit=True,wait_on_rate_limit_notify=True)

csvFile=open('Network.csv','a')
csvWriter=csv.writer(csvFile)

for reTweet in api.retweets(1132711785256103938):
	#print(reTweet)
	csvWriter.writerow([reTweet.retweeted_status.id,reTweet.user.screen_name])
	print(reTweet.retweeted_status.id,reTweet.user.screen_name)






