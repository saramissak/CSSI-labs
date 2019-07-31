class Tweet(object):
    def __init__(self, user, tweet, retweets):
        self.Tweet_user = user
        self.Tweet_tweet = tweet
        self.Tweet_retweets = retweets

    def getTweet(self):
        if(self.Tweet_retweets <= 1000):
            return "Thats not a lot of tweets"
        else:
            return "Thats a lot of tweets"

my_tweet = Tweet('lol_smm', 'nah', 201)
print(my_tweet.getTweet())
