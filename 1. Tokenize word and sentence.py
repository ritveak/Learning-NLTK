
# BASICALLY Tokenizing is splitting the whole string.
# sent_tokenize, tokenizes the whole string into sentences.
# word_tokenize, tokenizes the whole string into words.
# run the code to understand it!!


from nltk.tokenize import sent_tokenize,word_tokenize 

example_text = "Hello, Mr. X, How are you doing? This is Mr. Ritveak, I hope everything is fine. Don't fall asleep every time! Bye for now."

for i in sent_tokenize(example_text):
    print(i)

for i in word_tokenize(example_text):
    print(i)
