from lftk.derivation.foundation_collector import FoundationCollector
from lftk.utils import safe_division

class AvgEntity(FoundationCollector):
    def average_number_of_named_entities_per_word(
        SE: object,
        ) -> float:
        try:
            return SE.average_number_of_named_entities_per_word_
        except AttributeError:
            total_number_of_words_ = \
                FoundationCollector.total_number_of_words(SE)
            total_number_of_named_entities_ = \
                FoundationCollector.total_number_of_named_entities(SE)
            SE.average_number_of_named_entities_per_word_ = \
                safe_division(
                    total_number_of_named_entities_,
                    total_number_of_words_
                )
            return SE.average_number_of_named_entities_per_word_
    

    def average_number_of_named_entities_per_sentence(
        SE: object,
        ) -> float:
        try:
            return SE.average_number_of_named_entities_per_sentence_
        except AttributeError:
            total_number_of_sentences_ = \
                FoundationCollector.total_number_of_sentences(SE)
            total_number_of_named_entities_ = \
                FoundationCollector.total_number_of_named_entities(SE)
            SE.average_number_of_named_entities_per_sentence_ = \
                safe_division(
                    total_number_of_named_entities_,
                    total_number_of_sentences_
                )
            return SE.average_number_of_named_entities_per_sentence_