import json
from collections import Counter



with open('trump_test_2.json', 'r') as wfile:
    article_dump = json.load(wfile)


    #in this block, we're creating a list of unique words.

all_words = []
for item in article_dump:
    for eachword in item['Text']:
        all_words.append(eachword)

wordset = set(all_words)          #all words includes repeats. converting to a set removes repeats
wlist = list(wordset)             #cast set as a list
            #THIS APPROACH CHANGES THE ORDER OF THE LIST (using set changes the order)


edgelist = []
z = len(wlist)

for word_a in wlist:
    temp = []
    # temp.append(word_a)
    a = wlist.index(word_a) + 1
    if a != z - 1:                       #checking that we're not at end of wlist
        portion_wlist = wlist[a:z]   #checking word_a against only the words that haven't been checked yet
        for word_b in portion_wlist:
            temp.extend([word_a, word_b])
            link_count = 0          #number of shared articles between word_a and word_b
            for article in article_dump:
                if (word_a in article['Text'])&(word_b in article['Text']): #feel free to suggest a more parsimonious solution
                    link_count += 1
                else:
                    link_count += 0
            temp.append(link_count)
            edgelist.append([temp])         #Note to abe: we can always convert to tuple by saying b = tuple(temp)
            temp = []
print(edgelist[3])
