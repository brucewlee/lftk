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
    
    def total_number_of_syllables(
        SE: object,
        ) -> int:
        try:
            return SE.total_number_of_syllables_
        except AttributeError:
            SE.total_number_of_syllables_ = 0
            # always remove punctuations
            token_list = [token for token in SE.doc if token.is_punct != True]
            if not SE.options['stop_words']:
                token_list = [token for token in token_list if token.is_stop != True]
            # start counting syllables per word
            for token in token_list:
                word = token.text.lower()
                vowels = "aeiouy"
                # if word starts with a vowel,
                if word[0] in vowels:
                    SE.total_number_of_syllables_ += 1
                for index in range(1, len(word)):
                    # if a character is vowel and the preceding character is not,
                    if word[index] in vowels and word[index - 1] not in vowels:
                        SE.total_number_of_syllables_ += 1
                # if word ends with e,
                if word.endswith("e"):
                    SE.total_number_of_syllables_ -= 1
                # if count was 0,
                if SE.total_number_of_syllables_ == 0:
                    SE.total_number_of_syllables_ += 1
        return SE.total_number_of_syllables_

    def total_number_of_words_more_than_two_syllables(
        SE: object,
        ) -> int:
        try:
            return SE.total_number_of_words_more_than_two_syllables_
        except AttributeError:
            SE.total_number_of_words_more_than_two_syllables_ = 0
            # always remove punctuations
            token_list = [token for token in SE.doc if token.is_punct != True]
            if not SE.options['stop_words']:
                token_list = [token for token in token_list if token.is_stop != True]
            # start counting syllables per word
            for token in token_list:
                word = token.text.lower()
                total_number_of_syllables_this_word_ = 0
                vowels = "aeiouy"
                # if word starts with a vowel,
                if word[0] in vowels:
                    total_number_of_syllables_this_word_ += 1
                for index in range(1, len(word)):
                    # if a character is vowel and the preceding character is not,
                    if word[index] in vowels and word[index - 1] not in vowels:
                        total_number_of_syllables_this_word_ += 1
                # if word ends with e,
                if word.endswith("e"):
                    total_number_of_syllables_this_word_ -= 1
                # if count was 0,
                if total_number_of_syllables_this_word_ == 0:
                    total_number_of_syllables_this_word_ += 1
                if total_number_of_syllables_this_word_ >= 3:
                    SE.total_number_of_words_more_than_two_syllables_ += 1
        return SE.total_number_of_words_more_than_two_syllables_

    def total_number_of_words_more_than_three_syllables(
        SE: object,
        ) -> int:
        try:
            return SE.total_number_of_words_more_than_three_syllables_
        except AttributeError:
            SE.total_number_of_words_more_than_three_syllables_ = 0
            # always remove punctuations
            token_list = [token for token in SE.doc if token.is_punct != True]
            if not SE.options['stop_words']:
                token_list = [token for token in token_list if token.is_stop != True]
            # start counting syllables per word
            for token in token_list:
                word = token.text.lower()
                total_number_of_syllables_this_word_ = 0
                vowels = "aeiouy"
                # if word starts with a vowel,
                if word[0] in vowels:
                    total_number_of_syllables_this_word_ += 1
                for index in range(1, len(word)):
                    # if a character is vowel and the preceding character is not,
                    if word[index] in vowels and word[index - 1] not in vowels:
                        total_number_of_syllables_this_word_ += 1
                # if word ends with e,
                if word.endswith("e"):
                    total_number_of_syllables_this_word_ -= 1
                # if count was 0,
                if total_number_of_syllables_this_word_ == 0:
                    total_number_of_syllables_this_word_ += 1
                if total_number_of_syllables_this_word_ >= 4:
                    SE.total_number_of_words_more_than_three_syllables_ += 1
        return SE.total_number_of_words_more_than_three_syllables_

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
