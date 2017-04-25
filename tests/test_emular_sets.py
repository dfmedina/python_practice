# coding=utf-8
"""
This module contains a set of test cases for the exercise: Emulate Sets

Create a class to represent and handle a Set. The class must provide the next operations:

- Add an element to the Set.
- Remove an element from the Set.
- Difference between a Set and another.
- Intersection between a given Set and another.
- A method that determines if a Set is included in another. All the elements from one Set must be in the other one.
- Symmetrical difference between one Set and another.
- Cartesian product between one Set and another.
- Power set of a given Set.

"""

import unittest
from scripts.set_emulator import SetEmulator
import logging
import sets


class TestEmulateSets(unittest.TestCase):
    # logging.basicConfig(filename='Unittest_results.log', level=logging.INFO)

    def setUp(self):
        self.set_instance = SetEmulator([1, 2, ('a', None), 4, 5, 5, 4, ('a', None), [0, 1, 2, 3, 4]])
        a = sets.Set
        a.symmetric_difference()
        # logging.log(logging.INFO, ("Set instance: %", self.set_instance.elements))

    def test_add_element(self):
        new_element = 7
        self.set_instance.add(new_element)
        self.assertIn(new_element, self.set_instance.elements)

    def test_remove_element(self):
        remove_element = ('a', None)
        self.set_instance.remove(remove_element)
        self.assertNotIn(remove_element, self.set_instance.elements)

    def test_get_difference(self):
        snd_set = SetEmulator([1, 2, 0, ('a', None), 'z'])
        print(self.set_instance.difference(snd_set))
        self.assertNotIn(self.set_instance.difference(snd_set), self.set_instance.elements)

    def test_get_intersection(self):
        snd_set = SetEmulator([1, 2, 0, ('a', None), 'z'])
        self.assertTrue(self.assertIn(self.set_instance.intersection(snd_set), snd_set.elements) and
                        self.assertIn(self.set_instance.intersection(snd_set), self.set_instance.elements))

    def test_get_included(self):
        pass

    def test_symmetrical_difference(self):
        pass

    def test_cartesian_product(self):
        pass

    def test_power_set(self):
        pass

if __name__ == '__main__':
    unittest.main()
