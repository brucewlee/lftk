import spacy
from lftk.derivation.foundation_collector import FoundationCollector
from lftk.utils import safe_division

class AvgWordDiff(FoundationCollector):
    """AvgWordDiff

    Parent class for features that are in the 'avgworddiff' family.
    """

    def average_kuperman_age_of_acquistion_of_words_per_sentence(
        SE: object,
        ) -> float:
        """
        returns value of (total Kuperman score / total number of sentences)
        """
        try:
            return SE.average_kuperman_age_of_acquistion_of_words_per_sentence_
        except AttributeError:
            total_number_of_sentences_ = \
                FoundationCollector.total_number_of_sentences(SE)
            total_kuperman_age_of_acquistion_of_words_ = \
                FoundationCollector.total_kuperman_age_of_acquistion_of_words(SE)
            SE.average_kuperman_age_of_acquistion_of_words_per_sentence_ = \
                safe_division(
                    total_kuperman_age_of_acquistion_of_words_,
                    total_number_of_sentences_
                    )
            return SE.average_kuperman_age_of_acquistion_of_words_per_sentence_


    def average_kuperman_age_of_acquistion_of_words_per_word(
        SE: object,
        ) -> float:
        """
        returns value of (total Kuperman score / total number of words)
        """
        try:
            return SE.average_kuperman_age_of_acquistion_of_words_per_word_
        except AttributeError:
            total_number_of_words_ = \
                FoundationCollector.total_number_of_words(SE)
            total_kuperman_age_of_acquistion_of_words_ = \
                FoundationCollector.total_kuperman_age_of_acquistion_of_words(SE)
            SE.average_kuperman_age_of_acquistion_of_words_per_word_ = \
                safe_division(
                    total_kuperman_age_of_acquistion_of_words_,
                    total_number_of_words_
                    )
            return SE.average_kuperman_age_of_acquistion_of_words_per_word_
    

    def average_brysbaert_age_of_acquistion_of_words_per_word(
        SE: object,
        ) -> float:
        """
        returns value of (total Brysbaert score / total number of words)
        """
        try:
            return SE.average_brysbaert_age_of_acquistion_of_words_per_word_
        except AttributeError:
            total_number_of_words_ = \
                FoundationCollector.total_number_of_words(SE)
            total_brysbaert_age_of_acquistion_of_words_ = \
                FoundationCollector.total_brysbaert_age_of_acquistion_of_words(SE)
            SE.average_brysbaert_age_of_acquistion_of_words_per_word_ = \
                safe_division(
                    total_brysbaert_age_of_acquistion_of_words_,
                    total_number_of_words_
                )
            return SE.average_brysbaert_age_of_acquistion_of_words_per_word_
    

    def average_brysbaert_age_of_acquistion_of_words_per_sentence(
        SE: object,
        ) -> float:
        """
        returns value of (total Brysbaert score / total number of sentence)
        """
        try:
            return SE.average_brysbaert_age_of_acquistion_of_words_per_sentence_
        except AttributeError:
            total_number_of_sentences_ = \
                FoundationCollector.total_number_of_sentences(SE)
            total_brysbaert_age_of_acquistion_of_words_ = \
                FoundationCollector.total_brysbaert_age_of_acquistion_of_words(SE)
            SE.average_brysbaert_age_of_acquistion_of_words_per_sentence_ = \
                safe_division(
                    total_brysbaert_age_of_acquistion_of_words_,
                    total_number_of_sentences_
                )
            return SE.average_brysbaert_age_of_acquistion_of_words_per_sentence_

    
    def average_subtlex_us_zipf_of_words_per_word(
        SE: object,
        ) -> float:
        """
        returns value of (total subtlexus zipf score / total number of words)
        """
        try:
            return SE.average_subtlex_us_zipf_of_words_per_word_
        except AttributeError:
            total_number_of_words_ = \
                FoundationCollector.total_number_of_words(SE)
            total_subtlex_us_zipf_of_words_ = \
                FoundationCollector.total_subtlex_us_zipf_of_words(SE)
            SE.average_subtlex_us_zipf_of_words_per_word_ = \
                safe_division(
                    total_subtlex_us_zipf_of_words_,
                    total_number_of_words_
                )
            return SE.average_subtlex_us_zipf_of_words_per_word_
    

    def average_subtlex_us_zipf_of_words_per_sentence(
        SE: object,
        ) -> float:
        """
        returns value of (total subtlexus zipf score / total number of sentences)
        """
        try:
            return SE.average_subtlex_us_zipf_of_words_per_sentence_
        except AttributeError:
            total_number_of_sentences_ = \
                FoundationCollector.total_number_of_sentences(SE)
            total_subtlex_us_zipf_of_words_ = \
                FoundationCollector.total_subtlex_us_zipf_of_words(SE)
            SE.subtlex_us_zipf_of_words_per_sentence_ = \
                safe_division(
                    total_subtlex_us_zipf_of_words_,
                    total_number_of_sentences_
                )
            return SE.subtlex_us_zipf_of_words_per_sentence_