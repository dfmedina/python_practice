from itertools import ifilter, ifilterfalse


class SetEmulator(object):

    def __init__(self, iterable=None):
        """Construct a set from an optional iterable."""
        self.info = {}
        if iterable is not None:
            self._update(iterable)

    def add(self, item):
        if item not in self.elements:
            self.elements.append(item)

    def remove(self, item):
        if item in self.elements:
            self.elements.remove(item)

    def difference(self, other):
        """Return the symmetric difference of two sets as a new set.

                (I.e. all elements that are in exactly one of the sets.)

        """
        result = self.__class__()
        data = result._data
        value = True
        selfdata = self._data
        try:
            otherdata = other._data
        except AttributeError:
            otherdata = SetEmulator(other)._data
        for elt in ifilterfalse(otherdata.__contains__, selfdata):
            data[elt] = value
        for elt in ifilterfalse(selfdata.__contains__, otherdata):
            data[elt] = value
        return result

        """
        result_set = []
        for item in iterable.elements:
            if item not in self.elements:
                result_set.append(item)
        return result_set
        """

    def intersection(self, iterable=()):
        result_set = []
        for item in iterable.elements:
            if item in self.elements:
                result_set.append(item)
        return result_set

    def len(self):
        return len(self.elements)



    def discard(self, item):
        try:
            del self.elements[self.elements.index(item)]
        except ValueError:
            pass


if __name__ == '__main__':
    set_instance = Set()
    set_instance.add()
    set_instance.remove()

