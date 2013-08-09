from twitter import *
import re
import time
import calendar
import datetime

t = Twitter(
            auth=OAuth("635651955-CMmg1DZjMkEWKEcpZ49CG8KzmwNw7IwublYrgVZZ", "CAiUYm7YFBK9bzk9XikA2ehm6irwkIbIzLqyyfbVQ",
                       "Hc89GpUxM0DVkTWdGKdw", "ZfkARmEJKFsEIFoAqqt5Ih85NMr3DKhgcOQ4eO3N9k")
           )
RETRIEVE_COUNT = 99
maxId = 0
x = []

while 1 == 1:
    if maxId == 0:
        x = t.search.tweets(q = "%232013jambo", count = RETRIEVE_COUNT + 1)
    else:
        maxId = 1
        x = t.search.tweets(q = "%232013jambo", count = RETRIEVE_COUNT + 1, max_id = x[len(x)-1]['id'] - 1)
    print(x)
    wait = input("...")
    for tweet in x:
        print(tweet.encode('ascii', 'ignore'))
        wait = input("...")
##        if ' dam ' in tweet['text']:
##            print(tweet['text'].encode('ascii', 'ignore'))
##            print(tweet['user']['screen_name'].encode('ascii', 'ignore'))
##            wait = input("...")
