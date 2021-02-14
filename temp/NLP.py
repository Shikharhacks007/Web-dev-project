from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer
from spacy import displacy
from nltk.stem import WordNetLemmatizer
import spacy
from spacy import displacy
from nltk.corpus import stopwords
import re

'''
text= "Is there a swimming pool here?"


sentence = sent_tokenize(text)

stop_words = set(stopwords.words("english"))
filt_text=[]
for i in sentence:
      if i not in stop_words:
            filt_text.append(i)

print(filt_text)
temp=""

for i in filt_text:
      temp += i

print (temp)
temp = word_tokenize(temp)

print(temp)
ps = PorterStemmer()
for w in temp:
      print(ps.stem(w),end=" ")

lemmatizer = WordNetLemmatizer()
for word in temp:
      print(lemmatizer.lemmatize(word), end =" ")


nlp = spacy.load("en_core_web_sm")
doc = nlp(temp)
displacy.serve(doc, style='dep')
'''


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


def display(doc):
    # display on the web
    spacy.displacy.serve(doc, style='dep')
    displacy.render(doc, style='dep')

# load english language model

nlp = spacy.load('en_core_web_sm') #disable=['ner','textcat'])

text = '''IS the plagiarism policy serious'''

sentence = stop_words((clean(text)))
print(sentence)
doc = nlp(sentence)
insight =[]
for token in doc:
    print(token.text,'->',token.pos_)
    if token.pos_=="NOUN":
        insight.append(token)
    elif token.pos_ =="ADJ":
        insight.append(token)

print(insight)
display(doc)


