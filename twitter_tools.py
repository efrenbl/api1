from models import Person
import tweepy
from datetime import datetime, date, time, timedelta

people = []

def twitter(screen_name):
    for person in people:
        if person.screen_name == screen_name:
            return person.__dict__

    api = get_api()

    user = None
    try:
        user = api.get_user(screen_name)
    except tweepy.error.TweepError:
        return {"Error":"Username Not Found"}
    tweets_count = user.statuses_count
    account_created_date = user.created_at
    followers_count = user.followers_count
    days = (datetime.utcnow() - account_created_date).days

    timeline = []
    for status in tweepy.Cursor(api.user_timeline, screen_name='@'+screen_name).items():
        timeline.append({"text":status._json["text"],"created_at":status._json["created_at"]})

    avg = float(tweets_count)/float(days)
    person = Person(screen_name,tweets_count,followers_count,days,timeline,avg)
    people.append(person)
    return person.__dict__

def get_api():
    consumer_key = 'jU1aiOcKjozJohtpjlUXCPMMA'
    consumer_secret = '0Ld6lCznXHW9S9YOqFR42OHD14wDN1HIbtZ6SDfWgoEqPCOuZZ'

    access_token = '1069129831-Noke5p9DQWN2nTUtfIPzsIytPqPrvyQ6QnpnVTb'
    access_token_secret = 'o7NqDtwj0axELYRSWv4ypPXyKZhTlxGHV3ILP5TKsrkSt'

    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)

    return tweepy.API(auth)