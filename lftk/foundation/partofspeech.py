class PartOfSpeech:
    def total_number_of_adjectives(
        SE: object
        ) -> float:
        try: 
            return SE.total_number_of_adjectives_
        except AttributeError:
            pos_list = [token.pos_ for token in SE.doc]
            SE.total_number_of_adjectives_ = pos_list.count("ADJ")
            return SE.total_number_of_adjectives_

    def total_number_of_unique_adjectives(
        SE: object
        ) -> float:
        try: 
            return SE.total_number_of_unique_adjectives_
        except AttributeError:
            pos_list = [token.lemma_ for token in SE.doc if token.pos_=="ADJ"]
            SE.total_number_of_unique_adjectives_ = len([*set(pos_list)])
            return SE.total_number_of_unique_adjectives_

    def total_number_of_adpositions(
        SE: object
        ) -> float:
        try: 
            return SE.total_number_of_adpositions_
        except AttributeError:
            pos_list = [token.pos_ for token in SE.doc]
            SE.total_number_of_adpositions_ = pos_list.count("ADP")
            return SE.total_number_of_adpositions_
        
    def total_number_of_unique_adpositions(
        SE: object
        ) -> float:
        try: 
            return SE.total_number_of_unique_adpositions_
        except AttributeError:
            pos_list = [token.lemma_ for token in SE.doc if token.pos_=="ADP"]
            SE.total_number_of_unique_adpositions_ = len([*set(pos_list)])
            return SE.total_number_of_unique_adpositions_

    def total_number_of_adverbs(
        SE: object
        ) -> float:
        try: 
            return SE.total_number_of_adverbs_
        except AttributeError:
            pos_list = [token.pos_ for token in SE.doc]
            SE.total_number_of_adverbs_ = pos_list.count("ADV")
            return SE.total_number_of_adverbs_
        
    def total_number_of_unique_adverbs(
        SE: object
        ) -> float:
        try: 
            return SE.total_number_of_unique_adverbs_
        except AttributeError:
            pos_list = [token.lemma_ for token in SE.doc if token.pos_=="ADV"]
            SE.total_number_of_unique_adverbs_ = len([*set(pos_list)])
            return SE.total_number_of_unique_adverbs_

    def total_number_of_auxiliaries(
        SE: object
        ) -> float:
        try: 
            return SE.total_number_of_auxiliaries_
        except AttributeError:
            pos_list = [token.pos_ for token in SE.doc]
            SE.total_number_of_auxiliaries_ = pos_list.count("AUX")
            return SE.total_number_of_auxiliaries_
        
    def total_number_of_unique_auxiliaries(
        SE: object
        ) -> float:
        try: 
            return SE.total_number_of_unique_auxiliaries_
        except AttributeError:
            pos_list = [token.lemma_ for token in SE.doc if token.pos_=="AUX"]
            SE.total_number_of_unique_auxiliaries_ = len([*set(pos_list)])
            return SE.total_number_of_unique_auxiliaries_

    def total_number_of_coordinating_conjunctions(
        SE: object
        ) -> float:
        try: 
            return SE.total_number_of_coordinating_conjunctions_
        except AttributeError:
            pos_list = [token.pos_ for token in SE.doc]
            SE.total_number_of_coordinating_conjunctions_ = pos_list.count("CCONJ")
            return SE.total_number_of_coordinating_conjunctions_

    def total_number_of_unique_coordinating_conjunctions(
        SE: object
        ) -> float:
        try: 
            return SE.total_number_of_unique_coordinating_conjunctions_
        except AttributeError:
            pos_list = [token.lemma_ for token in SE.doc if token.pos_=="CCONJ"]
            SE.total_number_of_unique_coordinating_conjunctions_ = len([*set(pos_list)])
            return SE.total_number_of_unique_coordinating_conjunctions_

    def total_number_of_determiners(
        SE: object
        ) -> float:
        try: 
            return SE.total_number_of_determiners_
        except AttributeError:
            pos_list = [token.pos_ for token in SE.doc]
            SE.total_number_of_determiners_ = pos_list.count("DET")
            return SE.total_number_of_determiners_

    def total_number_of_unique_determiners(
        SE: object
        ) -> float:
        try: 
            return SE.total_number_of_unique_determiners_
        except AttributeError:
            pos_list = [token.lemma_ for token in SE.doc if token.pos_=="DET"]
            SE.total_number_of_unique_determiners_ = len([*set(pos_list)])
            return SE.total_number_of_unique_determiners_

    def total_number_of_interjections(
        SE: object
        ) -> float:
        try: 
            return SE.total_number_of_interjections_
        except AttributeError:
            pos_list = [token.pos_ for token in SE.doc]
            SE.total_number_of_interjections_ = pos_list.count("INTJ")
            return SE.total_number_of_interjections_

    def total_number_of_unique_interjections(
        SE: object
        ) -> float:
        try: 
            return SE.total_number_of_unique_interjections_
        except AttributeError:
            pos_list = [token.lemma_ for token in SE.doc if token.pos_=="INTJ"]
            SE.total_number_of_unique_interjections_ = len([*set(pos_list)])
            return SE.total_number_of_unique_interjections_

    def total_number_of_nouns(
        SE: object
        ) -> float:
        try: 
            return SE.total_number_of_nouns_
        except AttributeError:
            pos_list = [token.pos_ for token in SE.doc]
            SE.total_number_of_nouns_ = pos_list.count("NOUN")
            return SE.total_number_of_nouns_

    def total_number_of_unique_nouns(
        SE: object
        ) -> float:
        try: 
            return SE.total_number_of_unique_nouns_
        except AttributeError:
            pos_list = [token.lemma_ for token in SE.doc if token.pos_=="NOUN"]
            SE.total_number_of_unique_nouns_ = len([*set(pos_list)])
            return SE.total_number_of_unique_nouns_

    def total_number_of_numerals(
        SE: object
        ) -> float:
        try: 
            return SE.total_number_of_numerals_
        except AttributeError:
            pos_list = [token.pos_ for token in SE.doc]
            SE.total_number_of_numerals_ = pos_list.count("NUM")
            return SE.total_number_of_numerals_

    def total_number_of_unique_numerals(
        SE: object
        ) -> float:
        try: 
            return SE.total_number_of_unique_numerals_
        except AttributeError:
            pos_list = [token.lemma_ for token in SE.doc if token.pos_=="NUM"]
            SE.total_number_of_unique_numerals_ = len([*set(pos_list)])
            return SE.total_number_of_unique_numerals_

    def total_number_of_particles(
        SE: object
        ) -> float:
        try: 
            return SE.total_number_of_particles_
        except AttributeError:
            pos_list = [token.pos_ for token in SE.doc]
            SE.total_number_of_particles_ = pos_list.count("PART")
            return SE.total_number_of_particles_

    def total_number_of_unique_particles(
        SE: object
        ) -> float:
        try: 
            return SE.total_number_of_unique_particles_
        except AttributeError:
            pos_list = [token.lemma_ for token in SE.doc if token.pos_=="PART"]
            SE.total_number_of_unique_particles_ = len([*set(pos_list)])
            return SE.total_number_of_unique_particles_

    def total_number_of_pronouns(
        SE: object
        ) -> float:
        try: 
            return SE.total_number_of_pronouns_
        except AttributeError:
            pos_list = [token.pos_ for token in SE.doc]
            SE.total_number_of_pronouns_ = pos_list.count("PRON")
            return SE.total_number_of_pronouns_

    def total_number_of_unique_pronouns(
        SE: object
        ) -> float:
        try: 
            return SE.total_number_of_unique_pronouns_
        except AttributeError:
            pos_list = [token.lemma_ for token in SE.doc if token.pos_=="PRON"]
            SE.total_number_of_unique_pronouns_ = len([*set(pos_list)])
            return SE.total_number_of_unique_pronouns_

    def total_number_of_proper_nouns(
        SE: object
        ) -> float:
        try: 
            return SE.total_number_of_proper_nouns_
        except AttributeError:
            pos_list = [token.pos_ for token in SE.doc]
            SE.total_number_of_proper_nouns_ = pos_list.count("PROPN")
            return SE.total_number_of_proper_nouns_

    def total_number_of_unique_proper_nouns(
        SE: object
        ) -> float:
        try: 
            return SE.total_number_of_unique_proper_nouns_
        except AttributeError:
            pos_list = [token.lemma_ for token in SE.doc if token.pos_=="PROPN"]
            SE.total_number_of_unique_proper_nouns_ = len([*set(pos_list)])
            return SE.total_number_of_unique_proper_nouns_

    def total_number_of_punctuations(
        SE: object
        ) -> float:
        try: 
            return SE.total_number_of_punctuations_
        except AttributeError:
            pos_list = [token.pos_ for token in SE.doc]
            SE.total_number_of_punctuations_ = pos_list.count("PUNCT")
            return SE.total_number_of_punctuations_

    def total_number_of_unique_punctuations(
        SE: object
        ) -> float:
        try: 
            return SE.total_number_of_unique_punctuations_
        except AttributeError:
            pos_list = [token.lemma_ for token in SE.doc if token.pos_=="PUNCT"]
            SE.total_number_of_unique_punctuations_ = len([*set(pos_list)])
            return SE.total_number_of_unique_punctuations_

    def total_number_of_subordinating_conjunctions(
        SE: object
        ) -> float:
        try: 
            return SE.total_number_of_subordinating_conjunctions_
        except AttributeError:
            pos_list = [token.pos_ for token in SE.doc]
            SE.total_number_of_subordinating_conjunctions_ = pos_list.count("SCONJ")
            return SE.total_number_of_subordinating_conjunctions_

    def total_number_of_unique_subordinating_conjunctions(
        SE: object
        ) -> float:
        try: 
            return SE.total_number_of_unique_subordinating_conjunctions_
        except AttributeError:
            pos_list = [token.lemma_ for token in SE.doc if token.pos_=="SCONJ"]
            SE.total_number_of_unique_subordinating_conjunctions_ = len([*set(pos_list)])
            return SE.total_number_of_unique_subordinating_conjunctions_

    def total_number_of_symbols(
        SE: object
        ) -> float:
        try: 
            return SE.total_number_of_symbols_
        except AttributeError:
            pos_list = [token.pos_ for token in SE.doc]
            SE.total_number_of_symbols_ = pos_list.count("SYM")
            return SE.total_number_of_symbols_

    def total_number_of_unique_symbols(
        SE: object
        ) -> float:
        try: 
            return SE.total_number_of_unique_symbols_
        except AttributeError:
            pos_list = [token.lemma_ for token in SE.doc if token.pos_=="SYM"]
            SE.total_number_of_unique_symbols_ = len([*set(pos_list)])
            return SE.total_number_of_unique_symbols_

    def total_number_of_verbs(
        SE: object
        ) -> float:
        try: 
            return SE.total_number_of_verbs_
        except AttributeError:
            pos_list = [token.pos_ for token in SE.doc]
            SE.total_number_of_verbs_ = pos_list.count("VERB")
            return SE.total_number_of_verbs_
    
    def total_number_of_unique_verbs(
        SE: object
        ) -> float:
        try: 
            return SE.total_number_of_unique_verbs_
        except AttributeError:
            pos_list = [token.lemma_ for token in SE.doc if token.pos_=="VERB"]
            SE.total_number_of_unique_verbs_ = len([*set(pos_list)])
            return SE.total_number_of_unique_verbs_

    def total_number_of_spaces(
        SE: object
        ) -> float:
        try: 
            return SE.total_number_of_spaces_
        except AttributeError:
            pos_list = [token.pos_ for token in SE.doc]
            SE.total_number_of_spaces_ = pos_list.count("SPACE")
            return SE.total_number_of_spaces_

    def total_number_of_unique_spaces(
        SE: object
        ) -> float:
        try: 
            return SE.total_number_of_unique_spaces_
        except AttributeError:
            pos_list = [token.lemma_ for token in SE.doc if token.pos_=="SPACE"]
            SE.total_number_of_unique_spaces_ = len([*set(pos_list)])
            return SE.total_number_of_unique_spaces_
