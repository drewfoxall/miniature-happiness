import tweepy


mykeys = open("TwitterBots/API_KEYS/twitterkeys.txt", "r").read().splitlines()

api_key = mykeys[0]
api_key_secret = mykeys[1]
access_token = mykeys[2]
access_token_secret = mykeys[3]

auth_handler = tweepy.OAuthHandler(consumer_key=api_key, consumer_secret=api_key_secret)
auth_handler.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth_handler)

api.update_status(status ="hihihihihihihihihihihi") 