class Entity:

    def total_number_of_named_entities(
        SE: object
        ) -> int:
        try:
            return SE.total_number_of_named_entities_ 
        except AttributeError:
            doc_total = 0
            for ent in SE.doc.ents:
                doc_total += 1
            SE.total_number_of_named_entities_ = doc_total
            return SE.total_number_of_named_entities_
   
    def total_number_of_named_entities_person(
        SE: object
        ) -> int:
        """
        returns the number of named entities that are PERSON (People, including fictional)
        """
        try:
            return SE.total_number_of_named_entities_person_ 
        except AttributeError:
            doc_total = 0
            for ent in SE.doc.ents:
                if ent.label_ == "PERSON":
                    doc_total += 1
            SE.total_number_of_named_entities_person_ = doc_total
            return SE.total_number_of_named_entities_person_
        
    def total_number_of_named_entities_norp(
        SE: object
        ) -> int:
        """
        returns the number of named entities that are NORP (Nationalities or religious or political groups)
        """
        try:
            return SE.total_number_of_named_entities_norp_ 
        except AttributeError:
            doc_total = 0
            for ent in SE.doc.ents:
                if ent.label_ == "NORP":
                    doc_total += 1
            SE.total_number_of_named_entities_norp_ = doc_total
            return SE.total_number_of_named_entities_norp_

    def total_number_of_named_entities_fac(
        SE: object
        ) -> int:
        """
        returns the number of named entities that are FAC (Buildings, airports, highways, bridges, etc.)
        """
        try:
            return SE.total_number_of_named_entities_fac_ 
        except AttributeError:
            doc_total = 0
            for ent in SE.doc.ents:
                if ent.label_ == "FAC":
                    doc_total += 1
            SE.total_number_of_named_entities_fac_ = doc_total
            return SE.total_number_of_named_entities_fac_

    def total_number_of_named_entities_org(
        SE: object
        ) -> int:
        """
        returns the number of named entities that are ORG (Companies, agencies, institutions, etc.)
        """
        try:
            return SE.total_number_of_named_entities_org_ 
        except AttributeError:
            doc_total = 0
            for ent in SE.doc.ents:
                if ent.label_ == "ORG":
                    doc_total += 1
            SE.total_number_of_named_entities_org_ = doc_total
            return SE.total_number_of_named_entities_org_
    
    def total_number_of_named_entities_gpe(
        SE: object
        ) -> int:
        """
        returns the number of named entities that are GPE (Countries, cities, states.)
        """
        try:
            return SE.total_number_of_named_entities_gpe_ 
        except AttributeError:
            doc_total = 0
            for ent in SE.doc.ents:
                if ent.label_ == "GPE":
                    doc_total += 1
            SE.total_number_of_named_entities_gpe_ = doc_total
            return SE.total_number_of_named_entities_gpe_
    
    def total_number_of_named_entities_loc(
        SE: object
        ) -> int:
        """
        returns the number of named entities that are LOC (Non-GPE locations, mountain ranges, bodies of water.)
        """
        try:
            return SE.total_number_of_named_entities_loc_ 
        except AttributeError:
            doc_total = 0
            for ent in SE.doc.ents:
                if ent.label_ == "LOC":
                    doc_total += 1
            SE.total_number_of_named_entities_loc_ = doc_total
            return SE.total_number_of_named_entities_loc_
    
    def total_number_of_named_entities_product(
        SE: object
        ) -> int:
        """
        returns the number of named entities that are PRODUCT (Objects, vehicles, foods, etc. (Not services.)
        """
        try:
            return SE.total_number_of_named_entities_product_ 
        except AttributeError:
            doc_total = 0
            for ent in SE.doc.ents:
                if ent.label_ == "PRODUCT":
                    doc_total += 1
            SE.total_number_of_named_entities_product_ = doc_total
            return SE.total_number_of_named_entities_product_
    
    def total_number_of_named_entities_event(
        SE: object
        ) -> int:
        """
        returns the number of named entities that are EVENT (Named hurricanes, battles, wars, sports events, etc.)
        """
        try:
            return SE.total_number_of_named_entities_event_ 
        except AttributeError:
            doc_total = 0
            for ent in SE.doc.ents:
                if ent.label_ == "EVENT":
                    doc_total += 1
            SE.total_number_of_named_entities_event_ = doc_total
            return SE.total_number_of_named_entities_event_
    
    def total_number_of_named_entities_art(
        SE: object
        ) -> int:
        """
        returns the number of named entities that are WORK_OF_ART (Titles of books, songs, etc.)
        """
        try:
            return SE.total_number_of_named_entities_art_ 
        except AttributeError:
            doc_total = 0
            for ent in SE.doc.ents:
                if ent.label_ == "WORK_OF_ART":
                    doc_total += 1
            SE.total_number_of_named_entities_art_ = doc_total
            return SE.total_number_of_named_entities_art_
    
    def total_number_of_named_entities_law(
        SE: object
        ) -> int:
        """
        returns the number of named entities that are LAW (Named documents made into laws.)
        """
        try:
            return SE.total_number_of_named_entities_law_ 
        except AttributeError:
            doc_total = 0
            for ent in SE.doc.ents:
                if ent.label_ == "LAW":
                    doc_total += 1
            SE.total_number_of_named_entities_law_ = doc_total
            return SE.total_number_of_named_entities_law_
    
    def total_number_of_named_entities_language(
        SE: object
        ) -> int:
        """
        returns the number of named entities that are LANGUAGE (Any named language.)
        """
        try:
            return SE.total_number_of_named_entities_language_ 
        except AttributeError:
            doc_total = 0
            for ent in SE.doc.ents:
                if ent.label_ == "LANGUAGE":
                    doc_total += 1
            SE.total_number_of_named_entities_language_ = doc_total
            return SE.total_number_of_named_entities_language_
    
    def total_number_of_named_entities_date(
        SE: object
        ) -> int:
        """
        returns the number of named entities that are DATE (Absolute or relative dates or periods.)
        """
        try:
            return SE.total_number_of_named_entities_date_ 
        except AttributeError:
            doc_total = 0
            for ent in SE.doc.ents:
                if ent.label_ == "DATE":
                    doc_total += 1
            SE.total_number_of_named_entities_date_ = doc_total
            return SE.total_number_of_named_entities_date_
        
    def total_number_of_named_entities_time(
        SE: object
        ) -> int:
        """
        returns the number of named entities that are TIME (Times smaller than a day.)
        """
        try:
            return SE.total_number_of_named_entities_time_ 
        except AttributeError:
            doc_total = 0
            for ent in SE.doc.ents:
                if ent.label_ == "TIME":
                    doc_total += 1
            SE.total_number_of_named_entities_time_ = doc_total
            return SE.total_number_of_named_entities_time_
    
    def total_number_of_named_entities_percent(
        SE: object
        ) -> int:
        """
        returns the number of named entities that are PERCENT (Percentage, including ”%“.)
        """
        try:
            return SE.total_number_of_named_entities_percent_ 
        except AttributeError:
            doc_total = 0
            for ent in SE.doc.ents:
                if ent.label_ == "PERCENT":
                    doc_total += 1
            SE.total_number_of_named_entities_percent_ = doc_total
            return SE.total_number_of_named_entities_percent_
    
    def total_number_of_named_entities_money(
        SE: object
        ) -> int:
        """
        returns the number of named entities that are MONEY (Monetary values, including unit.)
        """
        try:
            return SE.total_number_of_named_entities_money_ 
        except AttributeError:
            doc_total = 0
            for ent in SE.doc.ents:
                if ent.label_ == "PERCENT":
                    doc_total += 1
            SE.total_number_of_named_entities_money_ = doc_total
            return SE.total_number_of_named_entities_money_
    
    def total_number_of_named_entities_quantity(
        SE: object
        ) -> int:
        """
        returns the number of named entities that are QUANTITY (Measurements, as of weight or distance.)
        """
        try:
            return SE.total_number_of_named_entities_quantity_ 
        except AttributeError:
            doc_total = 0
            for ent in SE.doc.ents:
                if ent.label_ == "QUANTITY":
                    doc_total += 1
            SE.total_number_of_named_entities_quantity_ = doc_total
            return SE.total_number_of_named_entities_quantity_
    
    def total_number_of_named_entities_ordinal(
        SE: object
        ) -> int:
        """
        returns the number of named entities that are ORDINAL (“first”, “second”, etc.)
        """
        try:
            return SE.total_number_of_named_entities_ordinal_ 
        except AttributeError:
            doc_total = 0
            for ent in SE.doc.ents:
                if ent.label_ == "ORDINAL":
                    doc_total += 1
            SE.total_number_of_named_entities_ordinal_ = doc_total
            return SE.total_number_of_named_entities_ordinal_
    
    def total_number_of_named_entities_cardinal(
        SE: object
        ) -> int:
        """
        returns the number of named entities that are CARDINAL (Numerals that do not fall under another type.)
        """
        try:
            return SE.total_number_of_named_entities_cardinal_ 
        except AttributeError:
            doc_total = 0
            for ent in SE.doc.ents:
                if ent.label_ == "CARDINAL":
                    doc_total += 1
            SE.total_number_of_named_entities_cardinal_ = doc_total
            return SE.total_number_of_named_entities_cardinal_