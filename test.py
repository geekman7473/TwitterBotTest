from twitter import *
import re

#possible data flow
#1. check recent tweets from those i am following
#   1a. if a tweet contains an error add it to the temp list
#2. Check statuses.sample tweets
#   2a. If a tweet contains an error add it to the temp List
#3. assign score to all tweets in the temp list
#   3a. followers * errors + retweets
#   3b. Sort list based on score
#4. wait until the next time % 5 minutes == 0
#5. Post replies to top 5-10 tweets

# see "Authentication" section below for tokens and keys
t = Twitter(
            auth=OAuth("635651955-CMmg1DZjMkEWKEcpZ49CG8KzmwNw7IwublYrgVZZ", "CAiUYm7YFBK9bzk9XikA2ehm6irwkIbIzLqyyfbVQ",
                       "Hc89GpUxM0DVkTWdGKdw", "ZfkARmEJKFsEIFoAqqt5Ih85NMr3DKhgcOQ4eO3N9k")
           )
RETRIEVE_COUNT = 199
listOftweets = []
x = t.statuses.home_timeline(count = RETRIEVE_COUNT +1)
while 0 == 0:
    for z in range(0, len(x)):
        try:
            # UCS-4
            highpoints = re.compile(u'[\U00010000-\U0010ffff]')
        except re.error:
            # UCS-2
            highpoints = re.compile(u'[\uD800-\uDBFF][\uDC00-\uDFFF]')
            # mytext = u'<some string containing 4-byte chars>'
        listOftweets.append(x[z])
        mytext1 = highpoints.sub(u'\u25FD',x[z]['text'])
        mytext2 = highpoints.sub(u'\u25FD',x[z]['user']['screen_name'])
        print(mytext1.encode('ascii', 'ignore'))
        print(mytext2)
        print(z)
        wait = input("...")
    x = t.statuses.home_timeline(count = RETRIEVE_COUNT +1, max_id = x[len(x) -1]['id'] - 1)
##twitter_stream = TwitterStream(auth=OAuth("635651955-CMmg1DZjMkEWKEcpZ49CG8KzmwNw7IwublYrgVZZ", "CAiUYm7YFBK9bzk9XikA2ehm6irwkIbIzLqyyfbVQ",
##                       "Hc89GpUxM0DVkTWdGKdw", "ZfkARmEJKFsEIFoAqqt5Ih85NMr3DKhgcOQ4eO3N9k")
##                               )
##iterator = twitter_stream.statuses.sample()
##for tweet in iterator:
##    print(tweet['text'])
##    print(tweet['user']['screen_name'])

# Get your "home" timeline
#t.statuses.home_timeline()

# Get a particular friend's timeline
#t.statuses.friends_timeline(id = "LAZmanian_devil")

# Also supported (but totally weird)
#t.statuses.friends_timeline.LAZmanian_devil()

# Update your status
#t.statuses.update(
#status="Using @sixohsix's sweet Python Twitter Tools.")

# Send a direct message
#t.direct_messages.new(
#    user="LAZmanian_devil",
#    text="I think yer swell!")

# Get the members of tamtar's list "Things That Are Rad"
#t._("tamtar")._("things-that-are-rad").members()

# Note how the magic `_` method can be used to insert data
# into the middle of a call. You can also use replacement:
#t.user.list.members(user="tamtar", list="things-that-are-rad")

# An *optional* `_timeout` parameter can also be used for API
# calls which take much more time than normal or twitter stops
# responding for some reasone
#t.users.lookup(screen_name=','.join(A_LIST_OF_100_SCREEN_NAMES), _timeout=1)
