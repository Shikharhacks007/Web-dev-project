import json
import string
import warnings
import random
import nltk
import requests
warnings.filterwarnings("ignore")
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
f = open('content.txt','r',errors = 'ignore', encoding = 'utf-8')
paragraph = f.read()
nltk.download('punkt')   
sent_tokens = nltk.sent_tokenize(paragraph)
word_tokens = nltk.word_tokenize(paragraph)

greetings = ['Hey', 'Hello', 'Hi', 'It"s great to see you', 'Nice to see you', 'Good to see you']
bye = ['Bye', 'Bye-Bye', 'Goodbye', 'Have a good day','Stop']
thank_you = ['Thanks', 'Thank you', 'Thanks a bunch', 'Thanks a lot.', 'Thank you very much', 'Thanks so much', 'Thank you so much']
thank_response = ['You\'re welcome.' , 'No problem.', 'No worries.', ' My pleasure.' , 'It was the least I could do.', 'Glad to help.']

def bot_initialize(user_msg):
    if(user_msg in greetings):
          return random.choice(greetings)
    elif(user_msg in thank_you):
          return random.choice(thank_response)



def response(user_response):
    robo_response = ''
    sent_tokens.append(user_response)   
    TfidfVec = TfidfVectorizer(tokenizer = Normalize, stop_words='english') 
    tfidf = TfidfVec.fit_transform(sent_tokens)
    vals = cosine_similarity(tfidf[-1], tfidf)
    flat = vals.flatten()  
    flat.sort()
    req_tfidf = flat[-2] 
    if(req_tfidf == 0):    
        robo_response = robo_response + "I am sorry! I don't understand you. Please rephrase your query."
        return robo_response
    
    else:
        robo_response = robo_response + sent_tokens[idx]   
        return robo_response
