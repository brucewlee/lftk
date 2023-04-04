import spacy
import lftk.lftk as lftk
import time
searched_features = lftk.search_features(domain = "surface", family = "avgwordsent")
print(searched_features)
print(len(searched_features))