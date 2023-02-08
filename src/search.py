"""Gets the search result based on search"""
from googlesearch import search
from youtubesearchpython import VideosSearch

GOOGLE = ['google', 'google search', 'ggl', 'googlesearch']
YOUTUBE = ['youtube', 'yt', 'you tube', 'ytb']
DUCKDUCKGO = ['duckduckgo', 'duck duck go', 'duck duckgo', 'duckduck go']


def search_engine(engine, query):
    """Returns the search results"""
    if engine.lower() in GOOGLE:
        links = [link for link in search(query, num=3, stop=3, pause=2)]
    elif engine.lower() in YOUTUBE:
        videosSearch = VideosSearch(query, limit=3)
        links = [link['link'] for link in videosSearch.result()['result']]
    return links


if __name__ == "__main__":
    print(search_engine("ggl", "cat"))
