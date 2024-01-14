import unittest
from models import storage
from models.base_model import BaseModel
import json


class TestFileStorage(unittest.TestCase):
    def setUp(self):
        self.storage = storage()

    def test_all(self):
        self.assertEqual(self.storage.all(), {})

    def test_new(self):
        obj = BaseModel()
        self.storage.new(obj)
        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        self.assertEqual(self.storage.all()[key], obj)

    def test_save(self):
        obj = BaseModel()
        self.storage.new(obj)
        self.storage.save()
        with open(self.storage._FileStorage__file_path, "r") as f:
            self.assertEqual(json.load(f),
                             {obj.__class__.__name__ + "." +
                              obj.id: obj.to_dict()})

    def test_reload(self):
        obj = BaseModel()
        self.storage.new(obj)
        self.storage.save()
        self.storage.reload()
        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        self.assertEqual(self.storage.all()[key].to_dict(), obj.to_dict())


if __name__ == '__main__':
    unittest.main()
