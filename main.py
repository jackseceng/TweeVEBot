import tweepy
import contextlib
from json import loads
from urllib.request import urlopen, Request
from urllib.parse import urlencode
from bs4 import BeautifulSoup


# Authenticate to Twitter
auth = tweepy.OAuthHandler("<>", "<>")
auth.set_access_token("<>", "<>")


def twitter_auth_check():
    api = tweepy.API(auth)
    try:
        api.verify_credentials()
        print("Authentication OK")
    except:
        print("Error during authentication")


def twitter_status_update_test(tweet):
    tweet = (tweet + "\n#CyberSecurity")
    print(tweet)
    print(len(tweet))


def twitter_status_update(tweet):
    tweet = (tweet + "\n#CyberSecurity")
    api = tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True)
    api.update_status(tweet)


def make_tiny(url):
    request_url = ('http://tinyurl.com/api-create.php?' + urlencode({'url':url}))
    with contextlib.closing(urlopen(request_url)) as response:
        return response.read().decode('utf-8')


def get_cves():
    tweet = ("Newest: CVE | CVSS(>=8) | Product | Sploits: \n\n")
    count = 0
    url = "http://www.cvedetails.com/json-feed.php?numrows=10&vendor_id=0&product_id=0&version_id=0&hasexp=0&opec=0&opov=0&opcsrf=0&opfileinc=0&opgpriv=0&opsqli=0&opxss=0&opdirt=0&opmemc=0&ophttprs=0&opbyp=0&opginf=0&opdos=0&orderby=1&cvssscoremin=8"
    json_req = urlopen(Request(url, headers={'User-Agent': 'Mozilla'}))
    data = loads(json_req.read().decode())
    for entry in data:
        cve_id = entry.get('cve_id')
        product = html_parse(cve_id)
        if len(product.split()) > 1:
            list = (product.split())
            product = (list[0])
        exploit_count = entry.get('exploit_count')
        cvss_score = entry.get('cvss_score')
        url = make_tiny(entry.get('url'))
        tweet = (tweet + cve_id + " | " + cvss_score + " | " + product + " | " + exploit_count + " | " + url + "\n")
        count = count + 1
        if count is 3:
            break
    return tweet


def html_parse(cve_id):
    url = "https://www.cvedetails.com/cve/" + cve_id
    f = urlopen(Request(url, headers={'User-Agent': 'Mozilla'}))
    soup = BeautifulSoup(f, 'html.parser')
    table = soup.find(lambda tag: tag.name == 'table' and tag.has_attr('id') and tag['id'] == "vulnprodstable")
    rows = table.find_all('td')
    buffer = []
    for item in rows:
        buffer.append(str(item))
    try:
        product_line = buffer[3]
    except:
        "IndexError: list index out of range"
        return "none"
    head, sep, tail = product_line.partition('">')
    trim = tail
    head, sep, tail = trim.partition('</a>')
    return head


if __name__ == '__main__':
    tweet = get_cves()
    twitter_auth_check()
    twitter_status_update_test(tweet)
    #twitter_status_update(tweet)
