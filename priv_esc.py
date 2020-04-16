import build
import json
from urllib.request import urlopen, Request


def compose():
    url = "http://www.cvedetails.com/json-feed.php?numrows=1&vendor_id=0&product_id=0&version_id=0&hasexp=0&opec=0&opov=0&opcsrf=0&opfileinc=0&opgpriv=1&opsqli=0&opxss=0&opdirt=0&opmemc=0&ophttprs=0&opbyp=0&opginf=0&opdos=0&orderby=2&cvssscoremin=8"
    json_req = urlopen(Request(url, headers={'User-Agent': 'Mozilla'}))
    data = json.loads(json_req.read().decode())
    tweet = ("🤖Beep Boop... I'm a bot and my names TweeVE.🤖\n⏫🖥️did someone ask for a priv' esc. CVE?🖥️⏫\n\n")
    for entry in data:
        cve_id = entry.get('cve_id')
        cvss_score = build.scoring(entry.get('cvss_score'))
        url = build.make_tiny(entry.get('url'))
        product = build.html_parse(cve_id)
        tweet = (tweet + "ID: " + cve_id + "\nScore: " + cvss_score + "\nProduct: " + product + "\n" + url + "\n\n#CyberSecurity")
        return tweet
