from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer
from spacy import displacy
import searchmodule
from nltk.stem import WordNetLemmatizer
import spacy
from spacy import displacy
from nltk.corpus import stopwords
import re

def clean(text):
    # removing paragraph numbers
    text = re.sub('[0-9]+.\t', '', str(text))

    # removing new line characters
    text = re.sub('\n ', '', str(text))
    text = re.sub('\n', ' ', str(text))

    # removing apostrophes
    text = re.sub("'s", '', str(text))

    # removing hyphens
    text = re.sub("-", '', str(text))
    text = re.sub("— ", '', str(text))

    # removing quotation marks
    text = re.sub('\"', '', str(text))

    # removing the comma
    text = re.sub(',','',str(text))

    # removing salutations
    text = re.sub("Mr\.", 'Mr', str(text))
    text = re.sub("Mrs\.", 'Mrs', str(text))

    # removing any reference to outside text
    text = re.sub("[\(\[].*?[\)\]]", "", str(text))

    return text


# split sentences
def sentences(text):
    # split sentences and questions
    text = re.split('[!.?]', text)
    clean_sent = []
    for sent in text:
        clean_sent.append(sent)
    return clean_sent


def stop_words(text):
    # def remove_stop_words(text):
    stop_words = set(stopwords.words("English"))
    filter_sentence = [i for i in text.split() if not i in stop_words]
    print(filter_sentence)
    return stemmer(filter_sentence)


def stemmer(filter_sentence):
    sentence = ""
    ps = PorterStemmer()
    for i in filter_sentence:
        sentence += str(ps.stem(i)) + " "
    sentence.strip()
    return sentence


# load english language model
def execute(text):
    nlp = spacy.load('en_core_web_sm') #disable=['ner','textcat'])

    #text = '''is there gaming centre?'''

    sentence = stop_words((clean(text)))
    print(sentence)
    doc = nlp(sentence)  
        
    insight =[]
    for token in doc:
        print(token.text,'->',token.pos_)
        if token.pos_=="NOUN":
            insight.append(token.text)
        elif token.pos_ =="ADJ":
            insight.append(token.text)
            
    if(len(insight)==0):
        return None
    print(insight)
    # search module
    print(type(insight[0]))
    index = searchmodule.searching(insight)
    if(index!= None):
        print(index)
        y = str(index)
        x = "data"+ y +".txt"
        f = open(x, "r")
        line = f.read()
        print(line)
        f.close()
    elif(index == 8):
        line = "No issues!"
    else:
        line = "Sorry, I didn't understand. Rephrase and ask again"

    return line


