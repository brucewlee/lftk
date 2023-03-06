class WordSent:
    def total_number_of_words(
        SE: object,
        ) -> int:
        try:
            return SE.total_number_of_words_ 
        except AttributeError:   
            token_list = [token for token in SE.doc]
            if not SE.options['stop_words']:
                token_list = [token for token in token_list if token.is_stop != True]
            if not SE.options['punctuations']:
                token_list = [token for token in token_list if token.is_punct != True]
            # Calculate and save result
            SE.total_number_of_words_ = len(token_list)
            return SE.total_number_of_words_
    
    def total_number_of_unique_words(
        SE: object,
        ) -> int:
        try:
            return SE.total_number_of_unique_words_ 
        except AttributeError:   
            token_list = [token for token in SE.doc]
            if not SE.options['stop_words']:
                token_list = [token for token in token_list if token.is_stop != True]
            if not SE.options['punctuations']:
                token_list = [token for token in token_list if token.is_punct != True]
            # Count unique tokens in terms of lemma
            unique_token_list = [token.lemma_ for token in SE.doc]
            unique_token_list = list(set(unique_token_list))
            # Calculate and save result
            SE.total_number_of_unique_words_ = len(unique_token_list)
            return SE.total_number_of_unique_words_
    
    def total_number_of_unique_words_no_lemma(
        SE: object,
        ) -> int:
        try:
            return SE.total_number_of_unique_words_no_lemma_ 
        except AttributeError:   
            token_list = [token for token in SE.doc]
            if not SE.options['stop_words']:
                token_list = [token for token in token_list if token.is_stop != True]
            if not SE.options['punctuations']:
                token_list = [token for token in token_list if token.is_punct != True]
            # Count unique tokens in terms of lemma
            unique_token_list = [token.lemma_ for token in SE.doc]
            unique_token_list = list(set(unique_token_list))
            # Calculate and save result
            SE.total_number_of_unique_words_no_lemma_ = len(unique_token_list)
            return SE.total_number_of_unique_words_no_lemma_

    def total_number_of_sentences(
        SE: object,
        ) -> int:
        try:
            return SE.total_number_of_sentences_
        except AttributeError:
            # Calculate and save result
            SE.total_number_of_sentences_ =\
                len(list(SE.doc.sents))
            return SE.total_number_of_sentences_
    
    def total_number_of_characters(
        SE: object,
        ) -> int:
        try:
            return SE.total_number_of_characters_
        except AttributeError:
            token_list = [token for token in SE.doc]
            if not SE.options['stop_words']:
                token_list = [token for token in token_list if token.is_stop != True]
            if not SE.options['punctuations']:
                token_list = [token for token in token_list if token.is_punct != True]
            # Calculate and save result
            SE.total_number_of_characters_ =\
                sum([len(token) for token in token_list])
            return SE.total_number_of_characters_
