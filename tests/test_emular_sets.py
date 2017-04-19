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


class TestEmulateSets(unittest.TestCase):

    def setUp(self):
        self.set_instance = SetEmulator()

    def test_add_element(self):
        pass

    def test_remove_element(self):
        pass

    def test_get_difference(self):
        pass

    def test_get_intersection(self):
        pass

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
