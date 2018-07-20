# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import tweepy as tweepy
import time 
import os
import csv


# Consumer keys and access tokens, used for OAuth
consumer_key = 'csVjaKZLVGSNbg0ublfPpw7vd'
consumer_secret = 'XiixLm5g1ACEvQk0JPo5KllW393xDhy7aHK6vTlAJ0KUynw0mS' 
access_token = '4846250833-OsRTKTZcTTXS9raSlHlrGYkeCF9BsaPeTLvFv9o'
access_secret = '9TpUnT0GgEYCK9yI2KZ7Yh4bNLYIDyHwoDBmcIUxKOtiV'

#OAuth process, using the keys and tokens
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_secret)
 
# Creation of the actual interface, using authentication
api = tweepy.API(auth)

#api.update_status('Im back')



def save_cvs(data):
	with open("tweets.csv", 'wb') as  csv_file:
		writer = csv.writer(csv_file)
		writer.writerow(['id','created_at','text'])
		writer.writerows(data)


#gest n amount of tweets from the given username
def get_tweets(screen_name, n): 
	
	alltweets = []

	tl_tweets = api.user_timeline(username = '@seb1055',count=n) #get most recent tweets

	alltweets.extend(tl_tweets) #save the most recent 

	oldest = alltweets[-1].id - 1

	while len(tl_tweets) > 0:
		print "getting tweets before %s" % (oldest)
		
		#all subsiquent requests use the max_id param to prevent duplicates
		new_tweets = api.user_timeline(username = '@seb1055',count=n,max_id=oldest)
		
		#save most recent tweets
		alltweets.extend(new_tweets)
		
		#update the id of the oldest tweet less one
		oldest = alltweets[-1].id - 1
		
		print "...%s tweets downloaded so far" % (len(alltweets))
		save_cvs([[tweet.id_str, tweet.created_at, tweet.text.encode("utf-8")] for tweet in alltweets])
	
	#transform the tweepy tweets into a 2D array that will populate the csv	
	





def main():
	get_tweets("@seb1055",200)
	pass
    
    


if __name__ == "__main__":
    main()
