
from bs4 import BeautifulSoup
import requests
import json
from random import randint
from nltk.corpus import stopwords
import re
from collections import Counter
import pylab as pl
import numpy as np
import matplotlib.pyplot as plt


file_name = 'Democratic Debateon22_04_2016at10_25_13.json'

#This function prints the histogram of some dictionary d.
def histogram(d):
    X = np.arange(len(d))
    pl.bar(X, d.values(), align='center', width=1)
    pl.xticks(X, d.keys(), rotation = 'vertical')
    ymax = max(d.values()) + 1
    pl.ylim(0, ymax)
    # bar.set_ylabel('Count')
    pl.show()




##This function plots a histogram of the top 5 common words of articles
def common_word_plots(a_file):
    # Open json file
    with open(a_file) as json_file:
        json_data = json.load(json_file)

        # print(json_data[1]['Title']) ##this is how we access data in the json


# We take articles words and then count how many times each word appears. We collect those words into a single dictionary where the key is the word and the value is the number of appearances eg: egg : 2.
    word_collector = []
    for item in json_data:
        word_collector.append(Counter(item['Text']))





# This bit of code collects most common words into a dictionary that's then stored in a list.
    count_a = 0
    common_dict = []
    for item in word_collector:
        common_dict.append(dict((x, y) for x, y in item.most_common(5)))
        count_a += 1

# Call the histogram plotting function
    histogram(common_dict[4])




###just for fun this function counts the size of the vocabularly
def vocab_size(word_collector):
    vocab = []

    for item in word_collector:
        vocab.append(len(item))
    return(vocab)


common_word_plots(file_name)
