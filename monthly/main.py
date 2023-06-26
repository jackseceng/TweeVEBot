"""Module imports are explained below"""
import os # For getting environment information during runtime
import sys # For exiting after out of bounds during runtime
import requests # For making HTTP requests to CVE databases
import tweepy # Twitter library
from dateutil import parser # For parsing dates and times in event context
from google.cloud import secretmanager # For using GCP secret manager at runtime

project_id = os.environ["GCP_PROJECT"]
client = secretmanager.SecretManagerServiceClient()


def get_secrets(secret_request):
    """Grab secrets from GCP Secrets Manager"""
    name = f"projects/{project_id}/secrets/{secret_request}/versions/latest"
    response = client.access_secret_version(name=name)
    return response.payload.data.decode("UTF-8")


def twitter_auth_check_tweet(status):
    """Checks for auth to twitter API, then tweets if auth is successful"""
    consumer_key = get_secrets("twitter_consumer_key")
    consumer_secret = get_secrets("twitter_consumer_secret")
    access_token = get_secrets("twitter_access_token")
    access_secret = get_secrets("twitter_access_secret")

    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_secret)

    api = tweepy.API(auth)
    api.update_status(status)
    print("Tweet length: " + str(len(status)))


def scoring(score, event):
    """Adds emojis to score based on value"""
    if 7 <= float(score) <= 8:
        return str(score + " ⚠")
    if 8 <= float(score) <= 9:
        return str(score + " 💣")
    if 9 <= float(score) <= 10:
        return str(score + " ☠")
    else:
        print(f"""Error in scoring function. Triggering event: {event}""")
        sys.exit(1)


def compose_data(req, header, event):
    """Parses and formats json data from CVE feed"""
    json_resp = req.json()
    json_resp = json_resp[0]
    elements = (header, "CVE ID: " + json_resp['cve_id'], "CVSS Score: " + scoring(json_resp['cvss_score'], event),
                "URL: " + json_resp['url'], '#CyberSecurity', 'Hosted on @googlecloud')
    return '\n'.join(elements)


def choose_month(month, event):
    """Selects the type of vulnerability to tweet about based on the month of the year"""
    if month == '01' or month == '05' or month == '09':
        req = requests.get(
            "http://www.cvedetails.com/json-feed.php?numrows=1&vendor_id=0&product_id=0&version_id=0&hasexp=0&opec=1&opov=0&opcsrf=0&opfileinc=0&opgpriv=0&opsqli=0&opxss=0&opdirt=0&opmemc=0&ophttprs=0&opbyp=0&opginf=0&opdos=0&orderby=2&cvssscoremin=8", timeout=10)
        header = (
            "🤖Beep Boop... if you want to reach exploit absolution,🤖\n<😈>try out this CVE on Code Execution.<😈>\n\n")
        status = compose_data(req, header, event)
        twitter_auth_check_tweet(status)
    if month == '02' or month == '06' or month == '10':
        req = requests.get(
            "http://www.cvedetails.com/json-feed.php?numrows=1&vendor_id=0&product_id=0&version_id=0&hasexp=0&opec=0&opov=0&opcsrf=0&opfileinc=0&opgpriv=0&opsqli=1&opxss=0&opdirt=0&opmemc=0&ophttprs=0&opbyp=0&opginf=0&opdos=0&orderby=2&cvssscoremin=8", timeout=10)
        header = (
            "🤖Beep Boop... get your database some protection,🤖\n💉💾or it'll be pwned by SQL Injection!💉💾\n\n")
        status = compose_data(req, header, event)
        twitter_auth_check_tweet(status)
    if month == '03' or month == '07' or month == '11':
        req = requests.get(
            "http://www.cvedetails.com/json-feed.php?numrows=1&vendor_id=0&product_id=0&version_id=0&hasexp=0&opec=0&opov=0&opcsrf=0&opfileinc=0&opgpriv=0&opsqli=0&opxss=0&opdirt=0&opmemc=0&ophttprs=0&opbyp=0&opginf=0&opdos=0&orderby=2&cvssscoremin=7", timeout=10)
        header = (
            "🤖Beep boop... I'm TweeVEBot, & you humans may not have heard this;🤖\n🖥️💣but there's a dangerous vuln, that causes Denial of Service:💣🖥️\n\n")
        status = compose_data(req, header, event)
        twitter_auth_check_tweet(status)
    if month == '04' or month == '08' or month == '12':
        req = requests.get(
            "http://www.cvedetails.com/json-feed.php?numrows=1&vendor_id=0&product_id=0&version_id=0&hasexp=0&opec=0&opov=0&opcsrf=0&opfileinc=0&opgpriv=1&opsqli=0&opxss=0&opdirt=0&opmemc=0&ophttprs=0&opbyp=0&opginf=0&opdos=0&orderby=2&cvssscoremin=8", timeout=10)
        header = ("🤖Beep Boop... I'm a bot and my names TweeVE.🤖\n⏫🖥️did someone ask for a priv' esc. CVE?🖥️⏫\n\n")
        status = compose_data(req, header, event)
        twitter_auth_check_tweet(status)
    else:
        print(f"""Error in choose_month function. Triggering event: {event}""")
        sys.exit(1)


def date_parser(context):
    """Looks for date in context data"""
    timestamp = parser.isoparse(context.timestamp)
    return timestamp.strftime('%m')


def pubsub_trigger(event, context):
    """Trigger function from google cloud environment"""
    print(f"""This Function was triggered by messageId {context.event_id} published at {context.timestamp}""")
    month = date_parser(context)
    choose_month(month, event)
