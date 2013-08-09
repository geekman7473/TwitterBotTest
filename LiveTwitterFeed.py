from twitter import *
import re
import time
import calendar
import datetime


twitter_stream = TwitterStream(auth=OAuth("635651955-CMmg1DZjMkEWKEcpZ49CG8KzmwNw7IwublYrgVZZ", "CAiUYm7YFBK9bzk9XikA2ehm6irwkIbIzLqyyfbVQ",
                       "Hc89GpUxM0DVkTWdGKdw", "ZfkARmEJKFsEIFoAqqt5Ih85NMr3DKhgcOQ4eO3N9k")
                               )

iterator = twitter_stream.statuses.sample()

try:
    # UCS-4
    highpoints = re.compile(u'[\U00010000-\U0010ffff]')
except re.error:
    # UCS-2
    highpoints = re.compile(u'[\uD800-\uDBFF][\uDC00-\uDFFF]')

for tweet in iterator:
    if 'text' in tweet:
        print(highpoints.sub(u'\u25FD',tweet['text']).encode('ascii', 'ignore'))
        print(highpoints.sub(u'\u25FD',tweet['user']['screen_name']).encode('ascii', 'ignore'))
        print(tweet['created_at'])
        print("")
        input("PRESS ENTER TO CONTINUE.")
