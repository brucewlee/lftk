from lftk.derivation.foundation_collector import FoundationCollector
from lftk.utils import safe_division

class ReadTimeFormula(FoundationCollector):
    def reading_time_for_fast_readers(
        SE: object,
        ) -> float:
        try:
            return SE.reading_time_for_fast_readers_
        except AttributeError:
            # Override user options
            original_options = SE.options
            SE.options['stop_words'] = True
            SE.options['punctuations'] = False
            # Calculate necessary foundation features
            total_number_of_words_ = \
                FoundationCollector.total_number_of_words(SE)
            SE.reading_time_for_fast_readers_ = \
                safe_division(
                    total_number_of_words_,
                    300
                )
            # Revert back to user options
            SE.options = original_options
        return SE.reading_time_for_fast_readers_
    
    def reading_time_for_average_readers(
        SE: object,
        ) -> float:
        try:
            return SE.reading_time_for_average_readers_
        except AttributeError:
            # Override user options
            original_options = SE.options
            SE.options['stop_words'] = True
            SE.options['punctuations'] = False
            # Calculate necessary foundation features
            total_number_of_words_ = \
                FoundationCollector.total_number_of_words(SE)
            SE.reading_time_for_average_readers_ = \
                safe_division(
                    total_number_of_words_,
                    240
                )
            # Revert back to user options
            SE.options = original_options
        return SE.reading_time_for_average_readers_

    def reading_time_for_slow_readers(
        SE: object,
        ) -> float:
        try:
            return SE.reading_time_for_slow_readers_
        except AttributeError:
            # Override user options
            original_options = SE.options
            SE.options['stop_words'] = True
            SE.options['punctuations'] = False
            # Calculate necessary foundation features
            total_number_of_words_ = \
                FoundationCollector.total_number_of_words(SE)
            SE.reading_time_for_slow_readers_ = \
                safe_division(
                    total_number_of_words_,
                    175
                )
            # Revert back to user options
            SE.options = original_options
        return SE.reading_time_for_slow_readers_