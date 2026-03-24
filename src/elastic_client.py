from elasticsearch import Elasticsearch

class ElasticClient:
    def __init__(self, host):
        self.client = Elasticsearch(host)

    def get_count(self, index):
        return self.client.count(index=index)["count"]