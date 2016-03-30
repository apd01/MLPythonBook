import bs4
import feedparser
import json
from pprint import pprint

with file('rss_list.txt', 'r') as rss_file_list:
    items = json.load(rss_file_list)
    for url in items["sources"]:
        print(url)
        d = feedparser.parse(url)
        pprint(d, depth=4)
    with file('tmprss.txt', 'w') as outfile:

    # What is this file for?
    # Identify news stories as they happen, perhaps feed into an algorithm to predict front-page mma news?
