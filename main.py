import base64
import tweepy
import requests

from dateutil import parser
from os import getenv


def twitter_auth_check_tweet(status):
    consumer_key = getenv("consumer_key")
    consumer_secret = getenv("consumer_secret")
    access_token = getenv("access_token")
    access_secret = getenv("access_secret")

    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_secret)

    api = tweepy.API(auth)
    api.update_status(status)
    print("Tweet length: " + str(len(status)))


def scoring(score):
    if 7 <= float(score) <= 8:
        return str(score + " ⚠")
    if 8 <= float(score) <= 9:
        return str(score + " 💣")
    if 9 <= float(score) <= 10:
        return str(score + " ☠")


def compose_data(req, header):
    json_resp = req.json()
    json_resp = json_resp[0]
    elements = (header, "CVE ID: " + json_resp['cve_id'], "CVSS Score: " + scoring(json_resp['cvss_score']), "URL: " + json_resp['url'], '#CyberSecurity', 'Hosted on @googlecloud')
    return '\n'.join(elements)


def choose_month(month):
    if month == '01' or month == '05' or month == '09':
        req = requests.get("http://www.cvedetails.com/json-feed.php?numrows=1&vendor_id=0&product_id=0&version_id=0&hasexp=0&opec=1&opov=0&opcsrf=0&opfileinc=0&opgpriv=0&opsqli=0&opxss=0&opdirt=0&opmemc=0&ophttprs=0&opbyp=0&opginf=0&opdos=0&orderby=2&cvssscoremin=8")
        header = ("🤖Beep Boop... if you want to reach exploit absolution,🤖\n<😈>try out this CVE on Code Execution.<😈>\n\n")
        status = compose_data(req, header)
        twitter_auth_check_tweet(status)
    if month == '02' or month == '06' or month == '10':
        req = requests.get("http://www.cvedetails.com/json-feed.php?numrows=1&vendor_id=0&product_id=0&version_id=0&hasexp=0&opec=0&opov=0&opcsrf=0&opfileinc=0&opgpriv=0&opsqli=1&opxss=0&opdirt=0&opmemc=0&ophttprs=0&opbyp=0&opginf=0&opdos=0&orderby=2&cvssscoremin=8")
        header = ("🤖Beep Boop... get your database some protection,🤖\n💉💾or it'll be pwned by SQL Injection!💉💾\n\n")
        status = compose_data(req, header)
        twitter_auth_check_tweet(status)
    if month == '03' or month == '07' or month == '11':
        req = requests.get("http://www.cvedetails.com/json-feed.php?numrows=1&vendor_id=0&product_id=0&version_id=0&hasexp=0&opec=0&opov=0&opcsrf=0&opfileinc=0&opgpriv=0&opsqli=0&opxss=0&opdirt=0&opmemc=0&ophttprs=0&opbyp=0&opginf=0&opdos=0&orderby=2&cvssscoremin=7")
        header = ("🤖Beep boop... I'm TweeVEBot, & you humans may not have heard this;🤖\n🖥️💣but there's a dangerous vuln, that causes Denial of Service:💣🖥️\n\n")
        status = compose_data(req, header)
        twitter_auth_check_tweet(status)
    if month == '04' or month == '08' or month == '12':
        req = requests.get("http://www.cvedetails.com/json-feed.php?numrows=1&vendor_id=0&product_id=0&version_id=0&hasexp=0&opec=0&opov=0&opcsrf=0&opfileinc=0&opgpriv=1&opsqli=0&opxss=0&opdirt=0&opmemc=0&ophttprs=0&opbyp=0&opginf=0&opdos=0&orderby=2&cvssscoremin=8")
        header = ("🤖Beep Boop... I'm a bot and my names TweeVE.🤖\n⏫🖥️did someone ask for a priv' esc. CVE?🖥️⏫\n\n")
        status = compose_data(req, header)
        twitter_auth_check_tweet(status)


def date_parser(context):
    timestamp = parser.isoparse(context.timestamp)
    return timestamp.strftime('%m')


def pubsub_trigger(event, context):
    print("""This Function was triggered by messageId {} published at {}""".format(context.event_id, context.timestamp))
    month = date_parser(context)
    choose_month(month)
