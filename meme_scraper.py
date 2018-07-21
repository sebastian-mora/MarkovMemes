# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import tweepy as tweepy
import time 
import os
import csv
import os.path


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



def save_cvs(data,username):
	with open("Scraped_TLS/tweets_%s.csv" %username, 'wb') as  csv_file:
		writer = csv.writer(csv_file)
		writer.writerow(['id','created_at','text'])
		writer.writerows(data)

def limit_handled(cursor):  #this will pause the program until for the rate limit
    while True:
        try:
            yield cursor.next()
        except tweepy.RateLimitError:
			print("You hit the rate limit! Waiting for 15mins")
			time.sleep(15 * 60)

#gest n amount of tweets from the given username
def get_tweets(username, n): 
	
	alltweets = []

	for tweet in limit_handled(tweepy.Cursor(api.user_timeline, screen_name = username).items()):
		
		alltweets.append(tweet)

	alltweets = [[tweet.id_str, tweet.created_at, tweet.text.encode("utf-8")] for tweet in alltweets]
	save_cvs(alltweets,username)




def main():


	accounts_tobe_scraped = ['@meatymadison', '@WORLDSTAR',]

	for account in accounts_tobe_scraped:
		if os.path.isfile("Scraped_TLS/tweets_%s.csv" %account) is False:
			print("Currently scraping %s" %account)
			get_tweets(account,200)
		else:
			print("%s already exists in the Archive" %account)
    
    


if __name__ == "__main__":
    main()
