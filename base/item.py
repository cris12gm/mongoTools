from bson.json_util import dumps
import json

from base.mongo_engine import MongoEngine


class Item:
    collection_name = ''
    collection_schema = {}
    data = {}

    def __init__(self):
        pass

    """
        Returns the cursor to the collection.
    """
    def cursor(self):
        if self.collection_name != '':
            return MongoEngine().get_client()[self.collection_name]
        return None

    """
        Finds all the elements by the given criteria. Only returns the
        parameters specified in the projection.
    """
    def find(self, criteria={}, projection={}):
        _criteria = criteria if criteria else {'deleted': False}
        _projection = projection if projection else self.collection_schema
        data = json.loads(
            dumps(self.cursor().find(_criteria, _projection)))
        data_length = len(data)
        if data_length == 0:
            self.data = None
        elif data_length == 1:
            self.data = data[0]
        else:
            self.data = data

        return self

    """
        Inserts an item.
    """
    def insert(self, data=None):

        if data is None:
            return False
        elif type(data) is dict:
            _operation = 'insert_one'
        elif type(data) is list:
            _operation = 'insert_many'
        else:
            return False

        try:
            getattr(self.cursor(), _operation)(data)
            return True
        except Exception:
            return False

    """
        Completely removes an item by default. If force is false it marks the
        item as removed.
    """
    def remove(self, criteria={}):

        try:
            self.cursor().delete_one(filter=criteria)
            return True
        except Exception:
            return False

    """
        Updates the item that fits the criteria with the new data.
    """
    def update(self, criteria, data):
        try:
            self.cursor().update_one(filter=criteria, update={'$set': data})
            return True
        except Exception:
            return False
