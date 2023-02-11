"""Gets the search result based on search"""
from googlesearch import search
from youtubesearchpython import VideosSearch

GOOGLE = ['google', 'google search', 'ggl', 'googlesearch']
YOUTUBE = ['youtube', 'yt', 'you tube', 'ytb']


def stringify_list(results):
    """Converts resultant list into readable form"""
    strres = ""
    for i, string in enumerate(results):
        strres += str(i+1)+". "+string+"\n"
    return strres


def search_engine(engine, query):
    """Returns the search results"""
    if engine.lower() in GOOGLE:
        links = [link for link in search(query, num=3, stop=3, pause=2)]
    elif engine.lower() in YOUTUBE:
        videos_search = VideosSearch(query, limit=3)
        links = [link['link'] for link in videos_search.result()['result']]
    return stringify_list(links)


if __name__ == "__main__":
    print(search_engine("ggl", "cat"))
