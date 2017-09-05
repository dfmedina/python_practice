from functools import wraps
from time import time
import logging

logger = logging.getLogger()
logger.level = logging.DEBUG


def timed(f):
    @wraps(f)
    def wrapper(*args, **kwds):
        start = time()
        result = f(*args, **kwds)
        elapsed = time() - start
        logger.debug("%s took %d seconds to finish" % (f.__name__, elapsed))
        return result
    return wrapper


class QueryTime(object):

    def __init__(self):
        pass

    @staticmethod
    def get_query_time(mov_query):
        t = time()
        result = mov_query()
        elapsed = time() - t
        return result, elapsed
