"""
Class that emulates the behaviour of the Set
"""


class SetEmulator(object):
    def __init__(self, iterable=None):
        """
        Constructor for the SetEmulator class
        :param iterable: data that the set will have in its initialization
        """
        self._data = {}
        if iterable is not None:
            self.add(iterable)

    def elements(self):
        return self._data.keys()

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

    def intersection(self, other):
        return list(self.elements() & other.elements())

    def difference(self, other):
        self_elements = list(self.elements())
        other_elements = list(other.elements())
        return [a for a in self_elements + other_elements if (a not in self_elements) or (a not in other_elements)]

    def is_included(self, snd_set):
        for elem in snd_set.elements():
            if elem not in self.elements():
                return False
        return True

    def symmetrical_difference(self, other):
        self_elements = list(self.elements())
        other_elements = list(other.elements())
        sym_diff = set(i for i in self_elements) ^ set(i for i in other_elements)
        return [i for i in self_elements if i in sym_diff] + [i for i in other_elements if i in sym_diff]


