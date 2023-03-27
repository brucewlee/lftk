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
    def __init__(
        self, 
        docs: Union[spacy.tokens.doc.Doc, List[spacy.tokens.doc.Doc]]
        ) -> None:
        """
            Starter class for users
            input :
            - self
            - docs: single or multiple spacy doc object
            saves :
            - self.doc: spacy doc object
            - self.feature_map: dictionary of dictionary that contains "key" as the parent key and the others ("name", "type") as children keys
        """
        # Type adjustment
        if type(docs) is not list: docs = [docs]
        self.docs = docs
        self.feature_map = get_feature_map(path = FEATURE_MAP_PATH)
        self.customize()

    def customize(
        self,
        stop_words: bool = True,
        punctuations: bool = True,
        round_decimal: int = 3,
        ) -> None:
        """
            Save options
            input :
            - self
            - stop_words: set to False to remove stop words in all feature calculations
            - punctuations: set to False to remove punctuations in all feature calculations
            - round_decimal: maximum number of returned decimal points
            saves :
            - self.options
        """
        self.options = {
            'stop_words': stop_words,
            'punctuations': punctuations,
            'round_decimal': round_decimal
        }

    def extract(
        self, 
        features: Union[str, list] = "*"
        ) -> Union[
            Dict[str, Union[float,int]], 
            List[Dict[str, Union[float,int]]]
            ]:
        """
            Calculate linguistic feature(s) from all given spaCy docs
            input :
            - self
            - features: features to be extracted
            returns :
            - result: extracted linguistic feature(s)
        """
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
    def __init__(
        self, 
        doc: spacy.tokens.doc.Doc,
        feature_map: Dict[str, Dict[str, str]],
        options: Dict[str, Union[str, bool]]
        ) -> None:
        """
            Initialize pipeline
            input :
            - self
            - doc: single text inside spacy doc object
            saves :
            - self.doc: spacy doc object
        """
        self.doc = doc
        self.feature_map = feature_map
        self.options = options
        self.paths = {
            'FEATURE_MAP_PATH' : FEATURE_MAP_PATH,
            'AOA_KUP_PATH' : AOA_KUP_PATH,
            'AOA_BRY_PATH' : AOA_BRY_PATH,
            'SUBTLEX_US_PATH' : SUBTLEX_US_PATH,
        }

    def run(
        self, 
        features: list,
        ) -> Dict[str, Union[float,int]]:
        """
            Calculate linguistic feature(s) from spaCy doc
            input :
            - self
            - features: features to be extracted
            returns :
            - result: extracted linguistic feature(s)
        """
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

def search_features(
    domain: str = "*",
    family: str = "*",
    language: str ="*",
    return_format: str = "list_dict"
    ) -> Union[List[dict], pd.core.frame.DataFrame]:
    """
        Return available linguistic features that match user-specified attributes
        input :
        - domain: specify which domain
        - family: specify which family 
        - return_format: how to return searched features
        returns :
        - result: searched linguistic feature(s)
    """
    feature_df = convert_ndjson_to_pd(path = FEATURE_MAP_PATH)
    if domain != "*":
        feature_df = get_pandas_row(feature_df, "domain", domain, True)
    if family != "*":
        feature_df = get_pandas_row(feature_df, "family", family, True)
    if language != "*":
        feature_df = get_pandas_row(feature_df, "language", language, True)

    if return_format == "list_dict":
        result = feature_df.to_dict('records')
    elif return_format == "pandas":
        result = feature_df
    elif return_format == "list_key":
        list_dict = feature_df.to_dict('records')
        result = [dict_['key'] for dict_ in list_dict]
    else:
        raise ValueError('return_format must be "list_dict", "pandas", or "list_key"')

    return result