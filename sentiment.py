import tweepy
from textblob import TextBlob
import matplotlib.pyplot as plt


def percentage(part, whole):
   return 100 * float(part) / float(whole)

consumerKey = "TPQS2mfRtv392pctndfEoThn7"
consumerSecret = "54wHhExMml9gIkluu6FxAeKH8b7q30S2mNum49NLlmTxoGZycT"
accessToken = "1377506053345046531-QiycDFKaGQ010lMf9QtLFCCs0KHLvk"
accessTokenSecret = "WHCa95f9KSDUlLWoU8I2ysgn155nbPpY9mu3EWyMlAqJt"

auth = tweepy.OAuthHandler(consumerKey, consumerSecret)
auth.set_access_token(accessToken, accessTokenSecret)
api = tweepy.API(auth)

searchTerm = input("Enter Keyword/Tag to search about: ")
NoOfTerms = int(input("Enter how many tweets to search: "))

tweets = tweepy.Cursor(api.search, q=searchTerm).items(NoOfTerms)

positive = 0
negative = 0
neutral = 0
polarity = 0

for tweet in tweets:
    #print(tweet.text)
    analysis = TextBlob(tweet.text)
    polarity += analysis.sentiment.polarity

    if (analysis.sentiment.polarity == 0):
            neutral += 1

    elif (analysis.sentiment.polarity > 0.00):
            positive += 1

    elif (analysis.sentiment.polarity < 0.00):
            negative += 1


positive = percentage(positive, NoOfTerms)
negative = percentage(negative, NoOfTerms)
neutral = percentage(neutral, NoOfTerms)
polarity = percentage(polarity, NoOfTerms)

positive = format(positive, '.2f')
negative = format(negative, '.2f')
neutral = format(neutral, '.2f')

print("How people are reacting on " + searchTerm + " by analyzing " + str(NoOfTerms) + " tweets.")
print()
print("General Report: ")

if (polarity == 0):
        print("Neutral")
elif (polarity > 0):
        print("Positive")

elif (polarity < 0):
        print("Negative")

labels = ['positive['+ str(positive) + '%]', 'Neutral [' + str(neutral) + '%]', 'Negative [' + str(negative) + '%]' ]
sizes = [positive,neutral, negative]
colors = ['yellow','green', 'red']
patches,texts = plt.pie(sizes,colors=colors, startangle=90)
plt.legend(patches, labels, loc ="best")
plt.title("How people are reacting on " + searchTerm + " by analyzing " + str(NoOfTerms) + " tweets.")
plt.axis('equal')
plt.tight_layout()
plt.show()