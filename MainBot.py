from twitter import *
import re
import time
import calendar
import datetime
from collections import OrderedDict
import random
#possible data flow
#1. check recent tweets from those i am following
#   1a. split tweet into words by whitespace
#       1b. if a tweet contains an error add it to the temp list
#2. Check statuses.sample tweets
#   2a. split tweet into words by whitespace
#       2b. if a tweet contains an error add it to the temp list
#3. assign score to all tweets in the temp list
#   3a. followers * errors
#   3b. Sort list based on score
#4. wait until the next time % 5 minutes == 0
#5. Post replies to top 5-10 tweets

# Authenticates with twitter API

random.seed()

t = Twitter(
            auth=OAuth("1542425641-KYBzBv902fK7sb15jrtoqXqCnVYval8nqdxDlw6", "8yE0zNQ25WVKYwH8AMyFMaJQPXVLz9bal7TK8ErRZU",
                        "iRbKqkKjiky5ulsks3SoaA", "zlLAlpuuO8Jx7N5KIx59CNS1gt1FrpZT80FcbA4U")
           )
twitter_stream = TwitterStream(auth=OAuth("1542425641-KYBzBv902fK7sb15jrtoqXqCnVYval8nqdxDlw6", "8yE0zNQ25WVKYwH8AMyFMaJQPXVLz9bal7TK8ErRZU",
                        "iRbKqkKjiky5ulsks3SoaA", "zlLAlpuuO8Jx7N5KIx59CNS1gt1FrpZT80FcbA4U")
                               )

misspellings = {'summa' : "summer", 'Summa' : "Summer", 'ill': "i'll", 'Ill' : "I'll", 'y' : "why", 'Y' : "Why", 'yea' : "yeah", 'Yea' : "Yeah", 
                'hes':"he's", 'u\'re':"you're", 'U\'re':"You're", 'thats' : "that's", 'Thats' : "That's", 'gonna' : "going to", 'Gonna' : "Going to", 'cus' : "cus", 'Cus' : "Cus", 'wont' : "won't", 'Wont' : "Won't", 'kinda' : "kind of", 'Kinda' : "Kind of", 'wouldve' : "would've", 'Wouldve' : "Would've",
                'U': "You", 'u': "you", 'bc': "because", 'i': "I", 'im': "i'm", 'Im': "I'm", 'dat': "that", 'Dat': "That", 'doe': "though", 'Doe': "Though", 'dont': "don't", 'Dont': "Don't", 'comlpain': "complain",'Comlpain': "Complain", 'ppl': "people", 'Ppl': "People", 'wen': "when", 'Wen': "When", 'cant': "can't", 'Cant': "Can't", 'bc': "because"}

while True:
    #list of tweets to be further anaylzed
    errorTweetsList = []
    errorTweetsListErrors = []

    #set of tweets in the last five minutes, elements are all unique
    lastFiveMinTweets = []
    ###one less than the desired retrieval count
    ##RETRIEVE_COUNT = 199
    ##
    ##fiveMinsFound = False
    ##
    ###finds all tweets on my home timeline posted in the last five minutes
    ##x = t.statuses.home_timeline(count = RETRIEVE_COUNT +1)
    ##
    ###loop iterator variable
    ##i= 0
    ##
    ##while not fiveMinsFound == True:
    ##    while i < len(x):
    ##        if int(time.time()) - calendar.timegm(datetime.datetime.strptime(x[i]['created_at'],"%a %b %d %H:%M:%S +0000 %Y").utctimetuple()) <= 300:
    ##            lastFiveMinTweets.append(x[i])
    ##        else:
    ##            fiveMinsFound = True
    ##        i += 1
    ##    if fiveMinsFound == False:
    ##        x.append(t.statuses.home_timeline(count = RETRIEVE_COUNT +1, max_id = x[len(x) -1]['id'] - 1))

    iterator = twitter_stream.statuses.sample()

    StartTime = time.time()
    tweetCount = 0
    for tweet in iterator:
        if time.time() - StartTime > 300:
            break
        if 'text' in tweet:
            if not tweet['text'][2: 2] == "RT":
                lastFiveMinTweets.append(tweet)
    print("received x tweets: ", len(lastFiveMinTweets))
    debugStartTime = time.time()

    for tweet in lastFiveMinTweets:
        TempErrorCount = 0
        CorrectedErrors = []
        
        for word in tweet['text'].split():
            if word in misspellings:
                TempErrorCount += 1
                CorrectedErrors.append(misspellings[word])
        #Check for phrases here

        #Check for phrases here
        if TempErrorCount > 0:
            errorTweetsList.append(tweet)
            errorTweetsListErrors.append(CorrectedErrors)

    tweetScore = []
    j = 0
    for j in range(0, len(errorTweetsList)):
        tweetScore.append(errorTweetsList[j]['user']['followers_count'] * len(errorTweetsListErrors[j]))


    gap = len(tweetScore) // 2
    # loop over the gaps
    while gap > 0:
     # do the insertion sort
        for i in range(0, len(tweetScore) - gap):
            if tweetScore[i] < tweetScore[i + gap]:
                temp1 = tweetScore[i]
                temp2 = errorTweetsList[i]
                temp3 = errorTweetsListErrors[i]
             
                tweetScore[i] = tweetScore[i + gap]
                errorTweetsList[i] = errorTweetsList[i + gap]
                errorTweetsListErrors[i] = errorTweetsListErrors[i + gap]
             
                tweetScore[i + gap] = temp1
                errorTweetsList[i + gap] = temp2
                errorTweetsListErrors[i + gap] = temp3
        gap //= 2

    while True:
        actionTaken = False
        for i in range(0, len(tweetScore) - 1):
            if tweetScore[i] < tweetScore[i + 1]:
                temp1 = tweetScore[i]
                temp2 = errorTweetsList[i]
                temp3 = errorTweetsListErrors[i]
             
                tweetScore[i] = tweetScore[i + 1]
                errorTweetsList[i] = errorTweetsList[i + 1]
                errorTweetsListErrors[i] = errorTweetsListErrors[i + 1]
             
                tweetScore[i + 1] = temp1
                errorTweetsList[i + 1] = temp2
                errorTweetsListErrors[i + 1] = temp3
                actionTaken = True
        if actionTaken == False:
            break

##    print(len(tweetScore))
##    print(len(errorTweetsList))
##    print(len(errorTweetsListErrors))
##    print(time.time() - debugStartTime)
    for k in range(0, 1):
        print(tweetScore[k])
        print(errorTweetsList[k]['text'].encode('ascii', 'ignore'))
        print()
        outputString = "@" + errorTweetsList[k]['user']['screen_name'] + " I think you meant: "
        for error in list(OrderedDict.fromkeys(errorTweetsListErrors[k])):
            if len(outputString) + len(error) + 4 < 140:
                outputString = outputString + " *" + error + ", "
        print(outputString)
        t.statuses.update(status = outputString, in_reply_to_status_id = errorTweetsList[k]['id_str'], lat = (random.random() - .5) * 90, long = (random.random() - .5) * 180)
