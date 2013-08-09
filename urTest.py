from twitter import *
import re
import time
import calendar
import datetime

t = Twitter(
            auth=OAuth("635651955-CMmg1DZjMkEWKEcpZ49CG8KzmwNw7IwublYrgVZZ", "CAiUYm7YFBK9bzk9XikA2ehm6irwkIbIzLqyyfbVQ",
                       "Hc89GpUxM0DVkTWdGKdw", "ZfkARmEJKFsEIFoAqqt5Ih85NMr3DKhgcOQ4eO3N9k")
           )
twitter_stream = TwitterStream(auth=OAuth("635651955-CMmg1DZjMkEWKEcpZ49CG8KzmwNw7IwublYrgVZZ", "CAiUYm7YFBK9bzk9XikA2ehm6irwkIbIzLqyyfbVQ",
                       "Hc89GpUxM0DVkTWdGKdw", "ZfkARmEJKFsEIFoAqqt5Ih85NMr3DKhgcOQ4eO3N9k")
                               )

iterator = twitter_stream.statuses.sample()

yourCount = 0
youreCount = 0

for tweet in iterator:
    if 'text' in tweet:
        if " ur " in tweet['text'] or " Ur " in tweet['text'] or " UR " in tweet['text']:
            print(tweet['text'].encode('ascii', 'ignore'))
            print(tweet['user']['screen_name'].encode('ascii', 'ignore'))
            if input("1 for your/2 for you're") == "1":
                yourCount += 1
            else:
                youreCount += 1
            print(yourCount, " ", youreCount)
