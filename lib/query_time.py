import time


class QueryTime(object):

    def __init__(self):
        pass

    @staticmethod
    def get_query_time(mov_query):
        t = time.time()
        result = mov_query()
        elapsed = time.time() - t
        return result, elapsed
