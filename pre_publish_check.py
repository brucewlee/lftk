import lftk
import spacy

nlp = spacy.load("en_core_web_sm")
doc = nlp("I love research but my professor is strange.")

searched_features = lftk.search_features(domain = "surface", family = "avgwordsent", return_format = "list_key")
print(searched_features)

LFTK = lftk.Extractor(docs = doc)
LFTK.customize(stop_words=True, punctuations=False, round_decimal=3)
extracted_features = LFTK.extract(features = searched_features)
print(extracted_features)

searched_features = lftk.search_features(family = "wordsent", language = "general", return_format = "list_key")
print(searched_features)

extracted_features = LFTK.extract(features = searched_features)
print(extracted_features)