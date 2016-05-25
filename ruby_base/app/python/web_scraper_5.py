
from bs4 import BeautifulSoup
import requests
import json
import time
from google import search
from google import search_news
from google import get_page
from random import randint
from web_scraper_functions_5 import nyt, abc, cnn, nbc, hp, cbs
import time
from gensim import corpora, models
import gensim


def main():
    subject = input("what do you want to look up? ")
    date = time.strftime("%d_%m_%Y")
    the_time = time.strftime("%H_%M_%S")
    article_content = open(subject + '_on_' + date + '_at_' + the_time + '.json', 'w')

    # Create the file inwhich to store the

    article_holder = {'Title' : '' , 'Authors' : [], 'Text' : '', 'Date' : '', 'Publication' : 'New York Times'}


    # articles_nyt = nyt(subject)   ##where we call NYT webscraper function and put it into a dict with other NYT content
    # articles_abc = abc(subject)
    article_dump = []

    abc_list = abc(subject)
    nyt_list = nyt(subject)
    cnn_list = cnn(subject)
    nbc_list = nbc(subject)
    hp_list = hp(subject)
    cbs_list = cbs(subject)

    article_dump.extend(abc_list + nyt_list + cnn_list + nbc_list + hp_list + cbs_list)

    print('number of ABC articles collected : ' + str(len(abc_list)))
    print('number of New York Times articles collected : ' + str(len(nyt_list)))
    print('number of CNN articles collected : ' + str(len(cnn_list)))
    print('number of NBC articles collected : ' + str(len(nbc_list)))
    print('number of Huffington Post articles collected : ' + str(len(hp_list)))
    print('number of CBS articles collected : ' + str(len(cbs_list)))

    json.dump(article_dump, article_content, indent=4)







########################## THIS IS WHERE WE RUN MAIN ###########################
main()
###################################################################
