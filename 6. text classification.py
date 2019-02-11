#!/usr/bin/env python
# coding: utf-8

# In[1]:


#term frequency(tf) and inverse document freq(idf) used for vectorisation
 


# In[1]:


def gf(w):
    return {'last_letter':w[-1]}


# In[6]:


gf("rytsy")


# In[8]:


from nltk.corpus import names


# In[11]:


labelname = ([(name,'male') for name in names.words('male.txt')]+[(name,'female') for name in names.words('female.txt')])


# In[12]:


labelname


# In[14]:


import random


# In[19]:


random.shuffle(labelname)


# In[20]:


labelname


# In[21]:


featuresets = [(gf(n),gender) for(n,gender)in labelname]


# In[22]:


featuresets


# In[23]:


l2 = ([(name[-1],'male') for name in names.words('male.txt')]+[(name[-1],'female') for name in names.words('female.txt')])


# In[24]:


l2


# In[41]:


train, test = featuresets[500:],featuresets[:500]


# In[27]:


import nltk
classifier = nltk.NaiveBayesClassifier.train(train)


# In[28]:


classifier.classify(gf('david'))


# In[42]:


print(nltk.classify.accuracy(classifier,test))







