#!/usr/bin/env python3
"""nsert a document
"""


def insert_school(mongo_collection, **kwargs):
    """function that inserts a new document in a collection based on kwargs
    """
    value_id = mongo_collection.insert_one(kwargs)
    return value_id.inserted_id
