from pymongo import MongoClient

from base.config import MONGO_HOSTNAME, MONGO_PORT

class MongoEngine:
    client = MongoClient(MONGO_HOSTNAME, MONGO_PORT)
    database = ''
    engine = None

    def __new__(cls, *args, **kwargs):
        if not cls.engine:
            cls.engine = super(MongoEngine, cls).__new__(cls, *args, **kwargs)
        return cls.engine

    """
        Get the customers client.
    """
    def get_client(self):
        if self.database != '':
            return self.client[self.database]

        return None

    """
        Sets the database name.
    """
    def set_database_name(self, database):
        self.database = database

    """
        Gets the current database name.
    """
    def get_database_name(self):
        return self.database

    """
        Gets all database names.
    """
    def get_database_names(self):
        return self.get_client().list_database_names()

    """
        Drops a database.
    """
    def drop(self, dbname):
        self.client.drop_database(dbname)

    """
        Drops a collection.
    """
    def drop_collection(self, dbname, dbcollection):
        if dbname is not None and dbcollection is not None:
            self.client[dbname][dbcollection].drop()
