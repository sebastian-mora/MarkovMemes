# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import tweepy as tweepy
import time 
import os


# Consumer keys and access tokens, used for OAuth
consumer_key = 'csVjaKZLVGSNbg0ublfPpw7vd'
consumer_secret = 'xxxxxxxxxxxxxxxxxxx' 
access_token = '4846250833-OsRTKTZcTTXS9raSlHlrGYkeCF9BsaPeTLvFv9o'
access_secret = 'xxxxxxxxxxxxxxxxxxxxxxxxxxx'

#OAuth process, using the keys and tokens
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_secret)
 
# Creation of the actual interface, using authentication
api = tweepy.API(auth)

#api.update_status('Im back')

#gest n amount of tweets from the given username
def get_tweets(username, n): 
    
    tweets = api.user_timeline(screen_name=username)


