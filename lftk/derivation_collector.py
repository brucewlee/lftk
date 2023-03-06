from lftk.derivation.avgwordsent import AvgWordSent
from lftk.derivation.avgworddiff import AvgWordDiff
from lftk.derivation.avgentity   import AvgEntity
from lftk.derivation.typetokenratio import TypeTokenRatio

class DerivationCollector(AvgWordSent, AvgWordDiff, AvgEntity, TypeTokenRatio):
    pass 