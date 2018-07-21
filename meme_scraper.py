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

#writes the necesary data from .csv file into txt format, isolates text information and removes RTs, etc.
#writes the tweets into file named "tweets" in Scraped_TLS folder
def filter_and_write_tweets(account):
    
    text_file = open("Scraped_TLS/tweets.txt", "w")
    
    if os.path.isfile("Scraped_TLS/tweets_%s.csv" %account) is False:
        print("This account's file does not exist.")
        return None
    
    else:
        with open(("Scraped_TLS/tweets_%s.csv" %account), 'r') as csv_file:
            csv_reader = csv.reader(csv_file)
            
            next(csv_reader) #skips format line
            
            for line in csv_reader:
                
                tweet = line[2]
               #get rid of RTs
                rt_check = tweet[:2]
                if rt_check == 'RT':
                    next(csv_reader)
                    continue
                
                #ignore links and @s by breaking up each word in tweet
                seperate_words = tweet.split(' ')
                
                for word in seperate_words:
                    if ('https://' or 'http://') in word:
                        seperate_words.remove(word)
                        continue
                    if ('@') in word:
                        seperate_words.remove(word)
                        continue
                #join list back together into printable form
                
                tweet = " ".join(seperate_words)
                text_file.write(tweet +"\n")
     
    text_file.close()   
    

def main():


	accounts_tobe_scraped = ['@meatymadison', '@WORLDSTAR','@CueBallClarence',
                          '@WoodySee', '@YLSMJ', '@hornystonerdad',
                          '@ilooklikelilbil',]

	for account in accounts_tobe_scraped:
		if os.path.isfile("Scraped_TLS/tweets_%s.csv" %account) is False:
			print("Currently scraping %s" %account)
			get_tweets(account,200)
		else:
			print("%s already exists in the Archive" %account)
    
        filter_and_write_tweets(account)


if __name__ == "__main__":
    main()
