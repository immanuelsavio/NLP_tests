from nltk.tokenize import word_tokenize, WordPunctTokenizer, sent_tokenize
from nltk.stem.porter import PorterStemmer
from nltk.stem.lancaster import LancasterStemmer
from nltk.stem.snowball import SnowballStemmer

input_word = ['reading', 'Accomplishment', 'Jumping']
y = "My name is immanuelsavio"
x = word_tokenize(y)
print(x)