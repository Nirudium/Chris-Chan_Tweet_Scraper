import tweepy 
from configscrape import __DATA__, CWCUSERID  
import writetofile

auth = tweepy.OAuthHandler(__DATA__["consumer_key"], __DATA__["consumer_secret"]) 
auth.set_access_token(__DATA__["access_token"], __DATA__["access_token_secret"]) 
api = tweepy.API(auth) 
status = api.get_status(CWCUSERID) 

print(status) 