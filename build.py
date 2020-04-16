import contextlib
from urllib.parse import urlencode
from urllib.request import urlopen, Request

from bs4 import BeautifulSoup


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
        return "None found"
    head, sep, tail = product_line.partition('">')
    trim = tail
    head, sep, tail = trim.partition('</a>')
    return head


def scoring(score):
    if 7 <= float(score) <= 8:
        return str(score + " ⚠")
    if 8 <= float(score) <= 9:
        return str(score + " 💣")
    if 9 <= float(score) <= 10:
        return str(score + " ☠")


def make_tiny(url):
    request_url = ('http://tinyurl.com/api-create.php?' + urlencode({'url':url}))
    with contextlib.closing(urlopen(request_url)) as response:
        return response.read().decode('utf-8')