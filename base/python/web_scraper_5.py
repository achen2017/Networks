
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
    # subject = str(sys.argv[1])
    subject = 'bill'
    date = time.strftime("%d_%m_%Y")
    the_time = time.strftime("%H_%M_%S")
    # article_content = open(subject + '_on_' + date + '_at_' + the_time + '.json', 'w')

    # Create the file inwhich to store the

    article_holder = {'Title' : '' , 'Authors' : [], 'Text' : '', 'Date' : '', 'Publication' : 'New York Times'}


    # articles_nyt = nyt(subject)   ##where we call NYT webscraper function and put it into a dict with other NYT content
    # articles_abc = abc(subject)
    article_dump = []

    # abc_list = abc(subject)
    # nyt_list = nyt(subject)
    # cnn_list = cnn(subject)
    # nbc_list = nbc(subject)

    # cbs_list = cbs(subject)

    # article_dump.extend(abc_list + nyt_list + cnn_list + nbc_list + hp_list + cbs_list)


    ####If you want to test, uncomment the below
    # hp_list = hp(subject)
    # article_dump.extend(hp_list)

    # print('number of ABC articles collected : ' + str(len(abc_list)))
    # print('number of New York Times articles collected : ' + str(len(nyt_list)))
    # print('number of CNN articles collected : ' + str(len(cnn_list)))
    # print('number of NBC articles collected : ' + str(len(nbc_list)))
    # print('number of Huffington Post articles collected : ' + str(len(hp_list)))
    # print('number of CBS articles collected : ' + str(len(cbs_list)))

    # json.dump(article_dump, article_content, indent=4)
    # conn = sqlite3.connect('db/example.db')
    # c = conn.cursor()
    # blahblah = [['2a','3a','4a','5a','5a'],['2b','3b','4b','5b','5a'],['2c','3c','4c','5c','5a'],['2c','3c','4c','5c','5a'],['2c','3c','4c','5c','5a']]



    ### in this block, we finally learn to create a table and insert values, including those of an array.
    blahblah = [['a','b','c','d','e'],['1','1','1','1','1']]
    # print(blahblah)

    conn = lite.connect("../db/development.sqlite3")
    cursor = conn.cursor()



    # truther = cursor.execute("""SELECT count(*) FROM sqlite_master WHERE type='table' AND name='Output';""")
    # if truther == 0:
    #     cursor.execute("""CREATE TABLE Output (modules text, mys_a text, mys_b text, node_id int, word text);""")
    #
    for item in blahblah:
        cursor.execute("INSERT INTO queries VALUES (1,'golden duck', 'description', 'info', ?, ?);", (date, the_time))
        conn.commit()



    #### and this is how we insert into a table created in Ruby
    # cursor.execute("INSERT INTO Directors VALUES ('2','name', 'bio', '03/09/1999', ' ','1','2')")
    #not that the entry must start with an int




    ##### This is how you write to a specific entry in a row created by but you have to commit()
    # cursor.execute("UPDATE Actors SET bio=('Hi World') WHERE name=('Tim Robbins');")



    cursor.execute("INSERT INTO queries VALUES (12019238109834,'golden duck', 'description', 'info', ?, ?);", (date, the_time))
    conn.commit()




    # test_array = 'blahblah'
    # print(str(test_array))








########################## THIS IS WHERE WE RUN MAIN ###########################
main()
###################################################################
