#!/usr/bin/python3

"""
Unittest BaseModel:
test_init
test_save
test_to_dict
"""

import unittest
from datetime import datetime
from models.base_model import BaseModel


class TestBaseModel(unittest.TestCase):
    """"""
    def test_init(self):
        """"""
        obj = BaseModel()
        sizes = len(obj.id)
        self.assertIsInstance(obj.id, str)
        self.assertIsInstance(obj.created_at, datetime)
        self.assertIsInstance(obj.updated_at, datetime)
        self.assertEqual(sizes, 36)
        self.assertNotEqual(obj.created_at, obj.updated_at)

    def test_save(self):
        """"""
        obj = BaseModel()
        time_created = obj.created_at
        obj.save()
        self.assertNotEqual(obj.updated_at, time_created)
    
    def test_to_dict(self):
        """"""
        obj = BaseModel()
        o_dict = obj.to_dict()
        self.assertTrue(isinstance(o_dict, dict))
        self.assertEqual(len(o_dict), 4)
        self.assertTrue(isinstance(o_dict['created_at'], str))
        self.assertTrue(isinstance(o_dict['updated_at'], str))
        self.assertEqual(o_dict['__class__'], 'BaseModel')

    def test_str(self):
        """"""
        obj = BaseModel()
        o_str = str(obj)
        str_printed = "[BaseModel] ({}) {}".format(obj.id, obj.__dict__)
        self.assertEqual(o_str, str_printed)


if __name__ == '__main__':
    unittest.main()
