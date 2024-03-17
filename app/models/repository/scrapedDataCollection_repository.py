from typing import Dict

class scrapedDataCollectionRepository:
    def __init__(self, db_connection) -> None:
        self.__collection_name = "scrapedData"
        self.__db_connection = db_connection

    def insert_document(self, document: Dict) -> Dict:
        collection = self.__db_connection.get_collection(self.__collection_name)
        collection.insert_one(document)

        return document
    
    def find_by_url(self, url) -> Dict:
        collection = self.__db_connection.get_collection(self.__collection_name)
        document = collection.find_one({"url": url})
        
        if document: document['_id'] = str(document['_id'])

        return document
