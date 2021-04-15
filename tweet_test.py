import tweepy
import json

# https://kurozumi.github.io/tweepy/

credential_twitter = open("./credential_twitter.json", "r")
credential_twitter_load = json.load(credential_twitter)

API_KEY = credential_twitter_load["API_KEY"]
API_KEY_SECRET = credential_twitter_load["API_KEY_SECRET"]
ACCESS_TOKEN = credential_twitter_load["ACCESS_TOKEN"]
ACCESS_TOKEN_SECRET = credential_twitter_load["ACCESS_TOKEN_SECRET"]


auth = tweepy.OAuthHandler(API_KEY, API_KEY_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)

# キーワードからツイートを取得
api = tweepy.API(auth)
tweets = api.search(q=['Python'], count=10)
tweets = api.user_timeline(id = 'bashiiiiko')
#tweets = api.home_timeline()
for tweet in tweets:
    print('-----------------')
    print(tweet.text)

# 好きな言葉をツイート
api.update_status("Pythonから投稿テスト")