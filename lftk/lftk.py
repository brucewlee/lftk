# -*- coding: UTF-8 -*-
import os
from typing import Union, Dict, List
import sys

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
    """Main object

    Saves your spaCy doc objects to extract linguistic features from. As you declare this object, pass in spaCy doc(s).
        
    Parameters
    ----------
    docs : Union[spacy.tokens.doc.Doc, List[spacy.tokens.doc.Doc]]
        spaCy doc object or a list of spacy doc objects

    Examples
    ----------
    >>> import spacy
    >>> import lftk
    >>> 
    >>> nlp = spacy.load("en_core_web_sm")
    >>> doc1 = nlp("I think effects computers have on people are great!")
    >>> doc2 = nlp("I like drinking coffee...")
    >>> 
    >>> LFTK = lftk.Extractor(docs = [doc1, doc2])


    """
    def __init__(
        self, 
        docs: Union[spacy.tokens.doc.Doc, List[spacy.tokens.doc.Doc]]
        ) -> None:
        # Type adjustment
        if type(docs) is not list: docs = [docs]
        self.docs = docs
        # dictionary of dictionary that contains "key" as the parent key and the others ("name", "type") as children keys
        self.feature_map = get_feature_map(path = FEATURE_MAP_PATH)
        self.customize()

    def customize(
        self,
        stop_words: bool = True,
        punctuations: bool = True,
        round_decimal: int = 3,
        ) -> None:
        """Global customization
    
        Customizes all LFTK functions to extract features based on these options. This exclude some special functions that are intentionally designed to override global options.
        
        Parameters
        ----------
        stop_words : bool (default = True)
            Selection whether to include stop words for feature extraction
        punctuations : bool (default = True)
            Selection whether to include punctuations for feature extraction
        round_decimal : int (default = 3)
            The max number of decimal digits to return (for extracted feature values)
    
        Examples
        ----------
        >>> import spacy
        >>> import lftk
        >>> 
        >>> nlp = spacy.load("en_core_web_sm")
        >>> doc = nlp("I think effects computers have on people are great!")
        >>> 
        >>> LFTK = lftk.Extractor(docs = doc)
        >>> 
        >>> LFTK.customize(stop_words=True, punctuations=False, round_decimal=3)
        >>> output = LFTK.extract(features = ["a_word_ps", "a_kup_pw", "n_noun"])
        >>> # {'a_word_ps': 9.0, 'a_kup_pw': 5.323, 'n_noun': 3}
        >>> 
        >>> LFTK.customize(stop_words=False, punctuations=False, round_decimal=2)
        >>> output = LFTK.extract(features = ["a_word_ps", "a_kup_pw", "n_noun"])
        >>> # {'a_word_ps': 5.0, 'a_kup_pw': 9.6, 'n_noun': 3}


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
        """Extract function for select features
    
        Extracts feature(s) that are passed in by the user. All spaCy docs that were saved during LFTK Extractor declaration are used. This function extracts all features available in LFTK by default. 
        
        This function only accepts feature key(s) (e.g., "t_word", "a_kup_pw").
        
        Parameters
        ----------
        features : Union[str, list] (default = "*")
            A single feature key or a list of feature keys. Passing "*" extracts all available features.

        Returns
        ----------
        result : Union[Dict[str, Union[float,int]], List[Dict[str, Union[float,int]]]]
            A dictionary or a list of dictionaries, depending on the number of spaCy docs you passed in during the creation of LFTK Extractor object.

        Examples
        ----------
        >>> import spacy
        >>> import lftk
        >>> 
        >>> nlp = spacy.load("en_core_web_sm")
        >>> doc1 = nlp("I think effects computers have on people are great!")
        >>> doc2 = nlp("I like drinking coffee...")
        >>> 
        >>> LFTK = lftk.Extractor(docs = doc1)
        >>> 
        >>> output = LFTK.extract(features = ["a_word_ps", "a_kup_pw", "n_noun"])
        >>> # {'a_word_ps': 10.0, 'a_kup_pw': 4.791, 'n_noun': 3}
        >>> 
        >>> LFTK = lftk.Extractor(docs = [doc1, doc2])
        >>> 
        >>> output = LFTK.extract(features = ["a_word_ps", "a_kup_pw", "n_noun"])
        >>> # [{'a_word_ps': 10.0, 'a_kup_pw': 4.791, 'n_noun': 3}, {'a_word_ps': 5.0, 'a_kup_pw': 2.284, 'n_noun': 2}]
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
    """Search features
    
    Returns available linguistic features that match user-specified attributes. Putting "*" on any attribute is analogous to "any". You can use this function to produce list of feature keys and pass them into LFTK Extractor's extract() function (see above).
    
    Parameters
    ----------
    domain : str (default = "*")
        A single domain name (e.g., "surface", "lexico-semantics")
    family : str (default = "*")
        A single family name (e.g., "worddiff", "avgwordsent")
    language : str (default = "*")
        A single supported language (e.g., "worddiff", "avgwordsent")
    return_format : str (default = "list_dict")
        Select how the searched features should be returned. The available options are "list_dict", "pandas", or "list_key".
    
    Returns
    ----------
    result : Union[List[dict], pd.core.frame.DataFrame]
        Available features searched with user-given conditions

    Examples
    ----------
    >>> import lftk
    >>> 
    >>> output = lftk.search_features(domain = 'surface', family = "avgwordsent", language="general", return_format = "list_dict")
    >>> # [{'key': 'a_word_ps', 'name': 'average_number_of_words_per_sentence', 'formulation': 'derivation', 'domain': 'surface', 'family': 'avgwordsent', 'language': 'general'}, {'key': 'a_char_ps', 'name': 'average_number_of_characters_per_sentence', 'formulation': 'derivation', 'domain': 'surface', 'family': 'avgwordsent', 'language': 'general'}, {'key': 'a_char_pw', 'name': 'average_number_of_characters_per_word', 'formulation': 'derivation', 'domain': 'surface', 'family': 'avgwordsent', 'language': 'general'}]
    >>> 
    >>> output = lftk.search_features(domain = 'surface', family = "avgwordsent", language="general", return_format = "list_dict")
    >>> #           key                                       name formulation   domain       family language
    >>>  #9   a_word_ps       average_number_of_words_per_sentence  derivation  surface  avgwordsent  general
    >>> # 10  a_char_ps  average_number_of_characters_per_sentence  derivation  surface  avgwordsent  general
    >>> # 11  a_char_pw      average_number_of_characters_per_word  derivation  surface  avgwordsent  general
    >>> 
    >>> output = lftk.search_features(domain = 'surface', family = "avgwordsent", language="general", return_format = "list_dict")
    >>> # ['a_word_ps', 'a_char_ps', 'a_char_pw']
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