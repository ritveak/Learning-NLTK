from nltk.tokenize import sent_tokenize,word_tokenize

example_text = "Hello, Mr. Ritveak, How are you doing? I hope everything is fine. Don't fall asleep every time! Bye for now."
for i in sent_tokenize(example_text):
    print(i)

for i in word_tokenize(example_text):
    print(i)
