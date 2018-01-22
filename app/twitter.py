import tweepy

consumer_key = 'your_consumer_key'
consumer_secret = 'your_consumer_secret'
access_token = 'your_access_token
access_token_secret = 'your_access_token_secret'

def getNetflixUpdateFullText():
    # Make a handler
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)

    # Request access
    auth.set_access_token(access_token, access_token_secret)

    # Setting API
    api = tweepy.API(auth)

    updateFullText = []
    updateFullText.append('넷플릭스 업데이트 내역\n\n')

    tweets = api.user_timeline(id='netflixkr_up', count=5)
    for tweet in tweets:
        updateFullText.append('--------------------\n')
        updateFullText.append(tweet.text)
        updateFullText.append('\n\n')

    return ''.join(updateFullText).strip()
