import math

from lftk.derivation.foundation_collector import FoundationCollector
from lftk.utils import safe_division

class LexicalVariation(FoundationCollector):
    def simple_adjectives_variation(
        SE: object,
        ) -> float:
        try:
            return SE.simple_adjectives_variation_
        except AttributeError:
            total_number_of_unique_adjectives_ = \
                FoundationCollector.total_number_of_unique_adjectives(SE)
            total_number_of_adjectives_ = \
                FoundationCollector.total_number_of_adjectives(SE)
            SE.simple_adjectives_variation_ = \
                safe_division(
                    total_number_of_unique_adjectives_,
                    total_number_of_adjectives_
                )
            return SE.simple_adjectives_variation_
    
    def root_adjectives_variation(
        SE: object,
        ) -> float:
        try:
            return SE.root_adjectives_variation_
        except AttributeError:
            total_number_of_unique_adjectives_ = \
                FoundationCollector.total_number_of_unique_adjectives(SE)
            total_number_of_adjectives_ = \
                FoundationCollector.total_number_of_adjectives(SE)
            SE.root_adjectives_variation_ = \
                safe_division(
                    total_number_of_unique_adjectives_,
                    math.sqrt(total_number_of_adjectives_)
                )
            return SE.root_adjectives_variation_
        
    def corrected_adjectives_variation(
        SE: object,
        ) -> float:
        try:
            return SE.corrected_adjectives_variation_
        except AttributeError:
            total_number_of_unique_adjectives_ = \
                FoundationCollector.total_number_of_unique_adjectives(SE)
            total_number_of_adjectives_ = \
                FoundationCollector.total_number_of_adjectives(SE)
            SE.corrected_adjectives_variation_ = \
                safe_division(
                    total_number_of_unique_adjectives_,
                    math.sqrt(2*total_number_of_adjectives_)
                )
            return SE.corrected_adjectives_variation_
    
    def simple_adpositions_variation(
        SE: object,
        ) -> float:
        try:
            return SE.simple_adpositions_variation_
        except AttributeError:
            total_number_of_unique_adpositions_ = \
                FoundationCollector.total_number_of_unique_adpositions(SE)
            total_number_of_adpositions_ = \
                FoundationCollector.total_number_of_adpositions(SE)
            SE.simple_adpositions_variation_ = \
                safe_division(
                    total_number_of_unique_adpositions_,
                    total_number_of_adpositions_
                )
            return SE.simple_adpositions_variation_
    
    def root_adpositions_variation(
        SE: object,
        ) -> float:
        try:
            return SE.root_adpositions_variation_
        except AttributeError:
            total_number_of_unique_adpositions_ = \
                FoundationCollector.total_number_of_unique_adpositions(SE)
            total_number_of_adpositions_ = \
                FoundationCollector.total_number_of_adpositions(SE)
            SE.root_adpositions_variation_ = \
                safe_division(
                    total_number_of_unique_adpositions_,
                    math.sqrt(total_number_of_adpositions_)
                )
            return SE.root_adpositions_variation_
        
    def corrected_adpositions_variation(
        SE: object,
        ) -> float:
        try:
            return SE.corrected_adpositions_variation_
        except AttributeError:
            total_number_of_unique_adpositions_ = \
                FoundationCollector.total_number_of_unique_adpositions(SE)
            total_number_of_adpositions_ = \
                FoundationCollector.total_number_of_adpositions(SE)
            SE.corrected_adpositions_variation_ = \
                safe_division(
                    total_number_of_unique_adpositions_,
                    math.sqrt(2*total_number_of_adpositions_)
                )
            return SE.corrected_adpositions_variation_
    
    def simple_adverbs_variation(
        SE: object,
        ) -> float:
        try:
            return SE.simple_adverbs_variation_
        except AttributeError:
            total_number_of_unique_adverbs_ = \
                FoundationCollector.total_number_of_unique_adverbs(SE)
            total_number_of_adverbs_ = \
                FoundationCollector.total_number_of_adverbs(SE)
            SE.simple_adverbs_variation_ = \
                safe_division(
                    total_number_of_unique_adverbs_,
                    total_number_of_adverbs_
                )
            return SE.simple_adverbs_variation_
    
    def root_adverbs_variation(
        SE: object,
        ) -> float:
        try:
            return SE.root_adverbs_variation_
        except AttributeError:
            total_number_of_unique_adverbs_ = \
                FoundationCollector.total_number_of_unique_adverbs(SE)
            total_number_of_adverbs_ = \
                FoundationCollector.total_number_of_adverbs(SE)
            SE.root_adverbs_variation_ = \
                safe_division(
                    total_number_of_unique_adverbs_,
                    math.sqrt(total_number_of_adverbs_)
                )
            return SE.root_adverbs_variation_
        
    def corrected_adverbs_variation(
        SE: object,
        ) -> float:
        try:
            return SE.corrected_adverbs_variation_
        except AttributeError:
            total_number_of_unique_adverbs_ = \
                FoundationCollector.total_number_of_unique_adverbs(SE)
            total_number_of_adverbs_ = \
                FoundationCollector.total_number_of_adverbs(SE)
            SE.corrected_adverbs_variation_ = \
                safe_division(
                    total_number_of_unique_adverbs_,
                    math.sqrt(2*total_number_of_adverbs_)
                )
            return SE.corrected_adverbs_variation_
    
    def simple_auxiliaries_variation(
        SE: object,
        ) -> float:
        try:
            return SE.simple_auxiliaries_variation_
        except AttributeError:
            total_number_of_unique_auxiliaries_ = \
                FoundationCollector.total_number_of_unique_auxiliaries(SE)
            total_number_of_auxiliaries_ = \
                FoundationCollector.total_number_of_auxiliaries(SE)
            SE.simple_auxiliaries_variation_ = \
                safe_division(
                    total_number_of_unique_auxiliaries_,
                    total_number_of_auxiliaries_
                )
            return SE.simple_auxiliaries_variation_
    
    def root_auxiliaries_variation(
        SE: object,
        ) -> float:
        try:
            return SE.root_auxiliaries_variation_
        except AttributeError:
            total_number_of_unique_auxiliaries_ = \
                FoundationCollector.total_number_of_unique_auxiliaries(SE)
            total_number_of_auxiliaries_ = \
                FoundationCollector.total_number_of_auxiliaries(SE)
            SE.root_auxiliaries_variation_ = \
                safe_division(
                    total_number_of_unique_auxiliaries_,
                    math.sqrt(total_number_of_auxiliaries_)
                )
            return SE.root_auxiliaries_variation_
        
    def corrected_auxiliaries_variation(
        SE: object,
        ) -> float:
        try:
            return SE.corrected_auxiliaries_variation_
        except AttributeError:
            total_number_of_unique_auxiliaries_ = \
                FoundationCollector.total_number_of_unique_auxiliaries(SE)
            total_number_of_auxiliaries_ = \
                FoundationCollector.total_number_of_auxiliaries(SE)
            SE.corrected_auxiliaries_variation_ = \
                safe_division(
                    total_number_of_unique_auxiliaries_,
                    math.sqrt(2*total_number_of_auxiliaries_)
                )
            return SE.corrected_auxiliaries_variation_
        
    def simple_coordinating_conjunctions_variation(
        SE: object,
        ) -> float:
        try:
            return SE.simple_coordinating_conjunctions_variation_
        except AttributeError:
            total_number_of_unique_coordinating_conjunctions_ = \
                FoundationCollector.total_number_of_unique_coordinating_conjunctions(SE)
            total_number_of_coordinating_conjunctions_ = \
                FoundationCollector.total_number_of_coordinating_conjunctions(SE)
            SE.simple_coordinating_conjunctions_variation_ = \
                safe_division(
                    total_number_of_unique_coordinating_conjunctions_,
                    total_number_of_coordinating_conjunctions_
                )
            return SE.simple_coordinating_conjunctions_variation_
    
    def root_coordinating_conjunctions_variation(
        SE: object,
        ) -> float:
        try:
            return SE.root_coordinating_conjunctions_variation_
        except AttributeError:
            total_number_of_unique_coordinating_conjunctions_ = \
                FoundationCollector.total_number_of_unique_coordinating_conjunctions(SE)
            total_number_of_coordinating_conjunctions_ = \
                FoundationCollector.total_number_of_coordinating_conjunctions(SE)
            SE.root_coordinating_conjunctions_variation_ = \
                safe_division(
                    total_number_of_unique_coordinating_conjunctions_,
                    math.sqrt(total_number_of_coordinating_conjunctions_)
                )
            return SE.root_coordinating_conjunctions_variation_
        
    def corrected_coordinating_conjunctions_variation(
        SE: object,
        ) -> float:
        try:
            return SE.corrected_coordinating_conjunctions_variation_
        except AttributeError:
            total_number_of_unique_coordinating_conjunctions_ = \
                FoundationCollector.total_number_of_unique_coordinating_conjunctions(SE)
            total_number_of_coordinating_conjunctions_ = \
                FoundationCollector.total_number_of_coordinating_conjunctions(SE)
            SE.corrected_coordinating_conjunctions_variation_ = \
                safe_division(
                    total_number_of_unique_coordinating_conjunctions_,
                    math.sqrt(2*total_number_of_coordinating_conjunctions_)
                )
            return SE.corrected_coordinating_conjunctions_variation_
    
    def simple_determiners_variation(
        SE: object,
        ) -> float:
        try:
            return SE.simple_determiners_variation_
        except AttributeError:
            total_number_of_unique_determiners_ = \
                FoundationCollector.total_number_of_unique_determiners(SE)
            total_number_of_determiners_ = \
                FoundationCollector.total_number_of_determiners(SE)
            SE.simple_determiners_variation_ = \
                safe_division(
                    total_number_of_unique_determiners_,
                    total_number_of_determiners_
                )
            return SE.simple_determiners_variation_
    
    def root_determiners_variation(
        SE: object,
        ) -> float:
        try:
            return SE.root_determiners_variation_
        except AttributeError:
            total_number_of_unique_determiners_ = \
                FoundationCollector.total_number_of_unique_determiners(SE)
            total_number_of_determiners_ = \
                FoundationCollector.total_number_of_determiners(SE)
            SE.root_determiners_variation_ = \
                safe_division(
                    total_number_of_unique_determiners_,
                    math.sqrt(total_number_of_determiners_)
                )
            return SE.root_determiners_variation_
        
    def corrected_determiners_variation(
        SE: object,
        ) -> float:
        try:
            return SE.corrected_determiners_variation_
        except AttributeError:
            total_number_of_unique_determiners_ = \
                FoundationCollector.total_number_of_unique_determiners(SE)
            total_number_of_determiners_ = \
                FoundationCollector.total_number_of_determiners(SE)
            SE.corrected_determiners_variation_ = \
                safe_division(
                    total_number_of_unique_determiners_,
                    math.sqrt(2*total_number_of_determiners_)
                )
            return SE.corrected_determiners_variation_
    
    def simple_interjections_variation(
        SE: object,
        ) -> float:
        try:
            return SE.simple_interjections_variation_
        except AttributeError:
            total_number_of_unique_interjections_ = \
                FoundationCollector.total_number_of_unique_interjections(SE)
            total_number_of_interjections_ = \
                FoundationCollector.total_number_of_interjections(SE)
            SE.simple_interjections_variation_ = \
                safe_division(
                    total_number_of_unique_interjections_,
                    total_number_of_interjections_
                )
            return SE.simple_interjections_variation_
    
    def root_interjections_variation(
        SE: object,
        ) -> float:
        try:
            return SE.root_interjections_variation_
        except AttributeError:
            total_number_of_unique_interjections_ = \
                FoundationCollector.total_number_of_unique_interjections(SE)
            total_number_of_interjections_ = \
                FoundationCollector.total_number_of_interjections(SE)
            SE.root_interjections_variation_ = \
                safe_division(
                    total_number_of_unique_interjections_,
                    math.sqrt(total_number_of_interjections_)
                )
            return SE.root_interjections_variation_
        
    def corrected_interjections_variation(
        SE: object,
        ) -> float:
        try:
            return SE.corrected_interjections_variation_
        except AttributeError:
            total_number_of_unique_interjections_ = \
                FoundationCollector.total_number_of_unique_interjections(SE)
            total_number_of_interjections_ = \
                FoundationCollector.total_number_of_interjections(SE)
            SE.corrected_interjections_variation_ = \
                safe_division(
                    total_number_of_unique_interjections_,
                    math.sqrt(2*total_number_of_interjections_)
                )
            return SE.corrected_interjections_variation_
    
    def simple_nouns_variation(
        SE: object,
        ) -> float:
        try:
            return SE.simple_nouns_variation_
        except AttributeError:
            total_number_of_unique_nouns_ = \
                FoundationCollector.total_number_of_unique_nouns(SE)
            total_number_of_nouns_ = \
                FoundationCollector.total_number_of_nouns(SE)
            SE.simple_nouns_variation_ = \
                safe_division(
                    total_number_of_unique_nouns_,
                    total_number_of_nouns_
                )
            return SE.simple_nouns_variation_
    
    def root_nouns_variation(
        SE: object,
        ) -> float:
        try:
            return SE.root_nouns_variation_
        except AttributeError:
            total_number_of_unique_nouns_ = \
                FoundationCollector.total_number_of_unique_nouns(SE)
            total_number_of_nouns_ = \
                FoundationCollector.total_number_of_nouns(SE)
            SE.root_nouns_variation_ = \
                safe_division(
                    total_number_of_unique_nouns_,
                    math.sqrt(total_number_of_nouns_)
                )
            return SE.root_nouns_variation_
        
    def corrected_nouns_variation(
        SE: object,
        ) -> float:
        try:
            return SE.corrected_nouns_variation_
        except AttributeError:
            total_number_of_unique_nouns_ = \
                FoundationCollector.total_number_of_unique_nouns(SE)
            total_number_of_nouns_ = \
                FoundationCollector.total_number_of_nouns(SE)
            SE.corrected_nouns_variation_ = \
                safe_division(
                    total_number_of_unique_nouns_,
                    math.sqrt(2*total_number_of_nouns_)
                )
            return SE.corrected_nouns_variation_
    
    def simple_numerals_variation(
        SE: object,
        ) -> float:
        try:
            return SE.simple_numerals_variation_
        except AttributeError:
            total_number_of_unique_numerals_ = \
                FoundationCollector.total_number_of_unique_numerals(SE)
            total_number_of_numerals_ = \
                FoundationCollector.total_number_of_numerals(SE)
            SE.simple_numerals_variation_ = \
                safe_division(
                    total_number_of_unique_numerals_,
                    total_number_of_numerals_
                )
            return SE.simple_numerals_variation_
    
    def root_numerals_variation(
        SE: object,
        ) -> float:
        try:
            return SE.root_numerals_variation_
        except AttributeError:
            total_number_of_unique_numerals_ = \
                FoundationCollector.total_number_of_unique_numerals(SE)
            total_number_of_numerals_ = \
                FoundationCollector.total_number_of_numerals(SE)
            SE.root_numerals_variation_ = \
                safe_division(
                    total_number_of_unique_numerals_,
                    math.sqrt(total_number_of_numerals_)
                )
            return SE.root_numerals_variation_
        
    def corrected_numerals_variation(
        SE: object,
        ) -> float:
        try:
            return SE.corrected_numerals_variation_
        except AttributeError:
            total_number_of_unique_numerals_ = \
                FoundationCollector.total_number_of_unique_numerals(SE)
            total_number_of_numerals_ = \
                FoundationCollector.total_number_of_numerals(SE)
            SE.corrected_numerals_variation_ = \
                safe_division(
                    total_number_of_unique_numerals_,
                    math.sqrt(2*total_number_of_numerals_)
                )
            return SE.corrected_numerals_variation_
    
    def simple_particles_variation(
        SE: object,
        ) -> float:
        try:
            return SE.simple_particles_variation_
        except AttributeError:
            total_number_of_unique_particles_ = \
                FoundationCollector.total_number_of_unique_particles(SE)
            total_number_of_particles_ = \
                FoundationCollector.total_number_of_particles(SE)
            SE.simple_particles_variation_ = \
                safe_division(
                    total_number_of_unique_particles_,
                    total_number_of_particles_
                )
            return SE.simple_particles_variation_
    
    def root_particles_variation(
        SE: object,
        ) -> float:
        try:
            return SE.root_particles_variation_
        except AttributeError:
            total_number_of_unique_particles_ = \
                FoundationCollector.total_number_of_unique_particles(SE)
            total_number_of_particles_ = \
                FoundationCollector.total_number_of_particles(SE)
            SE.root_particles_variation_ = \
                safe_division(
                    total_number_of_unique_particles_,
                    math.sqrt(total_number_of_particles_)
                )
            return SE.root_particles_variation_
        
    def corrected_particles_variation(
        SE: object,
        ) -> float:
        try:
            return SE.corrected_particles_variation_
        except AttributeError:
            total_number_of_unique_particles_ = \
                FoundationCollector.total_number_of_unique_particles(SE)
            total_number_of_particles_ = \
                FoundationCollector.total_number_of_particles(SE)
            SE.corrected_particles_variation_ = \
                safe_division(
                    total_number_of_unique_particles_,
                    math.sqrt(2*total_number_of_particles_)
                )
            return SE.corrected_particles_variation_
    
    def simple_pronouns_variation(
        SE: object,
        ) -> float:
        try:
            return SE.simple_pronouns_variation_
        except AttributeError:
            total_number_of_unique_pronouns_ = \
                FoundationCollector.total_number_of_unique_pronouns(SE)
            total_number_of_pronouns_ = \
                FoundationCollector.total_number_of_pronouns(SE)
            SE.simple_pronouns_variation_ = \
                safe_division(
                    total_number_of_unique_pronouns_,
                    total_number_of_pronouns_
                )
            return SE.simple_pronouns_variation_
    
    def root_pronouns_variation(
        SE: object,
        ) -> float:
        try:
            return SE.root_pronouns_variation_
        except AttributeError:
            total_number_of_unique_pronouns_ = \
                FoundationCollector.total_number_of_unique_pronouns(SE)
            total_number_of_pronouns_ = \
                FoundationCollector.total_number_of_pronouns(SE)
            SE.root_pronouns_variation_ = \
                safe_division(
                    total_number_of_unique_pronouns_,
                    math.sqrt(total_number_of_pronouns_)
                )
            return SE.root_pronouns_variation_
        
    def corrected_pronouns_variation(
        SE: object,
        ) -> float:
        try:
            return SE.corrected_pronouns_variation_
        except AttributeError:
            total_number_of_unique_pronouns_ = \
                FoundationCollector.total_number_of_unique_pronouns(SE)
            total_number_of_pronouns_ = \
                FoundationCollector.total_number_of_pronouns(SE)
            SE.corrected_pronouns_variation_ = \
                safe_division(
                    total_number_of_unique_pronouns_,
                    math.sqrt(2*total_number_of_pronouns_)
                )
            return SE.corrected_pronouns_variation_
    
    def simple_proper_nouns_variation(
        SE: object,
        ) -> float:
        try:
            return SE.simple_proper_nouns_variation_
        except AttributeError:
            total_number_of_unique_proper_nouns_ = \
                FoundationCollector.total_number_of_unique_proper_nouns(SE)
            total_number_of_proper_nouns_ = \
                FoundationCollector.total_number_of_proper_nouns(SE)
            SE.simple_proper_nouns_variation_ = \
                safe_division(
                    total_number_of_unique_proper_nouns_,
                    total_number_of_proper_nouns_
                )
            return SE.simple_proper_nouns_variation_
    
    def root_proper_nouns_variation(
        SE: object,
        ) -> float:
        try:
            return SE.root_proper_nouns_variation_
        except AttributeError:
            total_number_of_unique_proper_nouns_ = \
                FoundationCollector.total_number_of_unique_proper_nouns(SE)
            total_number_of_proper_nouns_ = \
                FoundationCollector.total_number_of_proper_nouns(SE)
            SE.root_proper_nouns_variation_ = \
                safe_division(
                    total_number_of_unique_proper_nouns_,
                    math.sqrt(total_number_of_proper_nouns_)
                )
            return SE.root_proper_nouns_variation_
        
    def corrected_proper_nouns_variation(
        SE: object,
        ) -> float:
        try:
            return SE.corrected_proper_nouns_variation_
        except AttributeError:
            total_number_of_unique_proper_nouns_ = \
                FoundationCollector.total_number_of_unique_proper_nouns(SE)
            total_number_of_proper_nouns_ = \
                FoundationCollector.total_number_of_proper_nouns(SE)
            SE.corrected_proper_nouns_variation_ = \
                safe_division(
                    total_number_of_unique_proper_nouns_,
                    math.sqrt(2*total_number_of_proper_nouns_)
                )
            return SE.corrected_proper_nouns_variation_
    
    def simple_punctuations_variation(
        SE: object,
        ) -> float:
        try:
            return SE.simple_punctuations_variation_
        except AttributeError:
            total_number_of_unique_punctuations_ = \
                FoundationCollector.total_number_of_unique_punctuations(SE)
            total_number_of_punctuations_ = \
                FoundationCollector.total_number_of_punctuations(SE)
            SE.simple_punctuations_variation_ = \
                safe_division(
                    total_number_of_unique_punctuations_,
                    total_number_of_punctuations_
                )
            return SE.simple_punctuations_variation_
    
    def root_punctuations_variation(
        SE: object,
        ) -> float:
        try:
            return SE.root_punctuations_variation_
        except AttributeError:
            total_number_of_unique_punctuations_ = \
                FoundationCollector.total_number_of_unique_punctuations(SE)
            total_number_of_punctuations_ = \
                FoundationCollector.total_number_of_punctuations(SE)
            SE.root_punctuations_variation_ = \
                safe_division(
                    total_number_of_unique_punctuations_,
                    math.sqrt(total_number_of_punctuations_)
                )
            return SE.root_punctuations_variation_
        
    def corrected_punctuations_variation(
        SE: object,
        ) -> float:
        try:
            return SE.corrected_punctuations_variation_
        except AttributeError:
            total_number_of_unique_punctuations_ = \
                FoundationCollector.total_number_of_unique_punctuations(SE)
            total_number_of_punctuations_ = \
                FoundationCollector.total_number_of_punctuations(SE)
            SE.corrected_punctuations_variation_ = \
                safe_division(
                    total_number_of_unique_punctuations_,
                    math.sqrt(2*total_number_of_punctuations_)
                )
            return SE.corrected_punctuations_variation_
    
    def simple_subordinating_conjunctions_variation(
        SE: object,
        ) -> float:
        try:
            return SE.simple_subordinating_conjunctions_variation_
        except AttributeError:
            total_number_of_unique_subordinating_conjunctions_ = \
                FoundationCollector.total_number_of_unique_subordinating_conjunctions(SE)
            total_number_of_subordinating_conjunctions_ = \
                FoundationCollector.total_number_of_subordinating_conjunctions(SE)
            SE.simple_subordinating_conjunctions_variation_ = \
                safe_division(
                    total_number_of_unique_subordinating_conjunctions_,
                    total_number_of_subordinating_conjunctions_
                )
            return SE.simple_subordinating_conjunctions_variation_
    
    def root_subordinating_conjunctions_variation(
        SE: object,
        ) -> float:
        try:
            return SE.root_subordinating_conjunctions_variation_
        except AttributeError:
            total_number_of_unique_subordinating_conjunctions_ = \
                FoundationCollector.total_number_of_unique_subordinating_conjunctions(SE)
            total_number_of_subordinating_conjunctions_ = \
                FoundationCollector.total_number_of_subordinating_conjunctions(SE)
            SE.root_subordinating_conjunctions_variation_ = \
                safe_division(
                    total_number_of_unique_subordinating_conjunctions_,
                    math.sqrt(total_number_of_subordinating_conjunctions_)
                )
            return SE.root_subordinating_conjunctions_variation_
        
    def corrected_subordinating_conjunctions_variation(
        SE: object,
        ) -> float:
        try:
            return SE.corrected_subordinating_conjunctions_variation_
        except AttributeError:
            total_number_of_unique_subordinating_conjunctions_ = \
                FoundationCollector.total_number_of_unique_subordinating_conjunctions(SE)
            total_number_of_subordinating_conjunctions_ = \
                FoundationCollector.total_number_of_subordinating_conjunctions(SE)
            SE.corrected_subordinating_conjunctions_variation_ = \
                safe_division(
                    total_number_of_unique_subordinating_conjunctions_,
                    math.sqrt(2*total_number_of_subordinating_conjunctions_)
                )
            return SE.corrected_subordinating_conjunctions_variation_
    
    def simple_symbols_variation(
        SE: object,
        ) -> float:
        try:
            return SE.simple_symbols_variation_
        except AttributeError:
            total_number_of_unique_symbols_ = \
                FoundationCollector.total_number_of_unique_symbols(SE)
            total_number_of_symbols_ = \
                FoundationCollector.total_number_of_symbols(SE)
            SE.simple_symbols_variation_ = \
                safe_division(
                    total_number_of_unique_symbols_,
                    total_number_of_symbols_
                )
            return SE.simple_symbols_variation_
    
    def root_symbols_variation(
        SE: object,
        ) -> float:
        try:
            return SE.root_symbols_variation_
        except AttributeError:
            total_number_of_unique_symbols_ = \
                FoundationCollector.total_number_of_unique_symbols(SE)
            total_number_of_symbols_ = \
                FoundationCollector.total_number_of_symbols(SE)
            SE.root_symbols_variation_ = \
                safe_division(
                    total_number_of_unique_symbols_,
                    math.sqrt(total_number_of_symbols_)
                )
            return SE.root_symbols_variation_
        
    def corrected_symbols_variation(
        SE: object,
        ) -> float:
        try:
            return SE.corrected_symbols_variation_
        except AttributeError:
            total_number_of_unique_symbols_ = \
                FoundationCollector.total_number_of_unique_symbols(SE)
            total_number_of_symbols_ = \
                FoundationCollector.total_number_of_symbols(SE)
            SE.corrected_symbols_variation_ = \
                safe_division(
                    total_number_of_unique_symbols_,
                    math.sqrt(2*total_number_of_symbols_)
                )
            return SE.corrected_symbols_variation_
    
    def simple_verbs_variation(
        SE: object,
        ) -> float:
        try:
            return SE.simple_verbs_variation_
        except AttributeError:
            total_number_of_unique_verbs_ = \
                FoundationCollector.total_number_of_unique_verbs(SE)
            total_number_of_verbs_ = \
                FoundationCollector.total_number_of_verbs(SE)
            SE.simple_verbs_variation_ = \
                safe_division(
                    total_number_of_unique_verbs_,
                    total_number_of_verbs_
                )
            return SE.simple_verbs_variation_
    
    def root_verbs_variation(
        SE: object,
        ) -> float:
        try:
            return SE.root_verbs_variation_
        except AttributeError:
            total_number_of_unique_verbs_ = \
                FoundationCollector.total_number_of_unique_verbs(SE)
            total_number_of_verbs_ = \
                FoundationCollector.total_number_of_verbs(SE)
            SE.root_verbs_variation_ = \
                safe_division(
                    total_number_of_unique_verbs_,
                    math.sqrt(total_number_of_verbs_)
                )
            return SE.root_verbs_variation_
        
    def corrected_verbs_variation(
        SE: object,
        ) -> float:
        try:
            return SE.corrected_verbs_variation_
        except AttributeError:
            total_number_of_unique_verbs_ = \
                FoundationCollector.total_number_of_unique_verbs(SE)
            total_number_of_verbs_ = \
                FoundationCollector.total_number_of_verbs(SE)
            SE.corrected_verbs_variation_ = \
                safe_division(
                    total_number_of_unique_verbs_,
                    math.sqrt(2*total_number_of_verbs_)
                )
            return SE.corrected_verbs_variation_
        
    def simple_spaces_variation(
        SE: object,
        ) -> float:
        try:
            return SE.simple_spaces_variation_
        except AttributeError:
            total_number_of_unique_spaces_ = \
                FoundationCollector.total_number_of_unique_spaces(SE)
            total_number_of_spaces_ = \
                FoundationCollector.total_number_of_spaces(SE)
            SE.simple_spaces_variation_ = \
                safe_division(
                    total_number_of_unique_spaces_,
                    total_number_of_spaces_
                )
            return SE.simple_spaces_variation_
    
    def root_spaces_variation(
        SE: object,
        ) -> float:
        try:
            return SE.root_spaces_variation_
        except AttributeError:
            total_number_of_unique_spaces_ = \
                FoundationCollector.total_number_of_unique_spaces(SE)
            total_number_of_spaces_ = \
                FoundationCollector.total_number_of_spaces(SE)
            SE.root_spaces_variation_ = \
                safe_division(
                    total_number_of_unique_spaces_,
                    math.sqrt(total_number_of_spaces_)
                )
            return SE.root_spaces_variation_
        
    def corrected_spaces_variation(
        SE: object,
        ) -> float:
        try:
            return SE.corrected_spaces_variation_
        except AttributeError:
            total_number_of_unique_spaces_ = \
                FoundationCollector.total_number_of_unique_spaces(SE)
            total_number_of_spaces_ = \
                FoundationCollector.total_number_of_spaces(SE)
            SE.corrected_spaces_variation_ = \
                safe_division(
                    total_number_of_unique_spaces_,
                    math.sqrt(2*total_number_of_spaces_)
                )
            return SE.corrected_spaces_variation_