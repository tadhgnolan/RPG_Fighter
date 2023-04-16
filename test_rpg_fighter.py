"""
Module for unit testing framework.
"""

import unittest
import rpg_fighter


class TestRpgFighter(unittest.TestCase):
    """
    Unit test class.
    """

    def test_validate_data_for_correct_input(self):
        """
        Positive test function.
        """
        input_values = [
            "orc",
            "halfling",
            "dwarf",
            "skeleton",
            "elf",
            "human",
        ]

        expected_value = True
        actual_value = rpg_fighter.validate_data(values=input_values)
        self.assertEqual(actual_value, expected_value)

    def test_validate_data_for_incorrect_race(self):
        """
        Negative test function.
        """
        input_values = [
            "car",
            "halfling",
            "dwarf",
            "skeleton",
            "elf",
            "human",
        ]

        expected_value = False
        actual_value = rpg_fighter.validate_data(values=input_values)
        self.assertEqual(actual_value, expected_value)
