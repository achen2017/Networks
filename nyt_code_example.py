'''
File: nyt_code_example.py
Author: Adam Pah
Description: 
This program scrapes the NYT RSS feed for articles
'''

#Standard path imports
#This is where I put imports that don't need to be installed with pip 
#(basically the parts of python that come pre-installed)
from __future__ import division, print_function
import argparse
import json
import hashlib

#Non-standard imports
#Here's where I put things that need to be installed by someone else
import feedparser
import bs4
import requests

#Global directories and variables

def extract_title(article):
    article_title = article.text.split('<title>')
    article_title = article_title[1]
    article_title = article_title.split('</title>')
    article_title = article_title[0]
    article_title = article_title.rstrip(' - The New York Times')
    return article_title

def extract_authors(article):
    author_list = []

    article_author = article.text.split('<meta name="author" content="')
    article_author = article_author[1]
    article_author = article_author.split('" />')
    article_author = article_author[0]

    author_list.append(article_author)
    return author_list

def extract_text(article):
    pass

def extract_date(article):
    article_date = article.text.split('"DISPLAYDATE" content="')
    article_date = article_date[1]
    article_date = article_date.split('" />')
    article_date = article_date[0]
    return article_date

def main(args):
    #I like ot put things in functions
    #The main function will actually hold the brain of the code (it handles all the in and out data flows)
    articles = feedparser.parse('http://rss.nytimes.com/services/xml/rss/nyt/Europe.xml')['entries']
    for target_article in articles:
        article_link = target_article['link']
        try:
            article = requests.get(article_link)
            # print(article_link)
        except requests.exceptions.ConnectionError:
            print('something messed up')
        article_dict = {'Title' : '' , 'Authors' : [], 'Text' : '', 'Date' : '', 'Publication' : 'New York Times'}
        article_dict['Title'] = extract_title(article)
        article_dict['Authors'] = extract_authors(article)
        article_dict['Date'] = extract_date(article)
        #Convert the dictionary to a string
        json_string = json.dumps(article_dict)
        #Create a unique name - i do that with a hash of the dictionary (always unique to the content)
        wfname = hashlib.md5(json_string.encode('utf-8')).hexdigest()
        with open('data/' + wfname + '.json', 'w') as wfile:
            print(json_string, file=wfile)

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="")
    args = parser.parse_args()
    main(args)
