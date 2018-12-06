# In computing, stop words are words which are filtered out before or after processing of natural language data (text).
# Though "stop words" usually refers to the most common words in a language, there is no single universal list of stop words used by all natural language processing tools, and indeed not all tools even use such a list.
# Some tools specifically avoid removing these stop words to support phrase search. 


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



