import pymongo
from pymongo import MongoClient
import json
import twitter
from pprint import pprint

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

count = 100
q = "Bitcoin"
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

for document in tweet_cursor:
    try:
        print('-----')
        print('name:-', document["user"]["name"])
        print('text:-', document["text"])
        print('Created Date:-', document["created_at"])
    except:
        print("Error in Encoding")
        pass
