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

########Extract article_title
def get_title(article_request):
    article_title = article_request.text.split('<title>')
    article_title = article_title[1]
    article_title = article_title.split('</title>')
    article_title = article_title[0]
    article_title = article_title.rstrip(' - The New York Times')

    return article_title

########Extract article_authors
def get_authors(article_request):
    article_author = article_request.text.split('<meta name="author" content="')
    article_author = article_author[1]
    article_author = article_author.split('" />')
    article_author = article_author[0]

    return article_author


def get_content(article_request):
    article_soup = BeautifulSoup(article_request.text,'html.parser')
    article_text = article_soup.getText()
    return article_text



article_content = open('webscrapertwo.json', 'w')

# Create the file inwhich to store the

links = []

article_holder = {'Title' : '' , 'Authors' : [], 'Text' : '', 'Date' : '', 'Publication' : 'New York Times'}


for url in search_news('beyonce' + ' site:https://www.nytimes.com', stop = 5):
    links.append(url)

# x = len(links)
target_article = []


for link in links:
    try:
        target_article.append(requests.get(link))
        # print(article_link)
    except requests.exceptions.ConnectionError:
        print('something messed up')


y = 0

for request in target_article:
    article = {'Title' : '' , 'Authors' : [], 'Text' : '', 'Date' : '', 'Publication' : 'New York Times'}

    article['Title'] = get_title(request)
    article['Authors'] = get_authors(request)
    article['Text'] = get_content(request)

    json.dump(article, article_content, indent=4)

print(article['Text'])


print('\n')
print('\n')
print('\n')





#
# try:
#     target_site = requests.get(links[2])
# except requests.exceptions.ConnectionError:
#     print('something messed up')
#
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
