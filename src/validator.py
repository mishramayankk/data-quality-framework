class Validator:

    @staticmethod
    def count_match(sf_count, es_count):
        return {
            "status": sf_count == es_count,
            "sf_count": sf_count,
            "es_count": es_count
        }