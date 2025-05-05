#!/usr/bin/env python3
def list_all(mongo_collection):
    """
    Te odio mongo.
    """
    documents = list(mongo_collection.find())
    return documents
