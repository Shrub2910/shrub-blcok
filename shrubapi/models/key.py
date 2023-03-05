class Key:

    def __init__(self, data):
        
        self._data = data
        self._record = self._data["record"]

        self.token = self._record["key"]
        self.owner = self._record["owner"]
        self.limit = self._record["limit"]
        self.queries_in_past_min = self._record["queriesInPastMin"]
        self.total_queries = self._record["totalQueries"]