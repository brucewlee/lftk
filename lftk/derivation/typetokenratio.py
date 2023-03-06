import math
from lftk.derivation.foundation_collector import FoundationCollector
from lftk.utils import safe_division

class TypeTokenRatio(FoundationCollector):
    def simple_type_token_ratio(
        SE: object,
        ) -> float:
        try:
            return SE.simple_type_token_ratio_
        except AttributeError:
            total_number_of_unique_words_ = \
                FoundationCollector.total_number_of_unique_words(SE)
            total_number_of_words_ = \
                FoundationCollector.total_number_of_words(SE)
            SE.simple_type_token_ratio_ = \
                safe_division(
                    total_number_of_unique_words_,
                    total_number_of_words_
                )
            return SE.simple_type_token_ratio_
    
    def root_type_token_ratio(
        SE: object,
        ) -> float:
        try:
            return SE.root_type_token_ratio_
        except AttributeError:
            total_number_of_unique_words_ = \
                FoundationCollector.total_number_of_unique_words(SE)
            total_number_of_words_ = \
                FoundationCollector.total_number_of_words(SE)
            SE.root_type_token_ratio_ = \
                safe_division(
                    total_number_of_unique_words_,
                    math.sqrt(total_number_of_words_)
                )
            return SE.root_type_token_ratio_
    
    def corrected_type_token_ratio(
        SE: object,
        ) -> float:
        try:
            return SE.corrected_type_token_ratio_
        except AttributeError:
            total_number_of_unique_words_ = \
                FoundationCollector.total_number_of_unique_words(SE)
            total_number_of_words_ = \
                FoundationCollector.total_number_of_words(SE)
            SE.corrected_type_token_ratio_ = \
                safe_division(
                    total_number_of_unique_words_,
                    math.sqrt(2*total_number_of_words_)
                )
            return SE.corrected_type_token_ratio_

    def bilogarithmic_type_token_ratio(
        SE: object,
        ) -> float:
        try:
            return SE.bilogarithmic_type_token_ratio_
        except AttributeError:
            total_number_of_unique_words_ = \
                FoundationCollector.total_number_of_unique_words(SE)
            total_number_of_words_ = \
                FoundationCollector.total_number_of_words(SE)
            SE.bilogarithmic_type_token_ratio_ = \
                safe_division(
                    math.log(total_number_of_unique_words_),
                    math.log(total_number_of_words_)
                )
            return SE.bilogarithmic_type_token_ratio_
    
    def uber_type_token_ratio(
        SE: object,
        ) -> float:
        try:
            return SE.uber_type_token_ratio_
        except AttributeError:
            total_number_of_unique_words_ = \
                FoundationCollector.total_number_of_unique_words(SE)
            total_number_of_words_ = \
                FoundationCollector.total_number_of_words(SE)
            SE.uber_type_token_ratio_ = \
                safe_division(
                    math.log(total_number_of_unique_words_)**2,
                    math.log(
                        safe_division(
                            total_number_of_words_, 
                            total_number_of_unique_words_
                        )
                    )
                )
            return SE.uber_type_token_ratio_

    def simple_type_token_ratio_no_lemma(
        SE: object,
        ) -> float:
        try:
            return SE.simple_type_token_ratio_no_lemma_
        except AttributeError:
            total_number_of_unique_words_no_lemma_ = \
                FoundationCollector.total_number_of_unique_words_no_lemma(SE)
            total_number_of_words_ = \
                FoundationCollector.total_number_of_words(SE)
            SE.simple_type_token_ratio_no_lemma_ = \
                safe_division(
                    total_number_of_unique_words_no_lemma_,
                    total_number_of_words_
                )
            return SE.simple_type_token_ratio_no_lemma_
    
    def root_type_token_ratio_no_lemma(
        SE: object,
        ) -> float:
        try:
            return SE.root_type_token_ratio_no_lemma_
        except AttributeError:
            total_number_of_unique_words_no_lemma_ = \
                FoundationCollector.total_number_of_unique_words_no_lemma(SE)
            total_number_of_words_ = \
                FoundationCollector.total_number_of_words(SE)
            SE.root_type_token_ratio_no_lemma_ = \
                safe_division(
                    total_number_of_unique_words_no_lemma_,
                    math.sqrt(total_number_of_words_)
                )
            return SE.root_type_token_ratio_no_lemma_
    
    def corrected_type_token_ratio_no_lemma(
        SE: object,
        ) -> float:
        try:
            return SE.corrected_type_token_ratio_no_lemma_
        except AttributeError:
            total_number_of_unique_words_no_lemma_ = \
                FoundationCollector.total_number_of_unique_words_no_lemma(SE)
            total_number_of_words_ = \
                FoundationCollector.total_number_of_words(SE)
            SE.corrected_type_token_ratio_no_lemma_ = \
                safe_division(
                    total_number_of_unique_words_no_lemma_,
                    math.sqrt(2*total_number_of_words_)
                )
            return SE.corrected_type_token_ratio_no_lemma_

    def bilogarithmic_type_token_ratio_no_lemma(
        SE: object,
        ) -> float:
        try:
            return SE.bilogarithmic_type_token_ratio_no_lemma_
        except AttributeError:
            total_number_of_unique_words_no_lemma_ = \
                FoundationCollector.total_number_of_unique_words_no_lemma(SE)
            total_number_of_words_ = \
                FoundationCollector.total_number_of_words(SE)
            SE.bilogarithmic_type_token_ratio_no_lemma_ = \
                safe_division(
                    math.log(total_number_of_unique_words_no_lemma_),
                    math.log(total_number_of_words_)
                )
            return SE.bilogarithmic_type_token_ratio_no_lemma_
    
    def uber_type_token_ratio_no_lemma(
        SE: object,
        ) -> float:
        try:
            return SE.uber_type_token_ratio_no_lemma_
        except AttributeError:
            total_number_of_unique_words_no_lemma_ = \
                FoundationCollector.total_number_of_unique_words_no_lemma(SE)
            total_number_of_words_ = \
                FoundationCollector.total_number_of_words(SE)
            SE.uber_type_token_ratio_no_lemma_ = \
                safe_division(
                    math.log(total_number_of_unique_words_no_lemma_)**2,
                    math.log(
                        safe_division(
                            total_number_of_words_, 
                            total_number_of_unique_words_no_lemma_
                        )
                    )
                )
            return SE.uber_type_token_ratio_no_lemma_
