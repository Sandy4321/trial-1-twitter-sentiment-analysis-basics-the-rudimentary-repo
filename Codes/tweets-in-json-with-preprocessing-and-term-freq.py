import json
from twitter_app_login import *
from nltk.tokenize import word_tokenize
from collections import Counter
import re
import operator
from nltk.corpus import stopwords
import string

punctuation = list(string.punctuation)
stop = stopwords.words('english') + punctuation + ['rt', 'via','\\',',',"'",'xe0','xa4','xbe']

emoticons_str = r"""
    (?:
        [:=;] # Eyes
        [oO\-]? # Nose (optional)
        [D\)\]\(\]/\\OpP] # Mouth
    )"""
 
regex_str = [
    emoticons_str,
    r'<[^>]+>', # HTML tags
    r'(?:@[\w_]+)', # @-mentions
    r"(?:\#+[\w_]+[\w\'_\-]*[\w_]+)", # hash-tags
    r'http[s]?://(?:[a-z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-f][0-9a-f]))+', # URLs
 
   # r'(?:(?:\d+,?)+(?:\.?\d+)?)', # numbers
    r"(?:[a-z][a-z'\-_]+[a-z])", # words with - and '
  #  r'(?:[\w_]+)', # other words
  #  r'(?:\S)' # anything else
]
    
tokens_re = re.compile(r'('+'|'.join(regex_str)+')', re.VERBOSE | re.IGNORECASE)
emoticon_re = re.compile(r'^'+emoticons_str+'$', re.VERBOSE | re.IGNORECASE)
 
def tokenize(s):
    return tokens_re.findall(str(s))
 
def preprocess(s, lowercase=False):
    tokens = tokenize(s)
    if lowercase:
        tokens = [token if emoticon_re.search(token) else token.lower() for token in tokens]
    return tokens


with open("tweets.json") as f:    
    count_all = Counter()
    all_data = f.readlines()

    # Create a list with all the terms
    terms_all = [term for term in preprocess(all_data)]
    # Update the counter
    count_all.update(terms_all)

    # Removing stopwords
    punctuation = list(string.punctuation)
    terms_stop = [term for term in preprocess(all_data) if term not in stop]

    # Count terms only once, equivalent to Document Frequency
    terms_single = set(terms_all)

    # Count hashtags only
    terms_hash = [term for term in preprocess(all_data) 
                  if term.startswith('#')]

    # Count terms only (no hashtags, no mentions)
    terms_only = [term for term in preprocess(all_data) 
                  if term not in stop and
                  not term.startswith(('#', '@'))] 
                  # mind the ((double brackets))
                  # startswith() takes a tuple (not a list) if 
                  # we pass a list of inputs


    from nltk import bigrams 
    #
    terms_bigram = bigrams(terms_all)

#    print "after removing the stop words : ", terms_stop
    #print terms_single
 #   print terms_hash
    #print terms_only
    print terms_bigram
