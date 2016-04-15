##testing2

import bs4
from bs4 import BeautifulSoup
import requests

import json
import time
from google import search
from google import search_news
from google import get_page
from random import randint
from web_scraper_functions_4 import nyt, abc



def main():
    article_content = open('webscraperthree.json', 'w')

    # Create the file inwhich to store the

    article_holder = {'Title' : '' , 'Authors' : [], 'Text' : '', 'Date' : '', 'Publication' : 'New York Times'}

    subject = input("what do you want to look up? ")
    articles_nyt = nyt(subject)   ##where we call NYT webscraper function and put it into a dict with other NYT content
    articles_abc = abc(subject)
    article_dump = []
    article_dump.extend(articles_abc + articles_nyt)


    # json.dump(articles_nyt, article_content, indent=4)
    # json.dump(articles_abc, article_content, indent=4)
    json.dump(article_dump, article_content, indent=4)





########################## THIS IS WHERE WE RUN MAIN ###########################
main()
###################################################################
