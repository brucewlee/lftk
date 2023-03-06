[![spaCy](https://img.shields.io/badge/made%20with%20❤%20and-spaCy-09a3d5.svg)](https://spacy.io)
<img alt="PyPI Downloads" src="https://img.shields.io/pypi/dm/lftk?color=white&label=PyPI%20Downloads&style=plastic"></a>
<img alt="Language" src="https://img.shields.io/github/languages/top/brucewlee/lftk?style=plastic"></a>

# LFTK - Linguistic Features ToolKit
LFTK is a Python research package that extracts various handcrafted linguistic features (e.g. number of words per sentence, Flesch-Kincaid Readabiility Score) from a given text. LFTK is built with multilingual usage and expandability in mind. LFTK is also built on top of a popular NLP library named [spaCy](https://spacy.io), allowing users to freely explore whichever spaCy's pre-trained pipelines.

You can use LFTK to calculate readability score, evaluate word difficulty, count number of nouns, and many more.

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
# you can pass in a list of multiple docs, too
LFTK_Extractor = lftk.Extractor(docs = doc)

# optionally, you can customize how LFTK extractor should calculate linguistic features
# for example, count stop_words? how many decimals to round up?
LFTK_Extractor.customize(stop_words=False, punctuations=False, round_decimal=3)

# now, extract linguistic features that you need
# here, we test with average number of words per sentence, average word difficulty (based on Kuperman's Age-of-Acquisition research), and the total occurence of noun
extracted_features = LFTK_Extractor.extract(features = ["a_word_ps", "a_kup_pw", "n_noun"])

# {'a_word_ps': 4.0, 'a_kup_pw': 11.508, 'n_noun': 2}
print(extracted_features)
```

## Deep Dive: Linguistic Features
to be updated