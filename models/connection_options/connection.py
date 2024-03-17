from pymongo import MongoClient
from .mongo_db_config import mongo_db_config

class DBConnectionHandler:
    def __init__(self) -> None:
        self.__connection_string = "mongodb://{}:{}@{}:{}/?authSource=admin".format(
            mongo_db_config["DB_USERNAME"],
            mongo_db_config["DB_PASSWORD"],
            mongo_db_config["DB_HOST"],
            mongo_db_config["DB_PORT"],
        )
        self.__db_name = mongo_db_config["DB_NAME"]
        self.__mongo_client = None
        self.__db_connection = None

    def connect_to_db(self):
        self.__mongo_client = MongoClient(self.__connection_string)
        self.__db_connection = self.__mongo_client[self.__db_name]

    def get_db_connection(self):
        return self.__db_connection
    
    def get_db_client(self):
        return self.__mongo_client