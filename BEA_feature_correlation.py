import spacy
import lftk.lftk as lftk
import pandas as pd
from tqdm import tqdm

nlp = spacy.load("en_core_web_sm")

def evaluate_with_readability(searched_features: list):
    # list to populate
    target_and_features = []

    # read data
    df = pd.read_csv('data_task/CLEAR.csv')
    print(df.head())

    # change pandas df to list of dictionaries
    data_list_dict = df.to_dict("records")
    i = 0
    # iterate
    for item in tqdm(data_list_dict):
        text = item['Excerpt']
        readability = item['CAREC_M']

        # load into spaCy
        doc = nlp(text)
        
        # start LFTK
        LFTK = lftk.Extractor(docs = doc)
        LFTK.customize(stop_words=True, punctuations=True, round_decimal=3)
        
        # extract
        extracted_features = LFTK.extract(features = searched_features)
        extracted_features['readability'] = readability

        # populate list
        target_and_features.append(extracted_features)

    # convert back to df
    df_with_features = pd.DataFrame(target_and_features)

    correlation = df_with_features.corr(method='pearson')
    correlation_readability = correlation.readability.sort_values(ascending=False)
    correlation_readability.to_csv("correlation_readability.csv")


def evaluate_with_essay_scoring(searched_features: list):
    # list to populate
    target_and_features = []

    # read data
    df = pd.read_csv('data_task/asap.csv')
    print(df.head())

    # change pandas df to list of dictionaries
    data_list_dict = df.to_dict("records")
    i = 0
    # iterate
    for item in tqdm(data_list_dict):
        text = item['essay']
        essay_score = item['domain1_score']

        # load into spaCy
        doc = nlp(text)
        
        # start LFTK
        LFTK = lftk.Extractor(docs = doc)
        LFTK.customize(stop_words=True, punctuations=True, round_decimal=3)
        
        # extract
        extracted_features = LFTK.extract(features = searched_features)
        extracted_features['essay_score'] = essay_score

        # populate list
        target_and_features.append(extracted_features)

    # convert back to df
    df_with_features = pd.DataFrame(target_and_features)

    correlation = df_with_features.corr(method='pearson')
    correlation_essay_score = correlation.essay_score.sort_values(ascending=False)
    correlation_essay_score.to_csv("correlation_essay_score.csv")


def evaluate_with_fake_news(searched_features: list):
    # list to populate
    target_and_features = []

    # read data
    df = pd.read_csv('data_task/liar.csv')
    print(df.head())

    # modify
    labels = {"FALSE": 0, "barely-true": 1, "half-true": 2, "mostly-true": 3, "TRUE": 4}
    df.replace({"label": labels}, inplace=True)

    # change pandas df to list of dictionaries
    data_list_dict = df.to_dict("records")
    i = 0
    # iterate
    for item in tqdm(data_list_dict):
        if item['label'] != 'pants-fire':
            text = item['statement']
            true_score = item['label']

            # load into spaCy
            doc = nlp(text)
            
            # start LFTK
            LFTK = lftk.Extractor(docs = doc)
            LFTK.customize(stop_words=True, punctuations=True, round_decimal=3)
            
            # extract
            extracted_features = LFTK.extract(features = searched_features)
            extracted_features['true_score'] = true_score

            # populate list
            target_and_features.append(extracted_features)

    # convert back to df
    df_with_features = pd.DataFrame(target_and_features)
    
    correlation = df_with_features.corr(method='pearson')
    correlation_true_score = correlation.true_score.sort_values(ascending=False)
    correlation_true_score.to_csv("correlation_true_score.csv")


def evaluate_with_hate_speech(searched_features: list):
    # list to populate
    target_and_features = []

    # read data
    df = pd.read_csv('data_task/hateval2019.csv')
    print(df.head())

    # change pandas df to list of dictionaries
    data_list_dict = df.to_dict("records")
    i = 0
    # iterate
    for item in tqdm(data_list_dict):
        text = item['text']
        hate_speech = item['HS']

        # load into spaCy
        doc = nlp(text)
        
        # start LFTK
        LFTK = lftk.Extractor(docs = doc)
        LFTK.customize(stop_words=True, punctuations=True, round_decimal=3)
        
        # extract
        extracted_features = LFTK.extract(features = searched_features)
        extracted_features['hate_speech'] = hate_speech

        # populate list
        target_and_features.append(extracted_features)

    # convert back to df
    df_with_features = pd.DataFrame(target_and_features)

    correlation = df_with_features.corr(method='pearson')
    correlation_hate_speech = correlation.hate_speech.sort_values(ascending=False)
    correlation_hate_speech.to_csv("correlation_hate_speech.csv")


if __name__ == "__main__":
    # Retreive all available features
    searched_features = lftk.search_features(return_format = "list_key")
    print(f"{len(searched_features)} loaded")

    # Evaluate
    evaluate_with_hate_speech(searched_features)
    evaluate_with_fake_news(searched_features)
    evaluate_with_essay_scoring(searched_features)
    evaluate_with_readability(searched_features)