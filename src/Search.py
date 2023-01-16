import re
import requests
from urllib import parse
from bs4 import BeautifulSoup
from html.parser import HTMLParser


class LinkFinder(HTMLParser):
    def __init__(self):
        super().__init__()
        self.links = set()
        self.open = False

    def handle_starttag(self, tag, attrs):
        for attr, value in attrs:
            if attr == 'div':
                ...
        if self.open == True:
            if tag == 'a':
                for attr, value in attrs:
                    if attr == 'href' and value.startswith('http'):
                        self.links.add(value)
        else:
            pass

    def page_links(self):
        return self.links


searchUrls = {
    "ggl": "https://google.com/search?q=\"|\"",
    "brv": "https://search.brave.com/search?q=|",
    "ddg": "https://duckduckgo.com/?q=|",
    "ytb": "https://www.youtube.com/results?search_query=|",
    "wki": "https://en.wikipedia.org/wiki/Special:Search?search=|"
}
prsr = LinkFinder()
prsr.feed(requests.get(searchUrls["ggl"].replace('|', "cat")).text)
res = prsr.page_links()
print(res)
