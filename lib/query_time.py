import time


class QueryTime(object):

    def __init__(self):
        pass

    @staticmethod
    def get_query_time(query):
        t = time.time()
        result = query()
        elapsed = time.time() - t
        return result, elapsed
