#!/usr/bin/python3
"""Test database storage
"""
import unittest
from models import storage
from models.engine.db_storage import DBStorage
import pep8


class test_db_storage(unittest.TestCase):

    """Tests"""

    def test_pep8(self):
        """Test pep8 formatting"""
        style = pep8.StyleGuide(quiet=True)
        check = style.check_files(['models/engine/db_storage.py'])
        self.assertEqual(check.total_errors, 0, "needs fixes")

    def test_attrs(self):
        """Test for attrs"""
        self.assertTrue(hasattr(DBStorage, 'all'))
        self.assertTrue(hasattr(DBStorage, 'new'))
        self.assertTrue(hasattr(DBStorage, 'save'))
        self.assertTrue(hasattr(DBStorage, 'delete'))
        self.assertTrue(hasattr(DBStorage, 'reload'))
        self.assertTrue(hasattr(DBStorage, 'close'))
        self.assertTrue(hasattr(DBStorage, '_DBStorage__engine'))
        self.assertTrue(hasattr(DBStorage, '_DBStorage__session'))
