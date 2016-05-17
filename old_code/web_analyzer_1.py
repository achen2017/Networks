from bs4 import BeautifulSoup
import requests
import json

from random import randint
import time
from gensim import corpora, models, similarities
import gensim
import numpy
import scipy

def main():
    with open('trump_test.json', 'r') as wfile:
        article_dump = json.load(wfile)

    analyzer(article_dump)

def normalizer(special_array):

    sum = 0
    final_array = []
    for item in special_array:
        sum = sum + item[1]

        for item in special_array:
            norm_val = item[1]/sum
            final_array.append((item[0],norm_val))

    return(final_array)



def analyzer(article_dump):
    article_content_dump = []

    for item in article_dump:
        article_content_dump.append(item['Text'])


    lda_dictionary = corpora.Dictionary(article_content_dump)
##########


    ###########
    corpus = [lda_dictionary.doc2bow(text) for text in article_content_dump]

    corpus_norm =[]
    for item in corpus:
        corpus_norm.append(normalizer(item))

    ldamodel = gensim.models.ldamodel.LdaModel(corpus_norm, num_topics=5, id2word = lda_dictionary, passes=20)

    # print(corpus_norm)
    print("\n")



main()
