import json
import tweepy
import optparse

import code_exec
import ddos
import priv_esc
import sqli


def twitter_auth_check():
    api = tweepy.API(auth)
    try:
        api.verify_credentials()
        print("Authentication OK")
    except:
        print("Error during authentication")


def twitter_status_update_test(status):
    print(status)
    print(len(status))


def twitter_status_update(status):
    api = tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True)
    api.update_status(status)


def get_creds():
    auth_json = json.load(open('auth.json'))
    for c in auth_json:
        auth1 = c['cred1']
        auth2 = c['cred2']
        auth3 = c['cred3']
        auth4 = c['cred4']

    return [auth1, auth2, auth3, auth4]


def compose_tweet(month):
    if month == 0:
        return code_exec.compose()
    if month == 1:
        return sqli.compose()
    if month == 2:
        return ddos.compose()
    if month == 3:
        return priv_esc.compose()


if __name__ == '__main__':
    parser = optparse.OptionParser()
    parser.add_option('-m',
                      action="store", dest="month",
                      help="query string", default="spam")
    options, args = parser.parse_args()
    month = int(options.month)

    creds = get_creds()
    auth = tweepy.OAuthHandler(creds[0], creds[1])
    auth.set_access_token(creds[2], creds[3])
    tweet = compose_tweet(month)
    twitter_auth_check()
    #twitter_status_update_test(tweet)
    twitter_status_update(tweet)
