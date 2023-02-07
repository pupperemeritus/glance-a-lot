"""Gets the search result based on search"""
from html.parser import HTMLParser

import requests


class LinkFinder(HTMLParser):
    """Override of the HTML Parser class"""

    def __init__(self, maindivtag):
        super().__init__()
        self.links = set()
        self.open = False
        self.divcounter = 0
        self.maindivencounter = -1
        self.maindivtag = maindivtag

    def handle_starttag(self, tag: str, attrs) -> None:
        if tag == 'div':
            self.divcounter += 1
            for attr, value in attrs:
                if attr == 'id' and value == self.maindivtag:
                    self.maindivencounter = self.divcounter
        if self.open is True:
            if tag == 'a':
                for attr, value in attrs:
                    if attr == 'href' and value.startswith('http'):
                        self.links.add(value)

    def handle_endtag(self, tag: str) -> None:
        if tag == 'div':
            self.divcounter -= 1
            if self.divcounter == self.maindivencounter:
                self.open = False

    def page_links(self):
        """returns parsed links"""
        return self.links

    def error(self, message):
        return str("error: " + message)


class SearchWrapper:
    """Provides the wrapper class for link finding functionality"""

    def __init__(self):
        self.divid = {
            "ggl": "main"
        }
        self.search_urls = {
            "ggl": "https://google.com/search?q=\"|\"",
            "brv": "https://search.brave.com/search?q=|",
            "ddg": "https://duckduckgo.com/?q=|",
            "ytb": "https://www.youtube.com/results?search_query=|",
            "wki": "https://en.wikipedia.org/wiki/Special:Search?search=|"
        }

    def get_links(self, search_engine, query):
        """Gets the links for the given search engine"""
        if search_engine in self.search_urls:
            prsr = LinkFinder(self.divid[search_engine])
            try:
                prsr.feed(requests.get(
                    self.search_urls[search_engine].replace('|', query), timeout=10).text)
                return prsr.page_links()
            except TimeoutError:
                return "error fetching links"
        else:
            return "Cannot find the query link to the search engine"


if __name__ == "__main__":
    srchwrpr = SearchWrapper()
    res = srchwrpr.get_links("ggl", "cat")
    print(res)
