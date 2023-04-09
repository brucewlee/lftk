import spacy
import lftk.lftk as lftk
import time
nlp = spacy.load("en_core_web_sm")

searched_features = lftk.search_features(domain="lexico-semantics", language="general", family= "lexicalvariation", return_format="pandas")
print(searched_features)
doc = nlp("I think effects computers have on people are great learning skills/affects because they give us time to chat with friends/new people, helps us learn about the globe(astronomy) and keeps us out of troble!")
LFTK = lftk.Extractor(docs = doc)

searched_features = lftk.search_features(family = "partofspeech", return_format = "list_key")
extracted_features = LFTK.extract(features = searched_features)
print(extracted_features)