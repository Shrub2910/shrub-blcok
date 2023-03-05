class Key:

    def __init__(self, data):
        
        self.data = data
        self.record = self.data["record"]

        self.token = self.record["key"]
        self.owner = self.record["owner"]
        self.limit = self.record["limit"]
        self.queries_in_past_min = self.record["queriesInPastMin"]
        self.total_queries = self.record["totalQueries"]