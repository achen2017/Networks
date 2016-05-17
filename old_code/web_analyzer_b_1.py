from bs4 import BeautifulSoup
import requests
import json
from random import randint
import numpy as np
import scipy
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import networkx as nx
from scipy.spatial.distance import cosine
from itertools import permutations


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

    article_title_dump = []
    for item in article_dump:
        article_title_dump.append(item['Title'])

    article_pub_dump = []
    for item in article_dump:
        article_pub_dump.append(item['Publication'])

    words =[]
    for item in article_content_dump:
        for word in item:
            if word not in words:
                words.append(word)


    titles =[]
    for item in article_title_dump:
        if item not in titles:
            if item != '':
                titles.append(item)


    pubs =[]
    for item in article_pub_dump:
        if item not in pubs:
            pubs.append(item)


    word_arti = np.zeros((len(titles),len(words)))
    # word_arti = np.zeros((1000000,1000000))

    edgelist = []
##creates edgelist, a list of lists, where each of the lists contains [word, article title, # of words]
    wfile = open('party.csv', 'w')
    print('NewsOrg,Category,Perc', file=wfile)  #tells it to print just to wfile
    for i, word in enumerate(words):

        for j, title in enumerate(titles):
            temp = []
            temp.append(word)
            temp.append(title)
            for piece in article_dump:
                if piece['Title'] == title:
                    temp.append({'weight' : piece['Text'].count(word)})
                    word_arti[j][i] = piece['Text'].count(word)
                    tup = (temp[0],temp[1],temp[2])
                    print('"%s","%s","%d"' % (temp[1], temp[0], piece['Text'].count(word)), file=wfile) # put in %s (a string) and %d is a digit the % says, take the following info and put it into the previous ''
                    edgelist.append(tup)
    wfile.close()

    print("\n")








    # print(edgelist[0:2])
    ###uncommment this to show it
    # fig = plt.figure(figsize=(10,10))
    # ax = sns.heatmap(word_arti, yticklabels=words, xticklabels='')
    # ax.ytick_labels(rotation=90)
    # plt.show()

###########
    # G = nx.Graph()
    # G.add_edges_from(edgelist)
    # values = []
    # for n in G.nodes():
    #     if n in words:
    #         values.append(0.75)
    #     else:
    #         values.append(0.25)
    #     labels = dict([(k, v*100) for k,v in nx.get_edge_attributes(G, 'weight').items()])
    #
    #     nx.draw(G, cmap=plt.get_cmap('Accent'), node_color = values, edge_labels=labels)




#########
    # wfile = open('edgelist.csv', 'w')
    # print('Source,Target,Weight', file=wfile)
    # for k1, k2, wdict in edgelist:
    #     print(','.join([k1, k2, str(wdict['weight'])]), file=wfile)
    # wfile.close()




    # weighted_edges_a = []
    # for i1, i2 in permutations(range(len(titles)), 2):
    #     w = cosine(word_arti[i1], word_arti[i2])
    #     weighted_edges_a.append([titles[i1], titles[i2], w])
    #
    # print(weighted_edges_a[0])
    #
    #
    #
    #
    # wfile = open('weighted_edges_a.csv', 'w')
    # print('Source,Target,Weight', file=wfile)
    # for i,j,k in weighted_edges_a:
    #     print(','.join([i, j, str(k)]), file=wfile)
    # wfile.close()
    #
    # plt.hist([row[-1] for row in weighted_edges_a], bins = 14, color='steelblue')

main()
