##testing

import bs4
import requests
import feedparser
import json

# Create the file inwhich to store the
article_content = open('article1.json', 'w')


# get link for target article from the rss feed collector page

target_article_rss = feedparser.parse('http://rss.nytimes.com/services/xml/rss/nyt/Europe.xml')['entries']

# get link from target_article_rss
article_link = target_article_rss[0]['link']
try:
    target_article = requests.get(article_link)
    # print(article_link)
except requests.exceptions.ConnectionError:
    print('something messed up')


article1 = {'Title' : '' , 'Authors' : [], 'Text' : '', 'Date' : '', 'Publication' : 'New York Times'}

########Extract article_title
article_title = target_article.text.split('<title>')
article_title = article_title[1]
article_title = article_title.split('</title>')
article_title = article_title[0]
article_title = article_title.rstrip(' - The New York Times')


article1['Title'] = article_title

# print(article1['Title'])


########Extract article_authors
author_list = []

article_author = target_article.text.split('<meta name="author" content="')
article_author = article_author[1]
article_author = article_author.split('" />')
article_author = article_author[0]

author_list.append(article_author)
## need to write code to deal with multiple authors. These authors are just written as a single line eg "Abe Chen, Bob Apter, and Allen Schwarzenager"

article1['Authors'] = author_list



#######Extract article_content
article_text_rough = []
article_text_lessrough = []
article_text_list = []

article_text_semisplit = []
article_text_split = []
article_text_whole = []

article_text_rough = target_article.text.split('<p class="story-body-text story-content" data-para-count="')

article_text_rough.pop(0)


####this isn't set up correctly because if ''<dsfds><sdfsdf>text text text" then it will delete the text.
for text_paragrapha in article_text_rough:
    text_paragrapha = text_paragrapha.split('>')
    article_text_semisplit.extend(text_paragrapha)



for text_paragraphb in article_text_semisplit:
    text_paragraphb = text_paragraphb.split('<')
    article_text_split.extend(text_paragraphb)


print(article_text_split)


# del article_text_split[0::2]



######$$$$$$
# for text_paragrapha in article_text_rough:
#     text_paragrapha = text_paragrapha.split('">')
#     text_paragrapha.pop(0)
#     article_text_lessrough.extend(text_paragrapha)
#
# for text_paragraphb in article_text_lessrough:
#     article_text_list.append(text_paragraphb.split('</p>')[0])
#
# article_text = " ".join(str(x) for x in article_text_list)
#
# article1['Text'] = article_text
######$$$$$$


###### Fetching the Date
article_date = target_article.text.split('"DISPLAYDATE" content="')
article_date = article_date[1]
article_date = article_date.split('" />')
article_date = article_date[0]

article1['Date'] = article_date


########Writing article1 information to json
json.dump(article1, article_content, indent=4)
# print(article1)
