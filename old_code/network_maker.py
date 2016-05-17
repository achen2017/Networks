import json
from collections import Counter
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import networkx as nx
import csv
import os


file_name = "nu_more"  # this is future file name
pajek_name = 'another_test' # this is the pajek's name
numb_most = 500   #sets how many words go into the network. It can definitely handle 500

infomap_command = "../packages/Infomap/Infomap pajeks/another_test.net pajeks/term/ -N 10 --tree --bftree" ### #change we have to change the paths used here
with open('jsons/nu_dorm_attack.json', 'r') as wfile: # this is file pulled
    article_dump = json.load(wfile)



# In this block, we're creating a list of unique words. Based off of words that are most frequently used in the corpus.
# limiting to most common words may not be necessary given the limits of the corpus (just the lede)
all_words = []
for item in article_dump:
    for eachword in item['Text']:
        all_words.append(eachword)


counted_words = Counter(all_words)

common_words = counted_words.most_common(numb_most)

wlist = []
for item in common_words:
    wlist.append(item[0])   #wlist is a list of top numb_most most frequently used words in all the articles

zero_matrix = np.zeros((numb_most, numb_most))  # this Zero_matrix is one way of writing the edgelist. It's a giant two dimensional matrix where each side is a word and the weights linking two words is written into the entries




## in the following block, we make the network links
temp = []
edgelist = []
z = len(wlist)

for i, word_a in enumerate(wlist):
    a = i + 1
    if a != z - 1:                       #checking that we're not at end of wlist
        portion_wlist = wlist[a:z]   #checking word_a against only the words that haven't been checked yet
        for word_b in portion_wlist:
            temp.extend([word_a, word_b])
            link_count = 0          #number of shared articles between word_a and word_b
            j = wlist.index(word_b)
            for article in article_dump:
                if (word_a in article['Text'])&(word_b in article['Text']): #feel free to suggest a more parsimonious solution
                    link_count += 1
                else:
                    link_count += 0
            temp.append({'weight' : link_count})
            zero_matrix[i][j] = link_count
            edgelist.append(temp)         #Note: we can always convert to tuple via b = tuple(temp)
            temp = []

# next we normalize the weights of the zero_matrix network. We can easily impliment for edgelist.
sum_all = 0
for item in zero_matrix:
    sum_all += sum(item)
print(sum_all)

for i, line in enumerate(zero_matrix):
    for j, row in enumerate(line):
        zero_matrix[i][j] = zero_matrix[i][j]/sum_all



#Creates a list that can be easily transmitted into CSV
clean_list = []
for item in edgelist:
    clean_list.extend([[item[0],item[1],item[2]['weight']]])

myfile = open('clean_data_' + file_name + '.csv', 'w')
myfile.write('Target,Source,Weight' + '\n')
for item in clean_list:
    myfile.write(item[0] + ',' + item[1] + ',' + str(item[2]) + '\n')

myfile.close

#here we write graph data into pajek form from edgelist, which can be used by infomap to do more network analysis
G = nx.Graph()
G.add_edges_from(edgelist)
nx.write_pajek(G,'pajeks/' + pajek_name + '.net')   ### #change would have to change

#here, we're executing infomap in the shell to get infomap's capability (access to modularity)
os.system(infomap_command)



### This block takese the .tree output of infomaps and turns it into an array,
### where each each element contains information about each node. Information is:
### module name in the form "1:2" where 1 is larger module, and 2 is smaller module
### then there are two items that I don't understand and a final entry that is the id of the node.
### This should be turned into a #function later
key_name = 'another_test'
tree_text = open('pajeks/tell/' + key_name +'.tree').readlines()    ### #change, should change dynamically

line_array = []
final_array = []
for line in tree_text:
    counter += 1
    line_array.append([line])

del line_array[0:2]

for item in line_array:
    item = item[0].split(" ")
    item[3] = item[3].rstrip('\n')
    item[3] = int(item[3])
    final_array.append(item)

print(final_array[0:10])




### this block open the pajeks file back up, and reads it (we probably don't need to write Pajeks to a file)
node_net = open('pajeks/' + key_name +'.net').readlines()
node_array = []
for line in node_net:
    node_array.append(line.split(' '))


del node_array[0]




### this block appends the actual name of the node (a word) to the end of the item in final_array
### that contains the module information.
complete_array =[]
for item_final in final_array:

    for item_node in node_array[0:len(final_array)]:
        item_node[0] = int(item_node[0])
        if item_final[-1] == item_node[0]:
            item_final.append(item_node[1])
            complete_array.append(item_final)

### complete_array's elements look like this:
### ['14:4', '0.00643449', '"0.0"', 417, 'said']
### 14 in the first element of the above is the major module, and 4 is the submodule
### the second, third, and fourth modules mean something that I don't care about
### and the 'said' is the name of the node with the given modularity
