"""Gets the search result based on search"""
from html.parser import HTMLParser

import requests


class LinkFinder(HTMLParser):
    """Override of the HTML Parser class"""

    def __init__(self):
        super().__init__()
        self.links = set()
        self.open = False

    def handle_starttag(self, tag, attrs):
        for attr, value in attrs:
            if attr == 'div':
                ...
        if self.open is True:
            if tag == 'a':
                for attr, value in attrs:
                    if attr == 'href' and value.startswith('http'):
                        self.links.add(value)
        else:
            pass

    def page_links(self):
        """returns parsed links"""
        return self.links

    def error(self, message):
        return str("error: " + message)


class SearchWrapper:
    """Provides the wrapper class for link finding functionality"""

    def __init__(self):
        self.search_urls = {
            "ggl": "https://google.com/search?q=\"|\"",
            "brv": "https://search.brave.com/search?q=|",
            "ddg": "https://duckduckgo.com/?q=|",
            "ytb": "https://www.youtube.com/results?search_query=|",
            "wki": "https://en.wikipedia.org/wiki/Special:Search?search=|"
        }
        self.prsr = LinkFinder()

    def get_links(self, search_engine, query):
        """Gets the links for the given search engine"""
        if search_engine in self.search_urls:
            prsr = LinkFinder()
            prsr.feed(requests.get(
                self.search_urls[search_engine], timeout=10).replace('|', query))
        else:
            return "Cannot find the query link to the search engine"


if __name__ == "__main__":
    srchwrpr = SearchWrapper()
