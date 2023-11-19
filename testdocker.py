# %%
import bs4  # Scraping HTML
import requests  # Making Requests to a websites

import spacy
import pytextrank

import pandas as pd # Data Wrangling
import numpy as np # Math
# import nltk
# from nltk.corpus import stopwords
from sklearn.feature_extraction.text import CountVectorizer

import re # Regex

# %%
# Make a Request to a healthcare and pharmaceuticals subsite of Reuters
request = requests.get("https://www.reuters.com/business/healthcare-pharmaceuticals/")

# %%
# Parse Healthcare Subsite of Reuters
soup = bs4.BeautifulSoup(request.text, 'html.parser')

# %%
# Find all html parts containing links
anchor = soup.find_all("a")

# %%
# Print all extracted Links found on website
for attr in anchor:
    print(attr["href"])

# %%
# Get only links to articles about novo nordisk company
novo_news = [attr["href"] for attr in anchor if "novo" in attr["href"] or "ozempic" in attr["href"] or "wegovy" in attr["href"]]

# %%
novo_news

# %%
all_article_paragraphs = []

for article in novo_news:
    # Make a Request Append Https Reuters string for proper url format.
    request1 = requests.get("https://www.reuters.com" if "https" not in article else "" + article)
    
    # Parse HTML
    soup_subsite = bs4.BeautifulSoup(request1.text, "html.parser")
    
    # Seek All Paragraphs
    paragraphs = soup_subsite.find_all("p")
    
    # Delete html stuff
    # extracted_text = [re.sub("<[^>]+>", "", str(paragraph)) for paragraph in paragraphs]
    extracted_text = [paragraph.text for paragraph in paragraphs]
    

    # Append to a list of all articles
    all_article_paragraphs.append(extracted_text)

# %% [markdown]
# Article Requires Further Cleaning - Images, Legal Notices and other should be removed.

# # %%
# def article_tokenization(article):
#     article = " ".join(article)
#     sentences = nltk.sent_tokenize(article)
#     tokenized = [nltk.word_tokenize(sentence) for sentence in sentences]
#     return tokenized    

# # %%
# def process_words(tokenized_article, stemmer):
#     words_to_remove = set(stopwords.words("english"))
#     return [[stemmer.stem(word) for word in sentence if word not in words_to_remove] for sentence in tokenized_article]

# # %%
# tokenized_articles = [article_tokenization(article) for article in all_article_paragraphs]

# # %%
# ps = nltk.PorterStemmer()

# # %%
# tokenized_articles = [process_words(article, ps) for article in tokenized_articles]

# # %%
# tokenized_articles

# # %%
# bow = CountVectorizer()

# # %%
# bow.fit([" ".join(sentence) for sentence in tokenized_articles[0]])

# # %%
# bow.transform([" ".join(sentence) for sentence in tokenized_articles[0]]).toarray()

# %%

# example text
text = " ".join([paragraph for paragraph in all_article_paragraphs[3] if "reuters" not in paragraph.lower()])
# load a spaCy model, depending on language, scale, etc.
nlp = spacy.load("en_core_web_sm")

# add PyTextRank to the spaCy pipeline
nlp.add_pipe("textrank")
doc = nlp(text)

# %%
len(text)

# %%
len(doc)

# %%
print(*[paragraph for paragraph in doc.text.split(".") if len(paragraph) > 2], sep="\n")

# %%
[(phrase.text, phrase.rank) for phrase in doc._.phrases]

# %%
sent_bounds = [ [s.start, s.end, set([])] for s in doc.sents ]
sent_bounds

# %%
from icecream import ic

# %%
limit_phrases = 4

phrase_id = 0
unit_vector = []

for p in doc._.phrases:
    ic(phrase_id, p.text, p.rank)

    unit_vector.append(p.rank)

    for chunk in p.chunks:
        ic(chunk.start, chunk.end)

        for sent_start, sent_end, sent_vector in sent_bounds:
            if chunk.start >= sent_start and chunk.end <= sent_end:
                ic(sent_start, chunk.start, chunk.end, sent_end)
                sent_vector.add(phrase_id)
                break

    phrase_id += 1

    if phrase_id == limit_phrases:
        break

# %%
for sent in doc.sents:
    ic(sent)

# %%
sum_ranks = sum(unit_vector)

unit_vector = [ rank/sum_ranks for rank in unit_vector ]
unit_vector

# %%
from math import sqrt

sent_rank = {}
sent_id = 0

for sent_start, sent_end, sent_vector in sent_bounds:
    ic(sent_vector)
    sum_sq = 0.0
    ic
    for phrase_id in range(len(unit_vector)):
        ic(phrase_id, unit_vector[phrase_id])

        if phrase_id not in sent_vector:
            sum_sq += unit_vector[phrase_id]**2.0

    sent_rank[sent_id] = sqrt(sum_sq)
    sent_id += 1

# %%
from operator import itemgetter

sorted(sent_rank.items(), key=itemgetter(1)) 

# %%
limit_sentences = 5

sent_text = {}
sent_id = 0

for sent in doc.sents:
    sent_text[sent_id] = sent.text
    sent_id += 1

num_sent = 0

for sent_id, rank in sorted(sent_rank.items(), key=itemgetter(1)):
    ic(sent_id, sent_text[sent_id])
    num_sent += 1

    if num_sent == limit_sentences:
        break


