from lftk.derivation.foundation_collector import FoundationCollector
from lftk.utils import safe_division

class AvgPartOfSpeech(FoundationCollector):
    def average_number_of_adjectives_per_word(
        SE: object,
        ) -> float:
        try:
            return SE.average_number_of_adjectives_per_word_
        except AttributeError:
            total_number_of_words_ = \
                FoundationCollector.total_number_of_words(SE)
            total_number_of_adjectives_ = \
                FoundationCollector.total_number_of_adjectives(SE)
            SE.average_number_of_adjectives_per_word_ = \
                safe_division(
                    total_number_of_adjectives_,
                    total_number_of_words_
                )
            return SE.average_number_of_adjectives_per_word_
    
    def average_number_of_adjectives_per_sentence(
        SE: object,
        ) -> float:
        try:
            return SE.average_number_of_adjectives_per_sentence_
        except AttributeError:
            total_number_of_sentences_ = \
                FoundationCollector.total_number_of_sentences(SE)
            total_number_of_adjectives_ = \
                FoundationCollector.total_number_of_adjectives(SE)
            SE.average_number_of_adjectives_per_sentence_ = \
                safe_division(
                    total_number_of_adjectives_,
                    total_number_of_sentences_
                )
            return SE.average_number_of_adjectives_per_sentence_

    def average_number_of_adpositions_per_word(
        SE: object,
        ) -> float:
        try:
            return SE.average_number_of_adpositions_per_word_
        except AttributeError:
            total_number_of_words_ = \
                FoundationCollector.total_number_of_words(SE)
            total_number_of_adpositions_ = \
                FoundationCollector.total_number_of_adpositions(SE)
            SE.average_number_of_adpositions_per_word_ = \
                safe_division(
                    total_number_of_adpositions_,
                    total_number_of_words_
                )
            return SE.average_number_of_adpositions_per_word_
    
    def average_number_of_adpositions_per_sentence(
        SE: object,
        ) -> float:
        try:
            return SE.average_number_of_adpositions_per_sentence_
        except AttributeError:
            total_number_of_sentences_ = \
                FoundationCollector.total_number_of_sentences(SE)
            total_number_of_adpositions_ = \
                FoundationCollector.total_number_of_adpositions(SE)
            SE.average_number_of_adpositions_per_sentence_ = \
                safe_division(
                    total_number_of_adpositions_,
                    total_number_of_sentences_
                )
            return SE.average_number_of_adpositions_per_sentence_
    
    def average_number_of_adverbs_per_word(
        SE: object,
        ) -> float:
        try:
            return SE.average_number_of_adverbs_per_word_
        except AttributeError:
            total_number_of_words_ = \
                FoundationCollector.total_number_of_words(SE)
            total_number_of_adverbs_ = \
                FoundationCollector.total_number_of_adverbs(SE)
            SE.average_number_of_adverbs_per_word_ = \
                safe_division(
                    total_number_of_adverbs_,
                    total_number_of_words_
                )
            return SE.average_number_of_adverbs_per_word_
    
    def average_number_of_adverbs_per_sentence(
        SE: object,
        ) -> float:
        try:
            return SE.average_number_of_adverbs_per_sentence_
        except AttributeError:
            total_number_of_sentences_ = \
                FoundationCollector.total_number_of_sentences(SE)
            total_number_of_adverbs_ = \
                FoundationCollector.total_number_of_adverbs(SE)
            SE.average_number_of_adverbs_per_sentence_ = \
                safe_division(
                    total_number_of_adverbs_,
                    total_number_of_sentences_
                )
            return SE.average_number_of_adverbs_per_sentence_
    
    def average_number_of_auxiliaries_per_word(
        SE: object,
        ) -> float:
        try:
            return SE.average_number_of_auxiliaries_per_word_
        except AttributeError:
            total_number_of_words_ = \
                FoundationCollector.total_number_of_words(SE)
            total_number_of_auxiliaries_ = \
                FoundationCollector.total_number_of_auxiliaries(SE)
            SE.average_number_of_auxiliaries_per_word_ = \
                safe_division(
                    total_number_of_auxiliaries_,
                    total_number_of_words_
                )
            return SE.average_number_of_auxiliaries_per_word_
    
    def average_number_of_auxiliaries_per_sentence(
        SE: object,
        ) -> float:
        try:
            return SE.average_number_of_auxiliaries_per_sentence_
        except AttributeError:
            total_number_of_sentences_ = \
                FoundationCollector.total_number_of_sentences(SE)
            total_number_of_auxiliaries_ = \
                FoundationCollector.total_number_of_auxiliaries(SE)
            SE.average_number_of_auxiliaries_per_sentence_ = \
                safe_division(
                    total_number_of_auxiliaries_,
                    total_number_of_sentences_
                )
            return SE.average_number_of_auxiliaries_per_sentence_
    
    def average_number_of_conjunctions_per_word(
        SE: object,
        ) -> float:
        try:
            return SE.average_number_of_conjunctions_per_word_
        except AttributeError:
            total_number_of_words_ = \
                FoundationCollector.total_number_of_words(SE)
            total_number_of_conjunctions_ = \
                FoundationCollector.total_number_of_conjunctions(SE)
            SE.average_number_of_conjunctions_per_word_ = \
                safe_division(
                    total_number_of_conjunctions_,
                    total_number_of_words_
                )
            return SE.average_number_of_conjunctions_per_word_
    
    def average_number_of_conjunctions_per_sentence(
        SE: object,
        ) -> float:
        try:
            return SE.average_number_of_conjunctions_per_sentence_
        except AttributeError:
            total_number_of_sentences_ = \
                FoundationCollector.total_number_of_sentences(SE)
            total_number_of_conjunctions_ = \
                FoundationCollector.total_number_of_conjunctions(SE)
            SE.average_number_of_conjunctions_per_sentence_ = \
                safe_division(
                    total_number_of_conjunctions_,
                    total_number_of_sentences_
                )
            return SE.average_number_of_conjunctions_per_sentence_

    def average_number_of_coordinating_conjunctions_per_word(
        SE: object,
        ) -> float:
        try:
            return SE.average_number_of_coordinating_conjunctions_per_word_
        except AttributeError:
            total_number_of_words_ = \
                FoundationCollector.total_number_of_words(SE)
            total_number_of_coordinating_conjunctions_ = \
                FoundationCollector.total_number_of_coordinating_conjunctions(SE)
            SE.average_number_of_coordinating_conjunctions_per_word_ = \
                safe_division(
                    total_number_of_coordinating_conjunctions_,
                    total_number_of_words_
                )
            return SE.average_number_of_coordinating_conjunctions_per_word_
    
    def average_number_of_coordinating_conjunctions_per_sentence(
        SE: object,
        ) -> float:
        try:
            return SE.average_number_of_coordinating_conjunctions_per_sentence_
        except AttributeError:
            total_number_of_sentences_ = \
                FoundationCollector.total_number_of_sentences(SE)
            total_number_of_coordinating_conjunctions_ = \
                FoundationCollector.total_number_of_coordinating_conjunctions(SE)
            SE.average_number_of_coordinating_conjunctions_per_sentence_ = \
                safe_division(
                    total_number_of_coordinating_conjunctions_,
                    total_number_of_sentences_
                )
            return SE.average_number_of_coordinating_conjunctions_per_sentence_

    def average_number_of_determiners_per_word(
        SE: object,
        ) -> float:
        try:
            return SE.average_number_of_determiners_per_word_
        except AttributeError:
            total_number_of_words_ = \
                FoundationCollector.total_number_of_words(SE)
            total_number_of_determiners_ = \
                FoundationCollector.total_number_of_determiners(SE)
            SE.average_number_of_determiners_per_word_ = \
                safe_division(
                    total_number_of_determiners_,
                    total_number_of_words_
                )
            return SE.average_number_of_determiners_per_word_
    
    def average_number_of_determiners_per_sentence(
        SE: object,
        ) -> float:
        try:
            return SE.average_number_of_determiners_per_sentence_
        except AttributeError:
            total_number_of_sentences_ = \
                FoundationCollector.total_number_of_sentences(SE)
            total_number_of_determiners_ = \
                FoundationCollector.total_number_of_determiners(SE)
            SE.average_number_of_determiners_per_sentence_ = \
                safe_division(
                    total_number_of_determiners_,
                    total_number_of_sentences_
                )
            return SE.average_number_of_determiners_per_sentence_

    def average_number_of_interjections_per_word(
        SE: object,
        ) -> float:
        try:
            return SE.average_number_of_interjections_per_word_
        except AttributeError:
            total_number_of_words_ = \
                FoundationCollector.total_number_of_words(SE)
            total_number_of_interjections_ = \
                FoundationCollector.total_number_of_interjections(SE)
            SE.average_number_of_interjections_per_word_ = \
                safe_division(
                    total_number_of_interjections_,
                    total_number_of_words_
                )
            return SE.average_number_of_interjections_per_word_
    
    def average_number_of_interjections_per_sentence(
        SE: object,
        ) -> float:
        try:
            return SE.average_number_of_interjections_per_sentence_
        except AttributeError:
            total_number_of_sentences_ = \
                FoundationCollector.total_number_of_sentences(SE)
            total_number_of_interjections_ = \
                FoundationCollector.total_number_of_interjections(SE)
            SE.average_number_of_interjections_per_sentence_ = \
                safe_division(
                    total_number_of_interjections_,
                    total_number_of_sentences_
                )
            return SE.average_number_of_interjections_per_sentence_

    def average_number_of_nouns_per_word(
        SE: object,
        ) -> float:
        try:
            return SE.average_number_of_nouns_per_word_
        except AttributeError:
            total_number_of_words_ = \
                FoundationCollector.total_number_of_words(SE)
            total_number_of_nouns_ = \
                FoundationCollector.total_number_of_nouns(SE)
            SE.average_number_of_nouns_per_word_ = \
                safe_division(
                    total_number_of_nouns_,
                    total_number_of_words_
                )
            return SE.average_number_of_nouns_per_word_
    
    def average_number_of_nouns_per_sentence(
        SE: object,
        ) -> float:
        try:
            return SE.average_number_of_nouns_per_sentence_
        except AttributeError:
            total_number_of_sentences_ = \
                FoundationCollector.total_number_of_sentences(SE)
            total_number_of_nouns_ = \
                FoundationCollector.total_number_of_nouns(SE)
            SE.average_number_of_nouns_per_sentence_ = \
                safe_division(
                    total_number_of_nouns_,
                    total_number_of_sentences_
                )
            return SE.average_number_of_nouns_per_sentence_

    def average_number_of_numerals_per_word(
        SE: object,
        ) -> float:
        try:
            return SE.average_number_of_numerals_per_word_
        except AttributeError:
            total_number_of_words_ = \
                FoundationCollector.total_number_of_words(SE)
            total_number_of_numerals_ = \
                FoundationCollector.total_number_of_numerals(SE)
            SE.average_number_of_numerals_per_word_ = \
                safe_division(
                    total_number_of_numerals_,
                    total_number_of_words_
                )
            return SE.average_number_of_numerals_per_word_
    
    def average_number_of_numerals_per_sentence(
        SE: object,
        ) -> float:
        try:
            return SE.average_number_of_numerals_per_sentence_
        except AttributeError:
            total_number_of_sentences_ = \
                FoundationCollector.total_number_of_sentences(SE)
            total_number_of_numerals_ = \
                FoundationCollector.total_number_of_numerals(SE)
            SE.average_number_of_numerals_per_sentence_ = \
                safe_division(
                    total_number_of_numerals_,
                    total_number_of_sentences_
                )
            return SE.average_number_of_numerals_per_sentence_

    def average_number_of_particles_per_word(
        SE: object,
        ) -> float:
        try:
            return SE.average_number_of_particles_per_word_
        except AttributeError:
            total_number_of_words_ = \
                FoundationCollector.total_number_of_words(SE)
            total_number_of_particles_ = \
                FoundationCollector.total_number_of_particles(SE)
            SE.average_number_of_particles_per_word_ = \
                safe_division(
                    total_number_of_particles_,
                    total_number_of_words_
                )
            return SE.average_number_of_particles_per_word_
    
    def average_number_of_particles_per_sentence(
        SE: object,
        ) -> float:
        try:
            return SE.average_number_of_particles_per_sentence_
        except AttributeError:
            total_number_of_sentences_ = \
                FoundationCollector.total_number_of_sentences(SE)
            total_number_of_particles_ = \
                FoundationCollector.total_number_of_particles(SE)
            SE.average_number_of_particles_per_sentence_ = \
                safe_division(
                    total_number_of_particles_,
                    total_number_of_sentences_
                )
            return SE.average_number_of_particles_per_sentence_

    def average_number_of_pronouns_per_word(
        SE: object,
        ) -> float:
        try:
            return SE.average_number_of_pronouns_per_word_
        except AttributeError:
            total_number_of_words_ = \
                FoundationCollector.total_number_of_words(SE)
            total_number_of_pronouns_ = \
                FoundationCollector.total_number_of_pronouns(SE)
            SE.average_number_of_pronouns_per_word_ = \
                safe_division(
                    total_number_of_pronouns_,
                    total_number_of_words_
                )
            return SE.average_number_of_pronouns_per_word_
    
    def average_number_of_pronouns_per_sentence(
        SE: object,
        ) -> float:
        try:
            return SE.average_number_of_pronouns_per_sentence_
        except AttributeError:
            total_number_of_sentences_ = \
                FoundationCollector.total_number_of_sentences(SE)
            total_number_of_pronouns_ = \
                FoundationCollector.total_number_of_pronouns(SE)
            SE.average_number_of_pronouns_per_sentence_ = \
                safe_division(
                    total_number_of_pronouns_,
                    total_number_of_sentences_
                )
            return SE.average_number_of_pronouns_per_sentence_

    def average_number_of_proper_nouns_per_word(
        SE: object,
        ) -> float:
        try:
            return SE.average_number_of_proper_nouns_per_word_
        except AttributeError:
            total_number_of_words_ = \
                FoundationCollector.total_number_of_words(SE)
            total_number_of_proper_nouns_ = \
                FoundationCollector.total_number_of_proper_nouns(SE)
            SE.average_number_of_proper_nouns_per_word_ = \
                safe_division(
                    total_number_of_proper_nouns_,
                    total_number_of_words_
                )
            return SE.average_number_of_proper_nouns_per_word_
    
    def average_number_of_proper_nouns_per_sentence(
        SE: object,
        ) -> float:
        try:
            return SE.average_number_of_proper_nouns_per_sentence_
        except AttributeError:
            total_number_of_sentences_ = \
                FoundationCollector.total_number_of_sentences(SE)
            total_number_of_proper_nouns_ = \
                FoundationCollector.total_number_of_proper_nouns(SE)
            SE.average_number_of_proper_nouns_per_sentence_ = \
                safe_division(
                    total_number_of_proper_nouns_,
                    total_number_of_sentences_
                )
            return SE.average_number_of_proper_nouns_per_sentence_

    def average_number_of_punctuations_per_word(
        SE: object,
        ) -> float:
        try:
            return SE.average_number_of_punctuations_per_word_
        except AttributeError:
            total_number_of_words_ = \
                FoundationCollector.total_number_of_words(SE)
            total_number_of_punctuations_ = \
                FoundationCollector.total_number_of_punctuations(SE)
            SE.average_number_of_punctuations_per_word_ = \
                safe_division(
                    total_number_of_punctuations_,
                    total_number_of_words_
                )
            return SE.average_number_of_punctuations_per_word_
    
    def average_number_of_punctuations_per_sentence(
        SE: object,
        ) -> float:
        try:
            return SE.average_number_of_punctuations_per_sentence_
        except AttributeError:
            total_number_of_sentences_ = \
                FoundationCollector.total_number_of_sentences(SE)
            total_number_of_punctuations_ = \
                FoundationCollector.total_number_of_punctuations(SE)
            SE.average_number_of_punctuations_per_sentence_ = \
                safe_division(
                    total_number_of_punctuations_,
                    total_number_of_sentences_
                )
            return SE.average_number_of_punctuations_per_sentence_

    def average_number_of_subordinating_conjunctions_per_word(
        SE: object,
        ) -> float:
        try:
            return SE.average_number_of_subordinating_conjunctions_per_word_
        except AttributeError:
            total_number_of_words_ = \
                FoundationCollector.total_number_of_words(SE)
            total_number_of_subordinating_conjunctions_ = \
                FoundationCollector.total_number_of_subordinating_conjunctions(SE)
            SE.average_number_of_subordinating_conjunctions_per_word_ = \
                safe_division(
                    total_number_of_subordinating_conjunctions_,
                    total_number_of_words_
                )
            return SE.average_number_of_subordinating_conjunctions_per_word_
    
    def average_number_of_subordinating_conjunctions_per_sentence(
        SE: object,
        ) -> float:
        try:
            return SE.average_number_of_subordinating_conjunctions_per_sentence_
        except AttributeError:
            total_number_of_sentences_ = \
                FoundationCollector.total_number_of_sentences(SE)
            total_number_of_subordinating_conjunctions_ = \
                FoundationCollector.total_number_of_subordinating_conjunctions(SE)
            SE.average_number_of_subordinating_conjunctions_per_sentence_ = \
                safe_division(
                    total_number_of_subordinating_conjunctions_,
                    total_number_of_sentences_
                )
            return SE.average_number_of_subordinating_conjunctions_per_sentence_

    def average_number_of_symbols_per_word(
        SE: object,
        ) -> float:
        try:
            return SE.average_number_of_symbols_per_word_
        except AttributeError:
            total_number_of_words_ = \
                FoundationCollector.total_number_of_words(SE)
            total_number_of_symbols_ = \
                FoundationCollector.total_number_of_symbols(SE)
            SE.average_number_of_symbols_per_word_ = \
                safe_division(
                    total_number_of_symbols_,
                    total_number_of_words_
                )
            return SE.average_number_of_symbols_per_word_
    
    def average_number_of_symbols_per_sentence(
        SE: object,
        ) -> float:
        try:
            return SE.average_number_of_symbols_per_sentence_
        except AttributeError:
            total_number_of_sentences_ = \
                FoundationCollector.total_number_of_sentences(SE)
            total_number_of_symbols_ = \
                FoundationCollector.total_number_of_symbols(SE)
            SE.average_number_of_symbols_per_sentence_ = \
                safe_division(
                    total_number_of_symbols_,
                    total_number_of_sentences_
                )
            return SE.average_number_of_symbols_per_sentence_

    def average_number_of_verbs_per_word(
        SE: object,
        ) -> float:
        try:
            return SE.average_number_of_verbs_per_word_
        except AttributeError:
            total_number_of_words_ = \
                FoundationCollector.total_number_of_words(SE)
            total_number_of_verbs_ = \
                FoundationCollector.total_number_of_verbs(SE)
            SE.average_number_of_verbs_per_word_ = \
                safe_division(
                    total_number_of_verbs_,
                    total_number_of_words_
                )
            return SE.average_number_of_verbs_per_word_
    
    def average_number_of_verbs_per_sentence(
        SE: object,
        ) -> float:
        try:
            return SE.average_number_of_verbs_per_sentence_
        except AttributeError:
            total_number_of_sentences_ = \
                FoundationCollector.total_number_of_sentences(SE)
            total_number_of_verbs_ = \
                FoundationCollector.total_number_of_verbs(SE)
            SE.average_number_of_verbs_per_sentence_ = \
                safe_division(
                    total_number_of_verbs_,
                    total_number_of_sentences_
                )
            return SE.average_number_of_verbs_per_sentence_

    def average_number_of_spaces_per_word(
        SE: object,
        ) -> float:
        try:
            return SE.average_number_of_spaces_per_word_
        except AttributeError:
            total_number_of_words_ = \
                FoundationCollector.total_number_of_words(SE)
            total_number_of_spaces_ = \
                FoundationCollector.total_number_of_spaces(SE)
            SE.average_number_of_spaces_per_word_ = \
                safe_division(
                    total_number_of_spaces_,
                    total_number_of_words_
                )
            return SE.average_number_of_spaces_per_word_
    
    def average_number_of_spaces_per_sentence(
        SE: object,
        ) -> float:
        try:
            return SE.average_number_of_spaces_per_sentence_
        except AttributeError:
            total_number_of_sentences_ = \
                FoundationCollector.total_number_of_sentences(SE)
            total_number_of_spaces_ = \
                FoundationCollector.total_number_of_spaces(SE)
            SE.average_number_of_spaces_per_sentence_ = \
                safe_division(
                    total_number_of_spaces_,
                    total_number_of_sentences_
                )
            return SE.average_number_of_spaces_per_sentence_