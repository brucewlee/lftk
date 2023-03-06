from lftk.foundation.wordsent import WordSent
from lftk.foundation.worddiff import WordDiff
from lftk.foundation.entity   import Entity
from lftk.foundation.partofspeech import PartOfSpeech

class FoundationCollector(WordSent, WordDiff, Entity, PartOfSpeech):
    pass