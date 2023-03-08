import math

import spacy
from lftk.derivation.foundation_collector import FoundationCollector
from lftk.utils import safe_division

class ReadFormula(FoundationCollector):
    def flesch_kincaid_reading_ease(
        SE: object,
        ) -> float:
        """
        flesch kincaid reading ease formula
        100.00–90.00	5th grade	        Very easy to read.
        90.0–80.0	    6th grade	        Easy to read.
        80.0–70.0	    7th grade	        Fairly easy to read.
        70.0–60.0	    8th & 9th grade	    Plain English. 
        60.0–50.0	    10th to 12th grade	Fairly difficult to read.
        50.0–30.0	    College	            Difficult to read.
        30.0–10.0	    College graduate	Very difficult to read. 
        10.0–0.0	    Professional	    Extremely difficult to read. 
        input :
        - SE: Single Extractor object
        output:
        - SE.flesch_kincaid_reading_ease_
        """
        try:
            return SE.flesch_kincaid_reading_ease_
        except AttributeError:
            # Override user options
            original_options = SE.options
            SE.options['stop_words'] = True
            SE.options['punctuations'] = False
            # Calculate necessary foundation features
            total_number_of_words_ = \
                FoundationCollector.total_number_of_words(SE)
            total_number_of_sentences_ = \
                FoundationCollector.total_number_of_sentences(SE)
            total_number_of_syllables_ = \
                FoundationCollector.total_number_of_syllables(SE)
            average_number_of_words_per_sentence_ = \
                safe_division(
                    total_number_of_words_,
                    total_number_of_sentences_
                )
            average_number_of_syllables_per_word_ = \
                safe_division(
                    total_number_of_syllables_,
                    total_number_of_words_
                )
            # Calculate readability
            SE.flesch_kincaid_reading_ease_ = \
                206.835 - 1.015 * average_number_of_words_per_sentence_ - 84.6 * average_number_of_syllables_per_word_
            # Revert back to user options
            SE.options = original_options
            return SE.flesch_kincaid_reading_ease_
    
    def flesch_kincaid_grade_level(
        SE: object,
        ) -> float:
        """
        flesch kincaid grade level
        output number corresponds to US grade level
        input :
        - SE: Single Extractor object
        output:
        - SE.flesch_kincaid_grade_level_
        """
        try:
            return SE.flesch_kincaid_grade_level_
        except AttributeError:
            # Override user options
            original_options = SE.options
            SE.options['stop_words'] = True
            SE.options['punctuations'] = False
            # Calculate necessary foundation features
            total_number_of_words_ = \
                FoundationCollector.total_number_of_words(SE)
            total_number_of_sentences_ = \
                FoundationCollector.total_number_of_sentences(SE)
            total_number_of_syllables_ = \
                FoundationCollector.total_number_of_syllables(SE)
            average_number_of_words_per_sentence_ = \
                safe_division(
                    total_number_of_words_,
                    total_number_of_sentences_
                )
            average_number_of_syllables_per_word_ = \
                safe_division(
                    total_number_of_syllables_,
                    total_number_of_words_
                )
            # Calculate readability
            SE.flesch_kincaid_grade_level_ = \
                0.39 * average_number_of_words_per_sentence_ + 11.8 * average_number_of_syllables_per_word_ - 15.59
            # Revert back to user options
            SE.options = original_options
            return SE.flesch_kincaid_grade_level_
    
    def gunning_fog_index(
        SE: object,
        ) -> float:
        """
        gunning fog index
        17	College graduate
        16	College senior
        15	College junior
        14	College sophomore
        13	College freshman
        12	High school senior
        11	High school junior
        10	High school sophomore
        9	High school freshman
        8	Eighth grade
        7	Seventh grade
        6	Sixth grade
        input :
        - SE: Single Extractor object
        output:
        - SE.gunning_fog_index_
        """
        try:
            return SE.gunning_fog_index_
        except AttributeError:
            # Override user options
            original_options = SE.options
            SE.options['stop_words'] = True
            SE.options['punctuations'] = False
            # Calculate necessary foundation features
            total_number_of_words_ = \
                FoundationCollector.total_number_of_words(SE)
            total_number_of_sentences_ = \
                FoundationCollector.total_number_of_sentences(SE)
            total_number_of_words_more_than_two_syllables_ = \
                FoundationCollector.total_number_of_words_more_than_two_syllables(SE)
            average_number_of_words_per_sentence_ = \
                safe_division(
                    total_number_of_words_,
                    total_number_of_sentences_
                )
            average_number_of_words_more_than_two_syllables_per_word_ = \
                safe_division(
                    total_number_of_words_more_than_two_syllables_,
                    total_number_of_words_
                )
            # Calculate readability
            SE.gunning_fog_index_ = \
                0.4 * (average_number_of_words_per_sentence_ + 100 * average_number_of_words_more_than_two_syllables_per_word_)
            # Revert back to user options
            SE.options = original_options
            return SE.gunning_fog_index_
    
    def smog_index(
        SE: object,
        ) -> float:
        """
        simple measure of gobbledygook
        output number corresponds to US grade level
        input :
        - SE: Single Extractor object
        output:
        - SE.smog_index_
        """
        try:
            return SE.smog_index_
        except AttributeError:
            # Override user options
            original_options = SE.options
            SE.options['stop_words'] = True
            SE.options['punctuations'] = False
            # Calculate necessary foundation features
            total_number_of_sentences_ = \
                FoundationCollector.total_number_of_sentences(SE)
            total_number_of_words_more_than_three_syllables_ = \
                FoundationCollector.total_number_of_words_more_than_three_syllables(SE)
            # Calculate readability
            SE.smog_index_ = \
                1.0430 * math.sqrt(total_number_of_words_more_than_three_syllables_ * safe_division(30, total_number_of_sentences_))
            # Revert back to user options
            SE.options = original_options
            return SE.smog_index_

    def coleman_liau_index(
        SE: object,
        ) -> float:
        """
        coleman liau index
        output number corresponds to US grade level
        input :
        - SE: Single Extractor object
        output:
        - SE.coleman_liau_index_
        """
        try:
            return SE.coleman_liau_index_
        except AttributeError:
            # Override user options
            original_options = SE.options
            SE.options['stop_words'] = True
            SE.options['punctuations'] = False
            # Calculate necessary foundation features
            total_number_of_characters_ = \
                FoundationCollector.total_number_of_characters(SE)
            total_number_of_words_ = \
                FoundationCollector.total_number_of_words(SE)
            total_number_of_sentences_ = \
                FoundationCollector.total_number_of_sentences(SE)
            average_number_of_letters_per_100words_ = \
                safe_division(
                    total_number_of_characters_,
                    total_number_of_words_
                ) * 100
            average_number_of_sentences_per_100words_ = \
                safe_division(
                    total_number_of_sentences_,
                    total_number_of_words_
                ) * 100
            # Calculate readability
            SE.coleman_liau_index_ = \
                0.0588 * average_number_of_letters_per_100words_ - 0.296 * average_number_of_sentences_per_100words_ - 15.8
            # Revert back to user options
            SE.options = original_options
            return SE.coleman_liau_index_
    
    def automated_readability_index(
        SE: object,
        ) -> float:
        """
        automated readability index
        output number corresponds to US grade level
        input :
        - SE: Single Extractor object
        output:
        - SE.automated_readability_index_
        """
        try:
            return SE.automated_readability_index_
        except AttributeError:
            # Override user options
            original_options = SE.options
            SE.options['stop_words'] = True
            SE.options['punctuations'] = False
            # Calculate necessary foundation features
            total_number_of_characters_ = \
                FoundationCollector.total_number_of_characters(SE)
            total_number_of_words_ = \
                FoundationCollector.total_number_of_words(SE)
            total_number_of_sentences_ = \
                FoundationCollector.total_number_of_sentences(SE)
            average_number_of_letters_per_word_ = \
                safe_division(
                    total_number_of_characters_,
                    total_number_of_words_
                )
            average_number_of_words_per_sentence_ = \
                safe_division(
                    total_number_of_words_,
                    total_number_of_sentences_
                )
            # Calculate readability
            SE.automated_readability_index_ = \
                4.71 * average_number_of_letters_per_word_ + 0.5 * average_number_of_words_per_sentence_ - 21.43
            # Revert back to user options
            SE.options = original_options
            return SE.automated_readability_index_