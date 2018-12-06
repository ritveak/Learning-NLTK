# By stemming, we take the stem of each word.(not the root)
# By stem we mean, the pure word without suffix and prefix  

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
