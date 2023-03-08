from lftk.derivation.avgwordsent import AvgWordSent
from lftk.derivation.avgworddiff import AvgWordDiff
from lftk.derivation.avgentity   import AvgEntity
from lftk.derivation.typetokenratio import TypeTokenRatio
from lftk.derivation.avgpartofspeech import AvgPartOfSpeech
from lftk.derivation.readformula import ReadFormula

class DerivationCollector(AvgWordSent, AvgWordDiff, AvgEntity, TypeTokenRatio, AvgPartOfSpeech, ReadFormula):
    pass 