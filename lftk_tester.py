import pprint 

import spacy
import pandas as pd
from tqdm import tqdm

from lftk import lftk

paths = {
    'BeerQA': 'GPT3QA/predictions/BeerQA_test_GPT_preds.json',
    'CSQA2': 'GPT3QA/predictions/CSQA2_test_GPT_preds.json',
    'HotpotQA': 'GPT3QA/predictions/HotpotQA_test_GPT_preds.json',
    'NQ': 'GPT3QA/predictions/NQ_test_GPT_preds.json',
    'QANTA': 'GPT3QA/predictions/QANTA_test_GPT_preds.json',
    'StrategyQA': 'GPT3QA/predictions/StrategyQA_test_GPT_preds.json',
    'TimeQA': 'GPT3QA/predictions/TimeQA_test_GPT_preds.json',
    'TriviaQA': 'GPT3QA/predictions/TriviaQA_test_GPT_preds.json'
}

nlp = spacy.load("en_core_web_sm")

def analyze_dataset(path: str, name: str):
    DATA = pd.read_json(path, orient='records')
    DATA_dict = DATA.to_dict('records')

    correctness = []

    for row in tqdm(DATA_dict):
        LFTK = lftk.Start(docs = nlp(row['question']))
        LFTK.customize(stop_words=False, punctuations=False, round_decimal=3)
        extracted = LFTK.extract(features = ['t_word', 't_sent', 't_char', 'a_word_ps', 'a_char_ps', 'a_char_pw', 't_kup', 't_bry', 'a_kup_ps', 'a_bry_ps', 'a_kup_pw', 'a_bry_pw', 't_subtlex_us_zipf', 'a_subtlex_us_zipf_pw', 'a_subtlex_us_zipf_ps', 't_named_entity', 'a_named_entity_pw', 'a_named_entity_ps', 'simp_ttr', 'root_ttr', 'corr_ttr', 'bilog_ttr', 'uber_ttr', 'simp_ttr_no_lem', 'root_ttr_no_lem', 'corr_ttr_no_lem', 'bilog_ttr_no_lem', 'uber_ttr_no_lem'])
        row.update(extracted)

        print(row)

    DATA = pd.DataFrame(DATA_dict)
    DATA.to_csv(f'{name}_lftk.csv')

"""for key, value in paths.items():
    analyze_dataset(value, key)"""


doc = nlp("I love research but my professor is strange.")
LFTK_Extractor = lftk.Extractor(docs = doc)
LFTK_Extractor.customize(stop_words=False, punctuations=False, round_decimal=3)
extracted_features = LFTK_Extractor.extract(features = ["a_word_ps", "a_kup_pw", "n_noun"])
print(extracted_features)
pp = pprint.PrettyPrinter(indent=4)
pp.pprint(extracted_features)