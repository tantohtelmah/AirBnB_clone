#!/usr/bin/python3
import unittest
from models.base_model import BaseModel


class TestMyClass(unittest.TestCase):
    def test_init_with_kwargs(self):
        obj = BaseModel(foo=1, bar=2)
        self.assertEqual(obj.foo, 1)
        self.assertEqual(obj.bar, 2)

    def test_init_without_kwargs(self):
        obj = BaseModel()
        self.assertIsNotNone(obj.id)
        self.assertIsNotNone(obj.created_at)
        self.assertIsNotNone(obj.updated_at)

    def test_update(self):
        obj = BaseModel()
        old_updated_at = obj.updated_at
        obj.update()
        self.assertNotEqual(obj.updated_at, old_updated_at)

    def test_str(self):
        obj = BaseModel(foo=1, bar=2)
        self.assertEqual(str(obj),
                         "[MyClass] ({}) {'foo': 1, 'bar': 2}".format(obj.id))

    def test_update(self):
        obj = BaseModel()
        old_updated_at = obj.updated_at
        obj.update()
        self.assertNotEqual(obj.updated_at, old_updated_at)

    def test_str(self):
        obj = BaseModel(foo=1, bar=2)
        self.assertEqual(str(obj),
                         "[MyClass] ({}) {'foo': 1, 'bar': 2}".format(obj.id))
