[![spaCy](https://img.shields.io/badge/made%20with%20❤%20and-spaCy-09a3d5.svg)](https://spacy.io)
<img alt="PyPI Downloads" src="https://img.shields.io/pypi/dm/lftk?color=white&label=PyPI%20Downloads&style=plastic"></a>
<img alt="Language" src="https://img.shields.io/github/languages/top/brucewlee/lftk?style=plastic"></a>
<img alt="Available Features" src="https://img.shields.io/badge/Linguistic%20Feature%20Count-94-yellowgreen"></a>
<img alt="Latest Version" src="https://img.shields.io/badge/Latest%20Version-1.0.2-red"></a>
<img src="assets/logo-color.png" width="250" align="right">

# LFTK
- **What is LFTK?**: LFTK is a Python research package that extracts various handcrafted linguistic features (e.g. number of words per sentence, Flesch-Kincaid Readabiility Score) from a given text. 
- **What is good?**: LFTK is built with multilingual usage and expandability in mind. LFTK is rooted in its predecessor, [LingFeat](https://github.com/brucewlee/lingfeat).
- **Expands spaCy**: LFTK is also built on top of a popular NLP library named [spaCy](https://spacy.io), allowing users to freely explore spaCy's pre-trained pipelines.

You can use LFTK to calculate readability score, evaluate word difficulty, count number of nouns, and many more. There is much to explore in this package.

## Installation
Use package manager [pip](https://pip.pypa.io/en/stable/) to install LFTK. 

```bash
pip install lftk
```

Also, install spaCy and a [trained spaCy pipeline of your choice](https://spacy.io/usage). Here, we use en_core_web_sm.

```bash
pip install spacy

python -m spacy download en_core_web_sm
```

## Usage

```python
import spacy
import lftk

# load a trained pipeline of your choice from spacy
# remember we already downloaed "en_core_web_sm" pipeline above?
nlp = spacy.load("en_core_web_sm")

# create a spaCy doc object
doc = nlp("I love research but my professor is strange.")

# initiate LFTK extractor by passing in doc
# you can pass in a list of multiple docs
LFTK_Extractor = lftk.Extractor(docs = doc)

# optionally, you can customize how LFTK extractor calculates linguistic features
# for example, count stop_words (common words)? how many decimals to round up?
LFTK_Extractor.customize(stop_words=True, punctuations=False, round_decimal=3)

# now, extract linguistic features that you need
# here, we test with the average number of words per sentence, average word difficulty (based 
# on Kuperman's Age-of-Acquisition research), and the total occurence of nouns
extracted_features = LFTK_Extractor.extract(features = ["a_word_ps", "a_kup_pw", "n_noun"])

# {'a_word_ps': 8.0, 'a_kup_pw': 5.754, 'n_noun': 2}
print(extracted_features)

# how you customize LFTK extractor can bring varying results
LFTK_Extractor.customize(stop_words=False, punctuations=False, round_decimal=3)
extracted_features = LFTK_Extractor.extract(features = ["a_word_ps", "a_kup_pw", "n_noun"])

# {'a_word_ps': 4.0, 'a_kup_pw': 11.508, 'n_noun': 2}
print(extracted_features)

# extract function will extract all available features by default
extracted_features = LFTK_Extractor.extract()

# {'t_word': 4, ..., 'a_space_ps': 1.0}
print(extracted_features)
```

## Deep Dive: Linguistic Features

All linguistic features available in LFTK are categorized into domain, then family. Domain (e.g. lexico-semantic, discourse) refers to the linguistic branch that the feature belongs to. Family is a smaller group of linguistic features that share common properties in terms of calculation steps and function. 

Each linguistic feature can either foundation or derivation. Derivation-type linguistic features are derived on top of foundation-type linguistic features. For example, the *total number of words* and the *total number of sentences* in a given text is a foundation feature. On the other hand, the *average number of words per sentence* is a derivation feature as it builds on top of the two aforementioned foundation features.

Each linguistic feature also has an assigned language value. If the linguistic feature is universally applicable across languages, it is denoted "general". These general linguistic features can be used with any language given that spaCy has a supporting pipeline for that functionality in that language. This can be easily checked on [spaCy pipelines](https://universaldependencies.org/u/pos/). If the feature is designed for a specific language, like English, it is denoted with the specific language code.

### Programmatically Searching Linguistic Features

```python
import lftk

# returns all available features as a list of dictionaries by default
searched_features = lftk.search_features()

# [{'key': 't_word', 'name': 'total_number_of_words', 'formulation': 'foundation', 'domain': 'surface', 'family': 'wordsent'}, {'key': 't_uword', 'name': 'total_number_of_unique_words', 'formulation': 'foundation', 'domain': 'surface', 'family': 'wordsent'}, {'key': 't_sent', 'name': 'total_number_of_sentences', 'formulation': 'foundation', 'domain': 'surface', 'family': 'wordsent'},...]
print(searched_features)

# specify domain or family
searched_features = lftk.search_features(domain = "surface", family = "avgwordsent")

# [{'key': 'a_word_ps', 'name': 'average_number_of_words_per_sentence', 'formulation': 'derivation', 'domain': 'surface', 'family': 'avgwordsent'}, {'key': 'a_char_ps', 'name': 'average_number_of_characters_per_sentence', 'formulation': 'derivation', 'domain': 'surface', 'family': 'avgwordsent'}, {'key': 'a_char_pw', 'name': 'average_number_of_characters_per_word', 'formulation': 'derivation', 'domain': 'surface', 'family': 'avgwordsent'}]
print(searched_features)

# return pandas dataframe instead of list of dictionaries
searched_features = lftk.search_features(domain = 'surface', family = "avgwordsent", pandas=True)

#   key                                             name formulation   domain       family
#4  a_word_ps       average_number_of_words_per_sentence  derivation  surface  avgwordsent
#5  a_char_ps  average_number_of_characters_per_sentence  derivation  surface  avgwordsent
#6  a_char_pw      average_number_of_characters_per_word  derivation  surface  avgwordsent
print(searched_features)
```

### Google Sheet of All Lingusitic Features
[Link to Sheet](https://docs.google.com/spreadsheets/d/1uXtQ1ah0OL9cmHp2Hey0QcHb4bifJcQFLvYlVIAWWwQ/edit?usp=sharing)

### Domains
- **surface** : surface-level features that often do not represent a specific linguistic property
- **lexico-semantics** : attributes associated with words
- **discourse** : high-level dependencies between words and sentences
- **syntax** : arrangement of words and phrases

### Families - Foundation
- **wordsent** : basic counts of words and sentences
- **worddiff** : difficulty, familiarity, frequency of words
- **partofspeech** : features that deals with part of speech properties, we follow the [universal POS](https://universaldependencies.org/u/pos/) tagging scheme
- **entity** : named entities or entities such as location or person

### Families - Derivation
- **avgwordsent** : averaging **wordsent** features over certain spans
- **avgworddiff** : averaging **worddiff** features over certain spans
- **avgpartofspeech**  : averaging **partofspeech** features over certain spans
- **avgentity** : averaging **entity** features over certain spans
- **typetokenratio**  : type token ratio is known to capture lexical richness of a text
- **readformula** : traditional readability formulas that calculate text readability