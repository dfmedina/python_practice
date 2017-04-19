class SetEmulator(object):

    def __init__(self, iterable=()):
        self.elements = []
        for item in iterable:
            self.add(item)

    def add(self, item):
        if item not in self.elements:
            self.elements.append(item)

    def remove(self, item):
        if item in self.elements:
            self.elements.remove(item)

    def difference(self, iterable=()):
        result_set = []
        for item in iterable.elements:
            if item not in self.elements:
                result_set.append(item)
        return result_set

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

