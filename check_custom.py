import spacy
import lftk.lftk as lftk

nlp = spacy.load("en_core_web_sm")
doc1 = nlp("I think effects computers have on people are great!")
doc2 = nlp("I like drinking coffee...")

LFTK = lftk.Extractor(docs = doc1)
extracted_features = LFTK.extract(features = ["a_word_ps", "a_kup_pw", "n_noun"])
print(extracted_features)

LFTK = lftk.Extractor(docs = [doc1, doc2])
extracted_features = LFTK.extract(features = ["a_word_ps", "a_kup_pw", "n_noun"])
print(extracted_features)

import lftk.lftk as lftk

searched_features = lftk.search_features(domain = 'surface', family = "avgwordsent", language="general", return_format = "list_dict")
print(searched_features)
searched_features = lftk.search_features(domain = 'surface', family = "avgwordsent", language="general", return_format = "pandas")
print(searched_features)
searched_features = lftk.search_features(domain = 'surface', family = "avgwordsent", language="general", return_format = "list_key")
print(searched_features)