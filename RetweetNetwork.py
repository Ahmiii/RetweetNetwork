#!/usr/bin/env python
# coding: utf-8

# In[46]:


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

CONSUMER_KEY="fOto54rmIL287AljKvZGkhBbW"
CONSUMER_SECRET="cce12Z4coGbDa2Sv2B8h65RJ8w84KPGwfsa2hRNDD5yBcIMkZd"
ACCESS_KEY="746132823686393856-Wou6lNZPjtwwf6TNi7uoJfGDHy0NfYw"
ACCESS_SECRET="xisiY78hiBL0JujJbSwTXT61r7EhBMrPoq2u07bYjAElU"

auth = OAuthHandler(CONSUMER_KEY,CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
api = tweepy.API(auth,wait_on_rate_limit=True,wait_on_rate_limit_notify=True)


# In[47]:


import pandas as pd


# In[51]:


data=pd.read_csv('Network.csv',header=None,names=['Tweetid','RetweetPerson'])


# In[52]:


data.head()


# In[96]:


for i in range(len(data.RetweetPerson)-1):
    for j in range(0,len(data.RetweetPerson)-1):
        #print(data.RetweetPerson[i],data.RetweetPerson[j])
        if(data.RetweetPerson[i]==data.RetweetPerson[j]):
            print('pass')
        else:
            print(data.RetweetPerson[i],data.RetweetPerson[j])
            status=api.show_friendship(source_screen_name=data.RetweetPerson[i],target_screen_name=data.RetweetPerson[j])
            print(status[0].following,status[1].followed_by)


# In[ ]:




