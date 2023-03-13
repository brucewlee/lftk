import spacy
from lftk.derivation.foundation_collector import FoundationCollector
from lftk.utils import safe_division

class AvgWordSent(FoundationCollector):
    def average_number_of_words_per_sentence(
        SE: object,
        ) -> float:
        try:
            return SE.average_number_of_words_per_sentence_
        except AttributeError:
            total_number_of_words_ = \
                FoundationCollector.total_number_of_words(SE)
            total_number_of_sentences_ = \
                FoundationCollector.total_number_of_sentences(SE)
            SE.average_number_of_words_per_sentence_ = \
                safe_division(
                    total_number_of_words_,
                    total_number_of_sentences_
                )
            return SE.average_number_of_words_per_sentence_
    
    def average_number_of_characters_per_sentence(
        SE: object,
        ) -> float:
        try:
            return SE.average_number_of_characters_per_sentence_
        except AttributeError:
            total_number_of_characters_ = \
                FoundationCollector.total_number_of_characters(SE)
            total_number_of_sentences_ = \
                FoundationCollector.total_number_of_sentences(SE)
            SE.average_number_of_characters_per_sentence_ = \
                safe_division(
                    total_number_of_characters_,
                    total_number_of_sentences_
                )
            return SE.average_number_of_characters_per_sentence_

    def average_number_of_characters_per_word(
        SE: object,
        ) -> float:
        try:
            return SE.average_number_of_characters_per_word_
        except AttributeError:
            total_number_of_characters_ = \
                FoundationCollector.total_number_of_characters(SE)
            total_number_of_words_ = \
                FoundationCollector.total_number_of_words(SE)
            SE.average_number_of_characters_per_word_ = \
                safe_division(
                    total_number_of_characters_,
                    total_number_of_words_
                )
            return SE.average_number_of_characters_per_word_

    def average_number_of_syllables_per_sentence(
        SE: object,
        ) -> float:
        try:
            return SE.average_number_of_syllables_per_sentence_
        except AttributeError:
            total_number_of_syllables_ = \
                FoundationCollector.total_number_of_syllables(SE)
            total_number_of_sentences_ = \
                FoundationCollector.total_number_of_sentences(SE)
            SE.average_number_of_syllables_per_sentence_ = \
                safe_division(
                    total_number_of_syllables_,
                    total_number_of_sentences_
                )
            return SE.average_number_of_syllables_per_sentence_

    def average_number_of_syllables_per_word(
        SE: object,
        ) -> float:
        try:
            return SE.average_number_of_syllables_per_word_
        except AttributeError:
            total_number_of_syllables_ = \
                FoundationCollector.total_number_of_syllables(SE)
            total_number_of_words_ = \
                FoundationCollector.total_number_of_words(SE)
            SE.average_number_of_syllables_per_word_ = \
                safe_division(
                    total_number_of_syllables_,
                    total_number_of_words_
                )
            return SE.average_number_of_syllables_per_word_
    
    def average_number_of_stop_words_per_sentence(
        SE: object,
        ) -> float:
        try:
            return SE.average_number_of_stop_words_per_sentence_
        except AttributeError:
            total_number_of_stop_words_ = \
                FoundationCollector.total_number_of_stop_words(SE)
            total_number_of_sentences_ = \
                FoundationCollector.total_number_of_sentences(SE)
            SE.average_number_of_stop_words_per_sentence_ = \
                safe_division(
                    total_number_of_stop_words_,
                    total_number_of_sentences_
                )
            return SE.average_number_of_stop_words_per_sentence_

    def average_number_of_stop_words_per_word(
        SE: object,
        ) -> float:
        try:
            return SE.average_number_of_stop_words_per_word_
        except AttributeError:
            total_number_of_stop_words_ = \
                FoundationCollector.total_number_of_stop_words(SE)
            total_number_of_words_ = \
                FoundationCollector.total_number_of_words(SE)
            SE.average_number_of_stop_words_per_word_ = \
                safe_division(
                    total_number_of_stop_words_,
                    total_number_of_words_
                )
            return SE.average_number_of_stop_words_per_word_

    def average_number_of_punctuations_per_sentence(
        SE: object,
        ) -> float:
        try:
            return SE.average_number_of_punctuations_per_sentence_
        except AttributeError:
            total_number_of_punctuations_ = \
                FoundationCollector.total_number_of_punctuations(SE)
            total_number_of_sentences_ = \
                FoundationCollector.total_number_of_sentences(SE)
            SE.average_number_of_punctuations_per_sentence_ = \
                safe_division(
                    total_number_of_punctuations_,
                    total_number_of_sentences_
                )
            return SE.average_number_of_punctuations_per_sentence_

    def average_number_of_punctuations_per_word(
        SE: object,
        ) -> float:
        try:
            return SE.average_number_of_punctuations_per_word_
        except AttributeError:
            total_number_of_punctuations_ = \
                FoundationCollector.total_number_of_punctuations(SE)
            total_number_of_words_ = \
                FoundationCollector.total_number_of_words(SE)
            SE.average_number_of_punctuations_per_word_ = \
                safe_division(
                    total_number_of_punctuations_,
                    total_number_of_words_
                )
            return SE.average_number_of_punctuations_per_word_