##testing2

import bs4
import requests
import feedparser
import json
import time
from google import search
from random import randint

article_content = open('article1google.json', 'w')

# Create the file inwhich to store the



article_holder = {'Title' : '' , 'Authors' : [], 'Text' : '', 'Date' : '', 'Publication' : 'New York Times'}


# get link for target article from the rss feed collector page

for url in search ('goats', stop=100):
    sleeper = (randint(0,5)/10)
    print(url)
    time.sleep(sleeper)




# get link from target_article_rss






print('\n')
########Writing article1 information to json
json.dump(article_holder, article_content, indent=4)
# print(article1)
