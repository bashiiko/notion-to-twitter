import tweepy
import json

# https://kurozumi.github.io/tweepy/

class Twitter():
    def __init__(self, credential_data_path):
        credential_twitter = open(credential_data_path, "r")
        credential_twitter_load = json.load(credential_twitter)

        API_KEY = credential_twitter_load["API_KEY"]
        API_KEY_SECRET = credential_twitter_load["API_KEY_SECRET"]
        ACCESS_TOKEN = credential_twitter_load["ACCESS_TOKEN"]
        ACCESS_TOKEN_SECRET = credential_twitter_load["ACCESS_TOKEN_SECRET"]

        self.auth = tweepy.OAuthHandler(API_KEY, API_KEY_SECRET)
        self.auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)

    def tweet(self, message):
        # キーワードからツイートを取得
        api = tweepy.API(self.auth)
        tweets = api.search(q=['Python'], count=10)
        tweets = api.user_timeline(id = 'bashiiiiko')
        #tweets = api.home_timeline()
        for tweet in tweets:
            print('-----------------')
            print(tweet.text)

        # 好きな言葉をツイート
        #api.update_status("Pythonから投稿テスト")