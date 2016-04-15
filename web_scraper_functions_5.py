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

def rando():
    rando_num = randint(0 , 329)/101
    return rando_num


########Extract article_title
def get_title_nyt(article_request):
    article_soup = BeautifulSoup(article_request.text,'html.parser')
    try:
        article_title = article_soup.find("h1", {"class" : 'headline'}).text
    except AttributeError:
        article_title = article_soup.find("h1", {"itemprop" : 'headline'}).text
    return article_title

########Extract article_authors
def get_authors_nyt(article_request):
    article_author = article_request.text.split('<meta name="author" content="')
    article_author = article_author[1]
    article_author = article_author.split('" />')
    article_author = article_author[0]

    return article_author


def get_content_nyt(article_request):
    article_text = ''
    article_soup = BeautifulSoup(article_request.text,'html.parser')
    for part in article_soup.find_all("p", {"class" : 'story-body-text story-content'}):
        article_text += part.get_text()
    return article_text

##### NYT webscraper function
def nyt(query_subject):
    links = []
    for url in search_news(query_subject + ' site:https://www.nytimes.com', pause = rando(), stop = 5):
        links.append(url)

    article_list = []
    target_article = []

    for link in links:
        try:
            target_article.append(requests.get(link))

        except requests.exceptions.ConnectionError:
            print('something messed up')




    for request in target_article:
        article = {'Title' : '' , 'Authors' : [], 'Text' : '', 'Date' : '', 'Publication' : 'New York Times'}

        article['Title'] = get_title_nyt(request)
        article['Authors'] = get_authors_nyt(request)
        article['Text'] = get_content_nyt(request)

        article_list.append(article)

    return  article_list




############################    ABC News Functions
def get_content_abc(article_request):
    article_text=''
    article_soup = BeautifulSoup(article_request.text,'html.parser')

    for part in article_soup.find_all('p', {"itemprop" : 'articleBody'}):
        article_text += part.get_text()
    return article_text


##### ABC webscraper function
def abc(query_subject):
    links = []
    for url in search_news(query_subject + ' site:http://www.abcnews.com',  pause = rando(), stop = 5):
        links.append(url)

    article_list = []
    target_article = []

    for link in links:
        try:
            target_article.append(requests.get(link))

        except requests.exceptions.ConnectionError:
            print('something messed up')




    for request in target_article:
        article = {'Title' : '' , 'Authors' : [], 'Text' : '', 'Date' : '', 'Publication' : 'ABC News'}

        # article['Title'] = get_title_abc(request)
        # article['Authors'] = get_authors_abc(request)
        article['Text'] = get_content_abc(request)

        article_list.append(article)

    return  article_list


########################################

def get_content_cnn(article_request):
    article_text=''
    article_soup = BeautifulSoup(article_request.text,'html.parser')


#################   ##################   ########
#################   ##################   ########
    for part in article_soup.find_all('', {"class" : 'zn-body__paragraph'}):

        article_text += part.get_text()
    return article_text

def cnn(query_subject):
    links = []

#################   ##################   ########
#################   ##################   ########
    for url in search_news(query_subject + ' site:http://www.cnn.com/',  pause = rando(), stop = 5):
        links.append(url)

    article_list = []
    target_article = []

    for link in links:
        try:
            target_article.append(requests.get(link))

        except requests.exceptions.ConnectionError:
            print('something messed up')




    for request in target_article:
        article = {'Title' : '' , 'Authors' : [], 'Text' : '', 'Date' : '', 'Publication' : 'CNN'}

        # article['Title'] = get_title_abc(request)
        # article['Authors'] = get_authors_abc(request)
        article['Text'] = get_content_cnn(request)

        article_list.append(article)

    return  article_list
