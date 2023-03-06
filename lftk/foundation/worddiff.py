import pandas as pd

from lftk.utils import get_pandas_row, safe_division

class WordDiff:
    def total_kuperman_age_of_acquistion_of_words(
        SE: object
        ) -> float:
        try:
            return SE.total_kuperman_age_of_acquistion_of_words_ 
        except AttributeError:
            # Load databse
            database = pd.read_csv(SE.paths['AOA_KUP_PATH'])
            # Iterate doc
            doc_total = 0
            for token in SE.doc:
                row = get_pandas_row(database, 'Word', token.lemma_)
                try:
                    doc_total += float(row[0]['Rating.Mean'])
                except IndexError:
                    pass
            SE.total_kuperman_age_of_acquistion_of_words_ = doc_total
            return SE.total_kuperman_age_of_acquistion_of_words_


    def total_brysbaert_age_of_acquistion_of_words(
        SE: object
        ) -> float:
        try:
            return SE.total_brysbaert_age_of_acquistion_of_words_ 
        except AttributeError:
            database = pd.read_csv(SE.paths['AOA_BRY_PATH'])
            doc_total = 0
            for token in SE.doc:
                rows = get_pandas_row(database, 'WORD', token.lemma_)
                aoa_by_token_meaning = []
                for row in rows:
                    try:
                        aoa_by_token_meaning.append(row['AoAtestbased'])
                    except IndexError:
                        pass
                doc_total += safe_division(
                    sum(aoa_by_token_meaning),len(aoa_by_token_meaning)
                    )
            SE.total_brysbaert_age_of_acquistion_of_words_ = doc_total
            return SE.total_brysbaert_age_of_acquistion_of_words_

    
    def total_subtlex_us_zipf_of_words(
        SE: object
        ) -> float:
        try:
            return SE.total_subtlex_us_zipf_of_words_ 
        except AttributeError:
            database = pd.read_csv(SE.paths['SUBTLEX_US_PATH'])
            doc_total = 0
            for token in SE.doc:
                row = get_pandas_row(database, 'Word', token.text.lower())
                try:
                    doc_total += float(row[0]['Zipf-value'])
                except IndexError:
                    pass
            SE.total_subtlex_us_zipf_of_words_ = doc_total
            return SE.total_subtlex_us_zipf_of_words_
