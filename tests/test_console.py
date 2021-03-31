#!/usr/bin/python3
"""Test module for console
"""
import unittest
import console
import pep8


class test_console(unittest.TestCase):

    """Tests"""

    def test_pep8(self):
        """Test pep8"""
        style = pep8.StyleGuide(quiet=True)
        check = style.check_files(['console.py'])
        self.assertEqual(check.total_errors, 0, "needs fixes")

    def test_doc(self):
        """Test docstring"""
        self.assertIsNot(console.HBNBCommand.__doc__, None)
        self.assertTrue(len(console.HBNBCommand.__doc__) >= 1)
