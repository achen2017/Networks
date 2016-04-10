##testing2

import bs4
from bs4 import BeautifulSoup
import requests
# import feedparser
import json
import time
from google import search
from google import search_news
from google import get_page
from random import randint
# from googlesearch import GoogleSearch
# from pprint import pprint


article_content = open('article1google.json', 'w')

# Create the file inwhich to store the

links = []

article_holder = {'Title' : '' , 'Authors' : [], 'Text' : '', 'Date' : '', 'Publication' : 'New York Times'}


for url in search_news('beyonce formation nyt', stop = 10):
    links.append(url)

html = get_page(links[5])

soup = BeautifulSoup(html, 'html.parser')

print(soup)

print('\n')
print('\n')
print('\n')





#
# try:
#     target_site = requests.get(links[2])
# except requests.exceptions.ConnectionError:
#     print('something messed up')
#
# soup = bs4.BeautifulSoup(target_site.text, "lxml")
#
# title = soup.find('title')
# body = soup.find('body')
# print(title.text)




# gs = GoogleSearch("Bacon")
# for hit in gs.top_results():
#     print(hit)







print('\n')

########Writing article1 information to json
json.dump(article_holder, article_content, indent=4)
# print(article1)
