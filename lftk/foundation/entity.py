class Entity:
    def total_number_of_named_entities(
        SE: object
        ) -> float:
        try:
            return SE.total_number_of_named_entities_ 
        except AttributeError:
            doc_total = 0
            for ent in SE.doc.ents:
                doc_total += 1
            SE.total_number_of_named_entities_ = doc_total
            return SE.total_number_of_named_entities_
