#!/usr/bin/python3
"""
Initialisation of class
"""


import models
import uuid
from datetime import datetime


class BaseModel:
    """
    The base model class that contains the common attributes/methods
    for other classes
    """

    def __init__(self, *args, **kwargs):
        """ Initiale method"""

        if kwargs:
            for key, value in kwargs.items():
                if key != '__class__':
                    setattr(self, key, value)
            self.created_at = datetime.strptime(kwargs['created_at'],
                                                '%Y-%m-%dT%H:%M:%S.%f')
            self.updated_at = datetime.strptime(kwargs['updated_at'],
                                                '%Y-%m-%dT%H:%M:%S.%f')
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            models.storage.new(self)

    def update(self):
        """ Update method"""

        self.updated_at = datetime.now()

    def __str__(self):
        """ str method"""

        return "[{}] ({}) {}".format(self.__class__.__name__,
                                     self.id, self.__dict__)

    def save(self):
        """ save method. Updates the update_at attribute"""

        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        """ to_dict method returns a dictionary """
        dict_copy = self.__dict__.copy()
        dict_copy['__class__'] = type(self).__name__
        dict_copy['created_at'] = self.created_at.isoformat()
        dict_copy['updated_at'] = self.updated_at.isoformat()
        return dict_copy

    @classmethod
    def from_dict(cls, dict_repr):
        obj = cls()
        obj.__dict__.update(dict_repr)
        obj.created_at = datetime.fromisoformat(obj.created_at)
        obj.updated_at = datetime.fromisoformat(obj.updated_at)
        return obj
