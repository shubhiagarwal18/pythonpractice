import pymongo
from pymongo import MongoClient
import twitter
from pprint import pprint
import tweepy
from textblob import TextBlob
import matplotlib.pyplot as plt

CONSUMER_KEY = "TPQS2mfRtv392pctndfEoThn7"
CONSUMER_SECRET = "54wHhExMml9gIkluu6FxAeKH8b7q30S2mNum49NLlmTxoGZycT"
OAUTH_TOKEN = "1377506053345046531-QiycDFKaGQ010lMf9QtLFCCs0KHLvk"
OAUTH_TOKEN_SECRET = "WHCa95f9KSDUlLWoU8I2ysgn155nbPpY9mu3EWyMlAqJt"

auth = twitter.oauth.OAuth(OAUTH_TOKEN, OAUTH_TOKEN_SECRET, CONSUMER_KEY, CONSUMER_SECRET)
twitter_api = twitter.Twitter(auth=auth)

client = MongoClient()
db = client.tweet_db
tweet_collection = db.tweet_collection
tweet_collection.create_index([("id", pymongo.ASCENDING)], unique=True)

#count = 100
#q = "Bitcoin"

q = input("Enter Keyword/Tag to search about: ")
count = int(input("Enter how many tweets to search: "))
search_results = twitter_api.search.tweets(count=count, q=q)
# pprint(search_results['search_metadata'])


statuses = search_results["statuses"]

since_id_new = statuses[-1]['id']

for statues in statuses:
    try:
        tweet_collection.insert(statues)
    except:
        pass

tweet_cursor = tweet_collection.find()
print(tweet_cursor.count())
user_cursor = tweet_collection.distinct("user.id")
print(len(user_cursor))

'''for document in tweet_cursor:
    try:
        print('-----')
        print('name:-', document["user"]["name"])
        print('text:-', document["text"])
        print('Created Date:-', document["created_at"])
    except:
        print("Error in Encoding")
        pass'''

def percentage(part, whole):
   return 100 * float(part) / float(whole)

positive = 0
negative = 0
neutral = 0
polarity = 0

tweet_cursor = tweet_collection.find()
for tweet in tweet_cursor:
    try:
        #print(tweet["text"])
        analysis = TextBlob(tweet["text"])
        polarity += analysis.sentiment.polarity

        if (analysis.sentiment.polarity == 0):
            neutral += 1

        elif (analysis.sentiment.polarity > 0.00):
            positive += 1

        elif (analysis.sentiment.polarity < 0.00):
            negative += 1
    except:
        print("Error in Encoding")
        pass


positive = percentage(positive, count)
negative = percentage(negative, count)
neutral = percentage(neutral, count)
polarity = percentage(polarity, count)
print("shubhi111",positive)
positive = format(positive, '.2f')
negative = format(negative, '.2f')
neutral = format(neutral, '.2f')

print("How people are reacting on " + q + " by analyzing " + str(count) + " tweets.")
print()
print("General Report: ")

if (polarity == 0):
    print("Neutral")
elif (polarity > 0):
    print("Positive")

elif (polarity < 0):
    print("Negative")

labels = ['positive[' + str(positive) + '%]', 'Neutral [' + str(neutral) + '%]', 'Negative [' + str(negative) + '%]']
sizes = [positive, neutral, negative]
colors = ['yellow', 'green', 'red']
patches, texts = plt.pie(sizes, colors=colors, startangle=90)
plt.legend(patches, labels, loc="best")
plt.title("How people are reacting on " + q + " by analyzing " + str(count) + " tweets.")
plt.axis('equal')
plt.tight_layout()
plt.show()