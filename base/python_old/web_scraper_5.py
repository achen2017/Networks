
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
import sys
import sqlite3 as lite


import shutil

def main():
    subject = str(sys.argv[1])
    subject = 'bill'
    date = time.strftime("%d_%m_%Y")
    the_time = time.strftime("%H_%M_%S")

    blahblah = [['alpha','b','c','d','e'],['uno','1','1','1','1']]
    conn = lite.connect("../db/development.sqlite3")
    cursor = conn.cursor()

    counter = int(sys.argv[2])
    for item in blahblah:
        counter += 1
        cursor.execute("INSERT INTO queries VALUES (?, ?, ?, ?, ?, ?);", (counter, item[0], item[1], item[2], date, the_time))
        conn.commit()





########################## THIS IS WHERE WE RUN MAIN ###########################
main()
###################################################################
