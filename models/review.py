#!/usr/bin/python3
"""
Initialisation of class
"""
from models.base_model import BaseModel


class Review(BaseModel):
    place_id = ""
    user_id = ""
    text = ""
