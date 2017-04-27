__author__ = 'rahul kanojiya'
import tweepy
import getdata as gd
gd.run()
contests_list = gd.contests
access_token = "ENTER_ACCESS_TOKEN"
access_token_secret = "ENTER_ACCESS_TOKEN_SECRET"
consumer_key = "ENTER_CONSUMER_KEY"
consumer_secret = "ENTER_CONSUMER_SECRET"

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

for item in contests_list:
    str = "Contest : " +item['event'] + "\nStart time : "+ item['start-time'] + " \nDuration : " + item['duration'] + "\n" + item['link']
    print(str)
    #ret = api.update_status(str)


