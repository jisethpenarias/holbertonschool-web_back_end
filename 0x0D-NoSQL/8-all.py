#!/usr/bin/env python3
"""List all documents
"""
import pprint


def list_all(mongo_collection):
    """function that lists all documents in a collection
    """
    collection = []
    for doc in mongo_collection.find():
        collection.append(doc)

    return collection
