import spacy
import lftk.lftk as lftk

nlp = spacy.load("en_core_web_sm")

doc = nlp("I love research but Korean in Seoul in America.")

LFTK = lftk.Extractor(docs = doc)

searched_features_A = lftk.search_features(return_format = "list_key")

extracted_features = LFTK.extract(features = searched_features_A)
print(len(extracted_features.keys()))

print(extracted_features)