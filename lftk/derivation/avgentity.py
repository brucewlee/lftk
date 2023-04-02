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
    
    def average_number_of_named_entities_person_per_word(
        SE: object
        ) -> float:
        """
        returns the number of named entities that are PERSON (People, including fictional)
        """
        try:
            return SE.average_number_of_named_entities_person_per_word_ 
        except AttributeError:
            total_number_of_words_ = \
                FoundationCollector.total_number_of_words(SE)
            total_number_of_named_entities_person_ = \
                FoundationCollector.total_number_of_named_entities_person(SE)
            SE.average_number_of_named_entities_person_per_word_ = \
                safe_division(
                    total_number_of_named_entities_person_,
                    total_number_of_words_
                )
            return SE.average_number_of_named_entities_person_per_word_
        
    def average_number_of_named_entities_norp_per_word(
        SE: object
        ) -> float:
        """
        returns the number of named entities that are NORP (Nationalities or religious or political groups)
        """
        try:
            return SE.average_number_of_named_entities_norp_per_word_ 
        except AttributeError:
            total_number_of_words_ = \
                FoundationCollector.total_number_of_words(SE)
            total_number_of_named_entities_norp_ = \
                FoundationCollector.total_number_of_named_entities_norp(SE)
            SE.average_number_of_named_entities_norp_per_word_ = \
                safe_division(
                    total_number_of_named_entities_norp_,
                    total_number_of_words_
                )
            return SE.average_number_of_named_entities_norp_per_word_

    def average_number_of_named_entities_fac_per_word(
        SE: object
        ) -> float:
        """
        returns the number of named entities that are FAC (Buildings, airports, highways, bridges, etc.)
        """
        try:
            return SE.average_number_of_named_entities_fac_per_word_ 
        except AttributeError:
            total_number_of_words_ = \
                FoundationCollector.total_number_of_words(SE)
            total_number_of_named_entities_fac_ = \
                FoundationCollector.total_number_of_named_entities_fac(SE)
            SE.average_number_of_named_entities_fac_per_word_ = \
                safe_division(
                    total_number_of_named_entities_fac_,
                    total_number_of_words_
                )
            return SE.average_number_of_named_entities_fac_per_word_

    def average_number_of_named_entities_org_per_word(
        SE: object
        ) -> float:
        """
        returns the number of named entities that are ORG (Companies, agencies, institutions, etc.)
        """
        try:
            return SE.average_number_of_named_entities_org_per_word_ 
        except AttributeError:
            total_number_of_words_ = \
                FoundationCollector.total_number_of_words(SE)
            total_number_of_named_entities_org_ = \
                FoundationCollector.total_number_of_named_entities_org(SE)
            SE.average_number_of_named_entities_org_per_word_ = \
                safe_division(
                    total_number_of_named_entities_org_,
                    total_number_of_words_
                )
            return SE.average_number_of_named_entities_org_per_word_
    
    def average_number_of_named_entities_gpe_per_word(
        SE: object
        ) -> float:
        """
        returns the number of named entities that are GPE (Countries, cities, states.)
        """
        try:
            return SE.average_number_of_named_entities_gpe_per_word_ 
        except AttributeError:
            total_number_of_words_ = \
                FoundationCollector.total_number_of_words(SE)
            total_number_of_named_entities_gpe_ = \
                FoundationCollector.total_number_of_named_entities_gpe(SE)
            SE.average_number_of_named_entities_gpe_per_word_ = \
                safe_division(
                    total_number_of_named_entities_gpe_,
                    total_number_of_words_
                )
            return SE.average_number_of_named_entities_gpe_per_word_
    
    def average_number_of_named_entities_loc_per_word(
        SE: object
        ) -> float:
        """
        returns the number of named entities that are LOC (Non-GPE locations, mountain ranges, bodies of water.)
        """
        try:
            return SE.average_number_of_named_entities_loc_per_word_ 
        except AttributeError:
            total_number_of_words_ = \
                FoundationCollector.total_number_of_words(SE)
            total_number_of_named_entities_loc_ = \
                FoundationCollector.total_number_of_named_entities_loc(SE)
            SE.average_number_of_named_entities_loc_per_word_ = \
                safe_division(
                    total_number_of_named_entities_loc_,
                    total_number_of_words_
                )
            return SE.average_number_of_named_entities_loc_per_word_
    
    def average_number_of_named_entities_product_per_word(
        SE: object
        ) -> float:
        """
        returns the number of named entities that are PRODUCT (Objects, vehicles, foods, etc. (Not services.)
        """
        try:
            return SE.average_number_of_named_entities_product_per_word_ 
        except AttributeError:
            total_number_of_words_ = \
                FoundationCollector.total_number_of_words(SE)
            total_number_of_named_entities_product_ = \
                FoundationCollector.total_number_of_named_entities_product(SE)
            SE.average_number_of_named_entities_product_per_word_ = \
                safe_division(
                    total_number_of_named_entities_product_,
                    total_number_of_words_
                )
            return SE.average_number_of_named_entities_product_per_word_
    
    def average_number_of_named_entities_event_per_word(
        SE: object
        ) -> float:
        """
        returns the number of named entities that are EVENT (Named hurricanes, battles, wars, sports events, etc.)
        """
        try:
            return SE.average_number_of_named_entities_event_per_word_ 
        except AttributeError:
            total_number_of_words_ = \
                FoundationCollector.total_number_of_words(SE)
            total_number_of_named_entities_event_ = \
                FoundationCollector.total_number_of_named_entities_event(SE)
            SE.average_number_of_named_entities_event_per_word_ = \
                safe_division(
                    total_number_of_named_entities_event_,
                    total_number_of_words_
                )
            return SE.average_number_of_named_entities_event_per_word_
    
    def average_number_of_named_entities_art_per_word(
        SE: object
        ) -> float:
        """
        returns the number of named entities that are WORK_OF_ART (Titles of books, songs, etc.)
        """
        try:
            return SE.average_number_of_named_entities_art_per_word_ 
        except AttributeError:
            total_number_of_words_ = \
                FoundationCollector.total_number_of_words(SE)
            total_number_of_named_entities_art_ = \
                FoundationCollector.total_number_of_named_entities_art(SE)
            SE.average_number_of_named_entities_art_per_word_ = \
                safe_division(
                    total_number_of_named_entities_art_,
                    total_number_of_words_
                )
            return SE.average_number_of_named_entities_art_per_word_
    
    def average_number_of_named_entities_law_per_word(
        SE: object
        ) -> float:
        """
        returns the number of named entities that are LAW (Named documents made into laws.)
        """
        try:
            return SE.average_number_of_named_entities_law_per_word_ 
        except AttributeError:
            total_number_of_words_ = \
                FoundationCollector.total_number_of_words(SE)
            total_number_of_named_entities_law_ = \
                FoundationCollector.total_number_of_named_entities_law(SE)
            SE.average_number_of_named_entities_law_per_word_ = \
                safe_division(
                    total_number_of_named_entities_law_,
                    total_number_of_words_
                )
            return SE.average_number_of_named_entities_law_per_word_
    
    def average_number_of_named_entities_language_per_word(
        SE: object
        ) -> float:
        """
        returns the number of named entities that are LANGUAGE (Any named language.)
        """
        try:
            return SE.average_number_of_named_entities_language_per_word_ 
        except AttributeError:
            total_number_of_words_ = \
                FoundationCollector.total_number_of_words(SE)
            total_number_of_named_entities_language_ = \
                FoundationCollector.total_number_of_named_entities_language(SE)
            SE.average_number_of_named_entities_language_per_word_ = \
                safe_division(
                    total_number_of_named_entities_language_,
                    total_number_of_words_
                )
            return SE.average_number_of_named_entities_language_per_word_
    
    def average_number_of_named_entities_date_per_word(
        SE: object
        ) -> float:
        """
        returns the number of named entities that are DATE (Absolute or relative dates or periods.)
        """
        try:
            return SE.average_number_of_named_entities_date_per_word_ 
        except AttributeError:
            total_number_of_words_ = \
                FoundationCollector.total_number_of_words(SE)
            total_number_of_named_entities_date_ = \
                FoundationCollector.total_number_of_named_entities_date(SE)
            SE.average_number_of_named_entities_date_per_word_ = \
                safe_division(
                    total_number_of_named_entities_date_,
                    total_number_of_words_
                )
            return SE.average_number_of_named_entities_date_per_word_
        
    def average_number_of_named_entities_time_per_word(
        SE: object
        ) -> float:
        """
        returns the number of named entities that are TIME (Times smaller than a day.)
        """
        try:
            return SE.average_number_of_named_entities_time_per_word_ 
        except AttributeError:
            total_number_of_words_ = \
                FoundationCollector.total_number_of_words(SE)
            total_number_of_named_entities_time_ = \
                FoundationCollector.total_number_of_named_entities_time(SE)
            SE.average_number_of_named_entities_time_per_word_ = \
                safe_division(
                    total_number_of_named_entities_time_,
                    total_number_of_words_
                )
            return SE.average_number_of_named_entities_time_per_word_
    
    def average_number_of_named_entities_percent_per_word(
        SE: object
        ) -> float:
        """
        returns the number of named entities that are PERCENT (Percentage, including ”%“.)
        """
        try:
            return SE.average_number_of_named_entities_percent_per_word_ 
        except AttributeError:
            total_number_of_words_ = \
                FoundationCollector.total_number_of_words(SE)
            total_number_of_named_entities_percent_ = \
                FoundationCollector.total_number_of_named_entities_percent(SE)
            SE.average_number_of_named_entities_percent_per_word_ = \
                safe_division(
                    total_number_of_named_entities_percent_,
                    total_number_of_words_
                )
            return SE.average_number_of_named_entities_percent_per_word_
    
    def average_number_of_named_entities_money_per_word(
        SE: object
        ) -> float:
        """
        returns the number of named entities that are MONEY (Monetary values, including unit.)
        """
        try:
            return SE.average_number_of_named_entities_money_per_word_ 
        except AttributeError:
            total_number_of_words_ = \
                FoundationCollector.total_number_of_words(SE)
            total_number_of_named_entities_money_ = \
                FoundationCollector.total_number_of_named_entities_money(SE)
            SE.average_number_of_named_entities_money_per_word_ = \
                safe_division(
                    total_number_of_named_entities_money_,
                    total_number_of_words_
                )
            return SE.average_number_of_named_entities_money_per_word_
    
    def average_number_of_named_entities_quantity_per_word(
        SE: object
        ) -> float:
        """
        returns the number of named entities that are QUANTITY (Measurements, as of weight or distance.)
        """
        try:
            return SE.average_number_of_named_entities_quantity_per_word_ 
        except AttributeError:
            total_number_of_words_ = \
                FoundationCollector.total_number_of_words(SE)
            total_number_of_named_entities_quantity_ = \
                FoundationCollector.total_number_of_named_entities_quantity(SE)
            SE.average_number_of_named_entities_quantity_per_word_ = \
                safe_division(
                    total_number_of_named_entities_quantity_,
                    total_number_of_words_
                )
            return SE.average_number_of_named_entities_quantity_per_word_
    
    def average_number_of_named_entities_ordinal_per_word(
        SE: object
        ) -> float:
        """
        returns the number of named entities that are ORDINAL (“first”, “second”, etc.)
        """
        try:
            return SE.average_number_of_named_entities_ordinal_per_word_ 
        except AttributeError:
            total_number_of_words_ = \
                FoundationCollector.total_number_of_words(SE)
            total_number_of_named_entities_ordinal_ = \
                FoundationCollector.total_number_of_named_entities_ordinal(SE)
            SE.average_number_of_named_entities_ordinal_per_word_ = \
                safe_division(
                    total_number_of_named_entities_ordinal_,
                    total_number_of_words_
                )
            return SE.average_number_of_named_entities_ordinal_per_word_
    
    def average_number_of_named_entities_cardinal_per_word(
        SE: object
        ) -> float:
        """
        returns the number of named entities that are CARDINAL (Numerals that do not fall under another type.)
        """
        try:
            return SE.average_number_of_named_entities_cardinal_per_word_ 
        except AttributeError:
            total_number_of_words_ = \
                FoundationCollector.total_number_of_words(SE)
            total_number_of_named_entities_cardinal_ = \
                FoundationCollector.total_number_of_named_entities_cardinal(SE)
            SE.average_number_of_named_entities_cardinal_per_word_ = \
                safe_division(
                    total_number_of_named_entities_cardinal_,
                    total_number_of_words_
                )
            return SE.average_number_of_named_entities_cardinal_per_word_
        
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
    
    def average_number_of_named_entities_person_per_sentence(
        SE: object
        ) -> float:
        """
        returns the number of named entities that are PERSON (People, including fictional)
        """
        try:
            return SE.average_number_of_named_entities_person_per_sentence_ 
        except AttributeError:
            total_number_of_sentences_ = \
                FoundationCollector.total_number_of_sentences(SE)
            total_number_of_named_entities_person_ = \
                FoundationCollector.total_number_of_named_entities_person(SE)
            SE.average_number_of_named_entities_person_per_sentence_ = \
                safe_division(
                    total_number_of_named_entities_person_,
                    total_number_of_sentences_
                )
            return SE.average_number_of_named_entities_person_per_sentence_
        
    def average_number_of_named_entities_norp_per_sentence(
        SE: object
        ) -> float:
        """
        returns the number of named entities that are NORP (Nationalities or religious or political groups)
        """
        try:
            return SE.average_number_of_named_entities_norp_per_sentence_ 
        except AttributeError:
            total_number_of_sentences_ = \
                FoundationCollector.total_number_of_sentences(SE)
            total_number_of_named_entities_norp_ = \
                FoundationCollector.total_number_of_named_entities_norp(SE)
            SE.average_number_of_named_entities_norp_per_sentence_ = \
                safe_division(
                    total_number_of_named_entities_norp_,
                    total_number_of_sentences_
                )
            return SE.average_number_of_named_entities_norp_per_sentence_

    def average_number_of_named_entities_fac_per_sentence(
        SE: object
        ) -> float:
        """
        returns the number of named entities that are FAC (Buildings, airports, highways, bridges, etc.)
        """
        try:
            return SE.average_number_of_named_entities_fac_per_sentence_ 
        except AttributeError:
            total_number_of_sentences_ = \
                FoundationCollector.total_number_of_sentences(SE)
            total_number_of_named_entities_fac_ = \
                FoundationCollector.total_number_of_named_entities_fac(SE)
            SE.average_number_of_named_entities_fac_per_sentence_ = \
                safe_division(
                    total_number_of_named_entities_fac_,
                    total_number_of_sentences_
                )
            return SE.average_number_of_named_entities_fac_per_sentence_

    def average_number_of_named_entities_org_per_sentence(
        SE: object
        ) -> float:
        """
        returns the number of named entities that are ORG (Companies, agencies, institutions, etc.)
        """
        try:
            return SE.average_number_of_named_entities_org_per_sentence_ 
        except AttributeError:
            total_number_of_sentences_ = \
                FoundationCollector.total_number_of_sentences(SE)
            total_number_of_named_entities_org_ = \
                FoundationCollector.total_number_of_named_entities_org(SE)
            SE.average_number_of_named_entities_org_per_sentence_ = \
                safe_division(
                    total_number_of_named_entities_org_,
                    total_number_of_sentences_
                )
            return SE.average_number_of_named_entities_org_per_sentence_
    
    def average_number_of_named_entities_gpe_per_sentence(
        SE: object
        ) -> float:
        """
        returns the number of named entities that are GPE (Countries, cities, states.)
        """
        try:
            return SE.average_number_of_named_entities_gpe_per_sentence_ 
        except AttributeError:
            total_number_of_sentences_ = \
                FoundationCollector.total_number_of_sentences(SE)
            total_number_of_named_entities_gpe_ = \
                FoundationCollector.total_number_of_named_entities_gpe(SE)
            SE.average_number_of_named_entities_gpe_per_sentence_ = \
                safe_division(
                    total_number_of_named_entities_gpe_,
                    total_number_of_sentences_
                )
            return SE.average_number_of_named_entities_gpe_per_sentence_
    
    def average_number_of_named_entities_loc_per_sentence(
        SE: object
        ) -> float:
        """
        returns the number of named entities that are LOC (Non-GPE locations, mountain ranges, bodies of water.)
        """
        try:
            return SE.average_number_of_named_entities_loc_per_sentence_ 
        except AttributeError:
            total_number_of_sentences_ = \
                FoundationCollector.total_number_of_sentences(SE)
            total_number_of_named_entities_loc_ = \
                FoundationCollector.total_number_of_named_entities_loc(SE)
            SE.average_number_of_named_entities_loc_per_sentence_ = \
                safe_division(
                    total_number_of_named_entities_loc_,
                    total_number_of_sentences_
                )
            return SE.average_number_of_named_entities_loc_per_sentence_
    
    def average_number_of_named_entities_product_per_sentence(
        SE: object
        ) -> float:
        """
        returns the number of named entities that are PRODUCT (Objects, vehicles, foods, etc. (Not services.)
        """
        try:
            return SE.average_number_of_named_entities_product_per_sentence_ 
        except AttributeError:
            total_number_of_sentences_ = \
                FoundationCollector.total_number_of_sentences(SE)
            total_number_of_named_entities_product_ = \
                FoundationCollector.total_number_of_named_entities_product(SE)
            SE.average_number_of_named_entities_product_per_sentence_ = \
                safe_division(
                    total_number_of_named_entities_product_,
                    total_number_of_sentences_
                )
            return SE.average_number_of_named_entities_product_per_sentence_
    
    def average_number_of_named_entities_event_per_sentence(
        SE: object
        ) -> float:
        """
        returns the number of named entities that are EVENT (Named hurricanes, battles, wars, sports events, etc.)
        """
        try:
            return SE.average_number_of_named_entities_event_per_sentence_ 
        except AttributeError:
            total_number_of_sentences_ = \
                FoundationCollector.total_number_of_sentences(SE)
            total_number_of_named_entities_event_ = \
                FoundationCollector.total_number_of_named_entities_event(SE)
            SE.average_number_of_named_entities_event_per_sentence_ = \
                safe_division(
                    total_number_of_named_entities_event_,
                    total_number_of_sentences_
                )
            return SE.average_number_of_named_entities_event_per_sentence_
    
    def average_number_of_named_entities_art_per_sentence(
        SE: object
        ) -> float:
        """
        returns the number of named entities that are WORK_OF_ART (Titles of books, songs, etc.)
        """
        try:
            return SE.average_number_of_named_entities_art_per_sentence_ 
        except AttributeError:
            total_number_of_sentences_ = \
                FoundationCollector.total_number_of_sentences(SE)
            total_number_of_named_entities_art_ = \
                FoundationCollector.total_number_of_named_entities_art(SE)
            SE.average_number_of_named_entities_art_per_sentence_ = \
                safe_division(
                    total_number_of_named_entities_art_,
                    total_number_of_sentences_
                )
            return SE.average_number_of_named_entities_art_per_sentence_
    
    def average_number_of_named_entities_law_per_sentence(
        SE: object
        ) -> float:
        """
        returns the number of named entities that are LAW (Named documents made into laws.)
        """
        try:
            return SE.average_number_of_named_entities_law_per_sentence_ 
        except AttributeError:
            total_number_of_sentences_ = \
                FoundationCollector.total_number_of_sentences(SE)
            total_number_of_named_entities_law_ = \
                FoundationCollector.total_number_of_named_entities_law(SE)
            SE.average_number_of_named_entities_law_per_sentence_ = \
                safe_division(
                    total_number_of_named_entities_law_,
                    total_number_of_sentences_
                )
            return SE.average_number_of_named_entities_law_per_sentence_
    
    def average_number_of_named_entities_language_per_sentence(
        SE: object
        ) -> float:
        """
        returns the number of named entities that are LANGUAGE (Any named language.)
        """
        try:
            return SE.average_number_of_named_entities_language_per_sentence_ 
        except AttributeError:
            total_number_of_sentences_ = \
                FoundationCollector.total_number_of_sentences(SE)
            total_number_of_named_entities_language_ = \
                FoundationCollector.total_number_of_named_entities_language(SE)
            SE.average_number_of_named_entities_language_per_sentence_ = \
                safe_division(
                    total_number_of_named_entities_language_,
                    total_number_of_sentences_
                )
            return SE.average_number_of_named_entities_language_per_sentence_
    
    def average_number_of_named_entities_date_per_sentence(
        SE: object
        ) -> float:
        """
        returns the number of named entities that are DATE (Absolute or relative dates or periods.)
        """
        try:
            return SE.average_number_of_named_entities_date_per_sentence_ 
        except AttributeError:
            total_number_of_sentences_ = \
                FoundationCollector.total_number_of_sentences(SE)
            total_number_of_named_entities_date_ = \
                FoundationCollector.total_number_of_named_entities_date(SE)
            SE.average_number_of_named_entities_date_per_sentence_ = \
                safe_division(
                    total_number_of_named_entities_date_,
                    total_number_of_sentences_
                )
            return SE.average_number_of_named_entities_date_per_sentence_
        
    def average_number_of_named_entities_time_per_sentence(
        SE: object
        ) -> float:
        """
        returns the number of named entities that are TIME (Times smaller than a day.)
        """
        try:
            return SE.average_number_of_named_entities_time_per_sentence_ 
        except AttributeError:
            total_number_of_sentences_ = \
                FoundationCollector.total_number_of_sentences(SE)
            total_number_of_named_entities_time_ = \
                FoundationCollector.total_number_of_named_entities_time(SE)
            SE.average_number_of_named_entities_time_per_sentence_ = \
                safe_division(
                    total_number_of_named_entities_time_,
                    total_number_of_sentences_
                )
            return SE.average_number_of_named_entities_time_per_sentence_
    
    def average_number_of_named_entities_percent_per_sentence(
        SE: object
        ) -> float:
        """
        returns the number of named entities that are PERCENT (Percentage, including ”%“.)
        """
        try:
            return SE.average_number_of_named_entities_percent_per_sentence_ 
        except AttributeError:
            total_number_of_sentences_ = \
                FoundationCollector.total_number_of_sentences(SE)
            total_number_of_named_entities_percent_ = \
                FoundationCollector.total_number_of_named_entities_percent(SE)
            SE.average_number_of_named_entities_percent_per_sentence_ = \
                safe_division(
                    total_number_of_named_entities_percent_,
                    total_number_of_sentences_
                )
            return SE.average_number_of_named_entities_percent_per_sentence_
    
    def average_number_of_named_entities_money_per_sentence(
        SE: object
        ) -> float:
        """
        returns the number of named entities that are MONEY (Monetary values, including unit.)
        """
        try:
            return SE.average_number_of_named_entities_money_per_sentence_ 
        except AttributeError:
            total_number_of_sentences_ = \
                FoundationCollector.total_number_of_sentences(SE)
            total_number_of_named_entities_money_ = \
                FoundationCollector.total_number_of_named_entities_money(SE)
            SE.average_number_of_named_entities_money_per_sentence_ = \
                safe_division(
                    total_number_of_named_entities_money_,
                    total_number_of_sentences_
                )
            return SE.average_number_of_named_entities_money_per_sentence_
    
    def average_number_of_named_entities_quantity_per_sentence(
        SE: object
        ) -> float:
        """
        returns the number of named entities that are QUANTITY (Measurements, as of weight or distance.)
        """
        try:
            return SE.average_number_of_named_entities_quantity_per_sentence_ 
        except AttributeError:
            total_number_of_sentences_ = \
                FoundationCollector.total_number_of_sentences(SE)
            total_number_of_named_entities_quantity_ = \
                FoundationCollector.total_number_of_named_entities_quantity(SE)
            SE.average_number_of_named_entities_quantity_per_sentence_ = \
                safe_division(
                    total_number_of_named_entities_quantity_,
                    total_number_of_sentences_
                )
            return SE.average_number_of_named_entities_quantity_per_sentence_
    
    def average_number_of_named_entities_ordinal_per_sentence(
        SE: object
        ) -> float:
        """
        returns the number of named entities that are ORDINAL (“first”, “second”, etc.)
        """
        try:
            return SE.average_number_of_named_entities_ordinal_per_sentence_ 
        except AttributeError:
            total_number_of_sentences_ = \
                FoundationCollector.total_number_of_sentences(SE)
            total_number_of_named_entities_ordinal_ = \
                FoundationCollector.total_number_of_named_entities_ordinal(SE)
            SE.average_number_of_named_entities_ordinal_per_sentence_ = \
                safe_division(
                    total_number_of_named_entities_ordinal_,
                    total_number_of_sentences_
                )
            return SE.average_number_of_named_entities_ordinal_per_sentence_
    
    def average_number_of_named_entities_cardinal_per_sentence(
        SE: object
        ) -> float:
        """
        returns the number of named entities that are CARDINAL (Numerals that do not fall under another type.)
        """
        try:
            return SE.average_number_of_named_entities_cardinal_per_sentence_ 
        except AttributeError:
            total_number_of_sentences_ = \
                FoundationCollector.total_number_of_sentences(SE)
            total_number_of_named_entities_cardinal_ = \
                FoundationCollector.total_number_of_named_entities_cardinal(SE)
            SE.average_number_of_named_entities_cardinal_per_sentence_ = \
                safe_division(
                    total_number_of_named_entities_cardinal_,
                    total_number_of_sentences_
                )
            return SE.average_number_of_named_entities_cardinal_per_sentence_