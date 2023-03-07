# -*- coding: UTF-8 -*-
"""
Software: LFTK - Linguistic Features Toolkit
Script: extractor.py
License: CC-BY-SA 4.0
Original Author: Bruce W. Lee (이웅성) @brucewlee
Affiliation 1: LXPER Inc. - Seoul, South Korea
Affiliation 2: University of Pennsylvania - PA, USA
"""
import os
from typing import Union, Dict, List

import spacy
import pandas as pd

from lftk.utils import get_feature_map, get_pandas_row, convert_ndjson_to_pd
from lftk.derivation_collector import DerivationCollector


CURRENT_PATH = os.path.abspath(os.path.dirname(__file__))
FEATURE_MAP_PATH = os.path.join(CURRENT_PATH, 'resources/feature_map.json')
AOA_KUP_PATH = os.path.join(CURRENT_PATH, 'resources/AoA_ratings_kup.csv')
AOA_BRY_PATH = os.path.join(CURRENT_PATH, 'resources/AoA_ratings_bry.csv')
SUBTLEX_US_PATH = os.path.join(CURRENT_PATH, 'resources/subtlex_us.csv')


class Extractor:
    """
    Starter class for users
    input :
    - self
    - docs: single or multiple spacy doc object
    saves :
    - self.doc: spacy doc object
    - self.feature_map: dictionary of dictionary that contains "key" as the parent key and the others ("name", "type") as children keys
    """
    def __init__(
        self, 
        docs: Union[spacy.tokens.doc.Doc, List[spacy.tokens.doc.Doc]]
        ) -> None:
        # Type adjustment
        if type(docs) is not list: docs = [docs]
        self.docs = docs
        self.feature_map = get_feature_map(path = FEATURE_MAP_PATH)


    """
    Save options
    input :
    - self
    - options
    saves :
    - self.options
    """
    def customize(
        self,
        stop_words: bool = True,
        punctuations: bool = True,
        round_decimal: int = 3,
        ) -> None:
        self.options = {
            'stop_words': stop_words,
            'punctuations': punctuations,
            'round_decimal': 3
        }


    """
    Calculate linguistic feature(s) from all given spaCy docs
    input :
    - self
    - features: features to be extracted
    returns :
    - result: extracted linguistic feature(s)
    """
    def extract(
        self, 
        features: Union[str, list] = "*"
        ) -> Union[
            Dict[str, Union[float,int]], 
            List[Dict[str, Union[float,int]]]
            ]:
        # Type adjustment
        if type(features) is not list: features = [features]
        # Iterate user input
        all_results = []
        for doc in self.docs:
            extractor = SingleExtractor(doc, self.feature_map, self.options)
            result = extractor.run(features)
            all_results.append(result)
        # Type adjustment
        if len(all_results) == 1:
            all_results = all_results[0]
        return all_results


class SingleExtractor:
    """
    Initialize pipeline
    input :
    - self
    - doc: single text inside spacy doc object
    saves :
    - self.doc: spacy doc object
    """
    def __init__(
        self, 
        doc: spacy.tokens.doc.Doc,
        feature_map: Dict[str, Dict[str, str]],
        options: Dict[str, Union[str, bool]]
        ) -> None:
        self.doc = doc
        self.feature_map = feature_map
        self.options = options
        self.paths = {
            'FEATURE_MAP_PATH' : FEATURE_MAP_PATH,
            'AOA_KUP_PATH' : AOA_KUP_PATH,
            'AOA_BRY_PATH' : AOA_BRY_PATH,
            'SUBTLEX_US_PATH' : SUBTLEX_US_PATH,
        }


    """
    Calculate linguistic feature(s) from spaCy doc
    input :
    - self
    - features: features to be extracted
    returns :
    - result: extracted linguistic feature(s)
    """
    def run(
        self, 
        features: list,
        ) -> Dict[str, Union[float,int]]:
        # Iterate through given features
        result = {}
        if features != ["*"]:
            for feature_key in features:
                # Get feature name from feature key
                feature_name = self.feature_map[feature_key]['name']
                # Get feature function from feature name
                feature_fn = getattr(DerivationCollector, feature_name)
                # Run feature function in DerivationCollector object
                result[f'{feature_key}'] = round(feature_fn(self), self.options['round_decimal'])
        else:
            # Extract all features
            for feature_key in self.feature_map:
                # Get feature name from feature key
                feature_name = self.feature_map[feature_key]['name']
                # Get feature function from feature name
                feature_fn = getattr(DerivationCollector, feature_name)
                # Run feature function in DerivationCollector object
                result[f'{feature_key}'] = round(feature_fn(self), self.options['round_decimal'])
        return result

"""
Return available linguistic features
input :
- domain: specify which domain
- family: specify which family
returns :
- result: searched linguistic feature(s)
"""
def search_features(
    domain: str = "*",
    family: str = "*",
    pandas: bool = False
    ) -> Union[List[dict], pd.core.frame.DataFrame]:
    feature_df = convert_ndjson_to_pd(path = FEATURE_MAP_PATH)
    if domain != "*":
        feature_df = get_pandas_row(feature_df, "domain", domain, True)
    if family != "*":
        feature_df = get_pandas_row(feature_df, "family", family, True)
    if pandas == False:
        result = feature_df.to_dict('records')
    else:
        result = feature_df
    return result