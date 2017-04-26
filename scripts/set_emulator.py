class SetEmulator(object):

    def __init__(self, iterable=None):
        self._data = {}
        if iterable is not None:
            self.add(iterable)

    def __repr__(self):
        elements = self._data.keys()
        if sorted:
            elements.sort()
        return '%s(%r)' % (self.__class__.__name__, elements)

    def add(self, iterable):
        value = True
        if type(iterable) in (list, tuple, dict):
            it = iter(iterable)
            while True:
                for element in it:
                    self._data[element] = value
                return
        else:
            self._data[iterable] = value

    def remove(self, item):
        del self._data[item]

    def difference(self, other):
        result = []
        data = self._data
        otherdata = other._data
        for item in otherdata.keys():
            if item not in data.keys():
                result.append(item)
        return self.__class__(result)

    def intersection(self, other):
        result = []
        data = self._data
        otherdata = other._data
        for item in otherdata.keys():
            if item in data.keys():
                result.append(item)
        return self.__class__(result)

    '''
    def len(self):
        return len(self.elements)



    def discard(self, item):
        try:
            del self.elements[self.elements.index(item)]
        except ValueError:
            pass
    '''
