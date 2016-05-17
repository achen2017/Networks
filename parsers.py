class Document(object):
    '''
    Class parser for a LexisNexis document
    '''

    def __init__(self, docname):
        '''
        Parses the document and opens it up
        '''
        #Initials
        self.docname = docname
        self.doctext = open(docname).read()
        self.doclines = self.doctext.split('\n')
        #To fill
        #Annotated line indices
        self.annoline_indices = []
        #Main text, str, single line
        self.maintext = ''
        #Alll words in actual text
        self.words = []
        #Stem the words
        self.stem_words = []
        #Capitalized keywords
        self.keywords = {}
        #Date of article
        self.date = None
        #Parse it up
        self.parse_document()

    def parse_document(self):
        '''
        Parses the text
        '''
        from stemming.porter2 import stem
        #Pull out the annotations
        self.annoline_indices = self.pull_keywords()
        #Pull out the maintext
        self.maintext_puller()
        #Create the bag of words
        self.bag_of_words_creation()
        #Stem the words
        ##Important
        self.stem_words = [stem(w) for w in self.words]
        #Get the date
        self.date = self.get_date()

    def pull_keywords(self):
        '''
        Pull the keywords
        '''
        annotation_lines = []
        for i, line in enumerate(self.doclines):
            first_word = line.split(' ')[0]
            if ':' in first_word and first_word.isupper():
                #Set the keywords
                self.keywords[first_word.strip(':')] = line.split(' ')[1:]
                #Set the annotation given the enumerated line
                annotation_lines.append(i)
        return annotation_lines


    def maintext_puller(self):
        '''
        pulls out the maintext
        '''
        #Get the largest gap between annotated lines, this will be the main text
        import numpy as np
        diffed_lines = np.diff(self.annoline_indices)
        maxdiff = max( diffed_lines )
        max_index = diffed_lines.tolist().index(maxdiff)
        start_index, end_index = self.annoline_indices[max_index], self.annoline_indices[max_index+1]
        #Get the text that is between the indices but not the indexed lines
        main_lines = self.doclines[start_index + 1: end_index]
        self.maintext = ' '.join(main_lines)

    def bag_of_words_creation(self):
        '''
        pulls individual words
        '''
        ##Important
        from nltk.corpus import stopwords
        import re
        #Kill any punctuation, find anything that is not a letter and get rid of it
        letters_only = re.sub("[^a-zA-Z]", " ", self.maintext)
        lower_case = letters_only.lower()
        #Split the lower_case article into individual words
        full_wordset = lower_case.split(' ')
        #Remove the stopwords
        self.words = [w for w in full_wordset if w not in stopwords.words("english") and w not in ['', ' ']]

    def get_date(self):
        '''
        gets the date for the article
        '''
        months = {'January':1,'February':2,'March':3,'April':4,'May':5,'June':6,'July':7,'August':8,'September':9,'October':10,'November':11,'December':12}
        import datetime
        story = self.doctext
        story = story.replace('\n',' ')
        story = story.lower()
        story = story.replace(',',' ')
        words = story.split()
        index = find_month(words)
        while not (isInteger(words[index+1]) and isInteger(words[index+2])):
            if index == -1:
                return None
            inter = words[index]+words[index+1]
            story = story[story.find(inter)+len(inter):len(story)]
            words = story.split()
            index = find_month(words)
        month = months[words[index].capitalize()]
        day = int(words[index+1])
        year = int(words[index+2])
        date = datetime.date(year, month, day)
        return date

def find_month(words):
#this is AJ's helper function with the below get_date function
    months = ['january','february','march','april','may','june','july','august','september','october','november','december']
    i = 0
    for word in words:
        if word in months:
            return i
        i+=1
    return -1

def isInteger(num):
    try:
        int(num)
        return True
    except ValueError:
        return False
