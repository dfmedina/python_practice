# coding=utf-8
"""
This module contains a set of test cases for the exercise: ETL Movies

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


class TestEmulateSets(unittest.TestCase):
    # logging.basicConfig(filename='Unittest_results.log', level=logging.INFO)

    def setUp(self):
        self.set_instance = SetEmulator([1, 2, ('a', None), 4, 'z', 5, 4, ('a', None)])
        # logging.log(logging.INFO, ("Set instance: %", self.set_instance.elements))

    def test_add_element(self):
        new_element = 7
        self.set_instance.add(new_element)
        self.assertIn(new_element, self.set_instance.elements())

    def test_remove_element(self):
        remove_element = ('a', None)
        self.set_instance.remove(remove_element)
        self.assertNotIn(remove_element, self.set_instance.elements())

    def test_get_intersection(self):
        snd_set = SetEmulator([1, 2, 0, ('a', None), 'z', 'w', (1, 2)])
        print(self.set_instance.intersection(snd_set))

    def test_get_difference(self):
        snd_set = SetEmulator([1, 2, 0, ('a', None), 'z', 'a'])
        print(self.set_instance.difference(snd_set))

    def test_get_is_included(self):
        snd_set = SetEmulator([1, 2, ('a', None)])
        trd_set = SetEmulator([1, 2, ('a', None), 'w'])
        self.assertTrue(self.set_instance.is_included(snd_set))
        self.assertFalse(self.set_instance.is_included(trd_set))

    def test_symmetrical_difference(self):
        snd_set = SetEmulator([1, 2, 0, ('a', None), 'z', 'a'])
        print(self.set_instance.symmetrical_difference(snd_set))

    def test_cartesian_product(self):
        snd_set = SetEmulator([1, 2, 0, ('a', None), 'z', 'a'])
        print(self.set_instance.cartesian_product(snd_set))

    def test_power_set(self):
        print(self.set_instance.power())


if __name__ == '__main__':
    unittest.main()
