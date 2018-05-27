import tweepy

# add your keys
CK = ""
CS = ""
AK = ""
AS = ""

auth = tweepy.OAuthHandler(CK, CS)
auth.set_access_token(AK, AS)
api = tweepy.API(auth)

# add search word and count
tweets = api.search(q='word', count=10)

# show tweets
for tweet in tweets:
  print(tweet.text, "\n")

