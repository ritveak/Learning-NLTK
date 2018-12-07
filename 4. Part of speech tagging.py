import nltk
from nltk.corpus import state_union
#state_union holds the addresses of presidents
from nltk.tokenize import PunktSentenceTokenizer
#this is another type of tokenizer(google for more info)
'''
we can use the below two lines to use a corpora like the one
about George Bush in 2005 and 2006.

uncomment these two lines and comment the two lines below it, to get the feel of
working with corpora.
'''

# sample= state_union.raw("2005-GWBush.txt")
# test= state_union.raw("2006-GWBush.txt")

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
# we will get a list of all words and their corresponding parts of speech. 
'''
POS tag list:

    CC coordinating conjunction
    CD cardinal digit
    DT determiner
    EX existential there (like: "there is" ... think of it like "there exists")
    FW foreign word
    IN preposition/subordinating conjunction
    JJ adjective 'big'
    JJR adjective, comparative 'bigger'
    JJS adjective, superlative 'biggest'
    LS list marker 1)
    MD modal could, will
    NN noun, singular 'desk'
    NNS noun plural 'desks'
    NNP proper noun, singular 'Harrison'
    NNPS proper noun, plural 'Americans'
    PDT predeterminer 'all the kids'
    POS possessive ending parent's
    PRP personal pronoun I, he, she
    PRP$ possessive pronoun my, his, hers
    RB adverb very, silently,
    RBR adverb, comparative better
    RBS adverb, superlative best
    RP particle give up
    TO to go 'to' the store.
    UH interjection errrrrrrrm
    VB verb, base form take
    VBD verb, past tense took
    VBG verb, gerund/present participle taking
    VBN verb, past participle taken
    VBP verb, sing. present, non-3d take
    VBZ verb, 3rd person sing. present takes
    WDT wh-determiner which
    WP wh-pronoun who, what
    WP$ possessive wh-pronoun whose
    WRB wh-abverb where, when

'''
