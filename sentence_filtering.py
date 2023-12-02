from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk import ngrams, pos_tag
import re


text = "Can you tell me a joke?"

stop_words = set(stopwords.words('english')) 


def tokenize(s:str)->list[str]:
    return word_tokenize(s, language="english")


print(tokenize(text))
word_tokens = word_tokenize(text) 
  
filtered_sentence = [w for w in word_tokens if w not in stop_words] 
  
filtered_sentence = [] 
  
for w in word_tokens: 
    if w not in stop_words: 
        filtered_sentence.append(w) 
  

print(filtered_sentence) 


nltk_tokens = word_tokenize(text) 
print(list(ngrams(filtered_sentence,3)))

print(pos_tag(filtered_sentence))




def cambiar(texto):
    patron=["o", "as", "a", "amos", "áis", "an"]
    for x in patron:
        nueva = re.sub(rf"{x}\b","ar", texto)
        texto = nueva
    return nueva
