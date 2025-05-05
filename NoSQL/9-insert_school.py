#!/usr/bin/env python3
"""
Quiero terminar el mongo
"""


def insert_school(mongo_collection, **kwargs):
    """
    No te quiero ver más mongo.
    """
    result = mongo_collection.insert_one(kwargs)
    return result.inserted_id
