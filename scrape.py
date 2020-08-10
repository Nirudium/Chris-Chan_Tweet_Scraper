import tweepy 
from configscrape import __DATA__, CWCUSERID  
from copy import deepcopy
from datetime import datetime
import csv
import pickle


### Connects to Twitter via a Developer App
auth = tweepy.OAuthHandler(__DATA__["consumer_key"], __DATA__["consumer_secret"]) 
auth.set_access_token(__DATA__["access_token"], __DATA__["access_token_secret"]) 
api = tweepy.API(auth) 

### Writes to a csv file (Should be openable in Excel for easy access and management) 
def writeToArchive(text, dateOfWriting):
    with open("cwctweets-" + datetime.today().strftime('%Y-%m-%d') + ".csv") as cwcTweets:
        cwcWriter = csv.writer(cwcTweets, delimiter=' ', quotechar=',', quoting=csv.QUOTE_MINIMAL)
        cwcWriter.writerow([text] + [dateOfWriting.strftime('%Y-%m-%d')])

### Wrapper function to make it more human readable
def grabLatestTweet():
    latestTweet = api.user_timeline(CWCUSERID, count = 1)[0]
    return latestTweet

### starts up the scraper
def startScraper(**kwargs):
    global mostRecentTweet
    pickle = kwargs.pop('pickle', False)
    if not pickle:
        mostRecentTweet = deepcopy(grabLatestTweet())
    else:
        mostRecentTweet = pickle.load(open("lastestTweet.pickle", "rb"))
    while True:
        if grabLatestTweet() != mostRecentTweet:
            mostRecentTweet = deepcopy(grabLatestTweet())
            writeToArchive(mostRecentTweet.text, mostRecentTweet.created_at)
            print('Just archived this tweet! \n`{}` \n'.format(mostRecentTweet.text))

if __name__ == "__main__":
    try: 
        startScraper()
    except KeyboardInterrupt:
        print("Program closing, pickling Chris's most recent tweet")
        pickle.dump(mostRecentTweet, open("latestTweet.pickle", "wb"))