#!/usr/bin/env python
# coding: utf-8

# In[2]:


import nltk


# In[3]:


from nltk.stem import PorterStemmer
st = PorterStemmer()
st.stem("exaggerated")


# In[6]:


st.stem("printer")


# In[6]:


st.stem("planted")


# In[7]:


st.stem("elaborate")


# In[8]:


st.stem("doctored")


# In[9]:


st.stem("reenter")


# In[10]:


st.stem("unemployed")


# In[19]:


st.stem("laziness")


# In[7]:


from nltk.stem import LancasterStemmer
stl = LancasterStemmer()
stl.stem("exaggerated")


# In[13]:


stl.stem("printer")


# In[15]:


stl.stem("printer")


# In[16]:


stl.stem("elaborate")


# In[8]:


stl.stem("doctored")


# In[18]:


stl.stem("unemployed")


# In[20]:


stl.stem("laziness")


# In[9]:


from nltk.stem import SnowballStemmer
SnowballStemmer.languages
sts = SnowballStemmer("english")
sts.stem("exaggerated")


# In[23]:


sts.stem("printer")


# In[10]:


sts.stem("planted")


# In[25]:


sts.stem("elaborate")


# In[26]:


sts.stem("doctored")


# In[27]:


sts.stem("unemployed")


# In[28]:


sts.stem("laziness")


# In[ ]:




