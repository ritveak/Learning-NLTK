#!/usr/bin/env python
# coding: utf-8

# In[2]:


from nltk.tokenize import sent_tokenize,word_tokenize 


# In[3]:


m = "Hi this is Ritveak. How are U? i AM JUST FINE."
print(sent_tokenize(m))


# In[5]:


from nltk.corpus import brown
brown.categories()


# In[11]:


brown.words(categories = 'adventure')


# In[6]:


brown.words(categories = 'adventure')[:20]


# In[15]:


from nltk.corpus import inaugural
inaugural.fileids()
inaugural.words(fileids='2009-Obama.txt')


# In[1]:


from nltk.corpus import wordnet 
  
# Then, we're going to use the term "program" to find synsets like so: 
syns = wordnet.synsets("room") 
  
# An example of a synset: 
print(syns[0].name()) 
  
# Just the word: 
print(syns[0].lemmas()[0].name()) 
  
# Definition of that first synset: 
print(syns[0].definition()) 
  
# Examples of the word in use in sentences: 
print(syns[0].examples()) 


# In[4]:


wordnet.synset("room.n.01").lemma_names()


# In[5]:


wordnet.synsets("mobile")


# In[9]:


wordnet.synset('mobile.s.01').lemma_names()


# In[10]:


from nltk.tokenize import TweetTokenizer


# In[13]:


text = "Hi, I am finally happy to get placed!!! #placed #blessed"
tokens = TweetTokenizer().tokenize(text)


# In[14]:


tokens


# In[16]:


import nltk
e = nltk.corpus.cmudict.entries()


# In[18]:


e[1000:1025]


# In[19]:


from nltk.tokenize import sent_tokenize,word_tokenize 

example_text = '''Hello, Mr. X, How are you doing? 
This is Mr. Ritveak, I hope everything is fine.
Don't fall asleep every time! Bye for now.'''

for i in sent_tokenize(example_text):
    print(i)

for i in word_tokenize(example_text):
    print(i)


# In[20]:


from nltk.corpus import stopwords

# Corpus is basically a fie that stores a lot of text.
# We are intrested in Stop words as of now, thats why we will only import that.

from nltk.tokenize import word_tokenize

eg = "Hi there Mr. X, we are here to show a stop word example."
stop_words = set(stopwords.words("english"))

#print(stop_words)
# uncomment the above line to see the stop words stored in nltk corpus.

words = word_tokenize(eg)
filtered_sentence = []

for w in words:
    if w not in stop_words:
        filtered_sentence.append(w)


#filtered_sentence = [w for w in words if not w in stop_words]

# above is a one line code for the 3 line code used above it, feel free to un commen it and
# play with it!!!

print(filtered_sentence)


# In[1]:


from nltk.stem import PorterStemmer
from nltk.tokenize import word_tokenize

ps = PorterStemmer()
eg = ["run", "running","runner"]
for w in eg:
    print(ps.stem(w))

new_eg = "It is very important to run, coz running can make you a runner"

#now taking a sentence, tokenizing the words and then finding out the stem words.
words = word_tokenize(new_eg)

for w in words:
    print(ps.stem(w))


# In[2]:


#pos tagging
import nltk
from nltk.corpus import state_union
from nltk.tokenize import PunktSentenceTokenizer

sample = "Hey! This is Ritveak, Trying to code and learn NLP."
test = "My name is Ritveak, I am a Btech student. I want to learn NLP. And that is the reason why I am coding."
custom_tokenizer = PunktSentenceTokenizer(sample)

tokenized = custom_tokenizer.tokenize(test)

def process():
    try:
        for i in tokenized:
            words = nltk.word_tokenize(i)
            tagged= nltk.pos_tag(words)
            print (tagged)


        
    except Exception as e:
        print (str(e))

process()


# In[ ]:




