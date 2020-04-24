#!/usr/bin/python3

import twitter
import os
from operator import attrgetter

tck = os.environ.get('TWITTER_CONSUMER_KEY')
tcs = os.environ.get('TWITTER_CONSUMER_SECRET')
tak = os.environ.get('TWITTER_ACCESS_KEY')
tas = os.environ.get('TWITTER_ACCESS_SECRET')
tsn = os.environ.get('TWITTER_FETCH_HANDLE')

if any(v is None for v in [tck, tcs, tak, tas, tsn]):
    raise ValueError("please make sure TWITTER_CONSUMER_KEY, TWITTER_CONSUMER_SECRET, TWITTER_ACCESS_KEY, TWITTER_ACCESS_SECRET, and TWITTER_FETCH_HANDLE are set and exported in environmental variables.")

api = twitter.Api(consumer_key=tck,
                  consumer_secret=tcs,
                  access_token_key=tak,
                  access_token_secret=tas,
                  sleep_on_rate_limit=True)
users = api.GetFollowers(screen_name=tsn)

users.sort(key=attrgetter('followers_count'), reverse=True)
print("".join(["@{}\t({})\t{}\n".format(u.screen_name, u.name, u.followers_count) for u in users]))
