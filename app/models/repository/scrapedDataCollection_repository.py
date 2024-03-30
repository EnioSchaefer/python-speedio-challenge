from typing import Dict

class scrapedDataCollectionRepository:
    def __init__(self, db_connection) -> None:
        self.__db_connection = db_connection
        self.__db_collection = self.__db_connection.get_collection("scrapedData")

    def insert_processing_document(self, url: str) -> str:
        result = self.__db_collection.insert_one({
            "url": url,
            "status": "in progress"
        })

        return result.inserted_id

    def insert_document(self, document: Dict) -> Dict:
        self.__db_collection.insert_one(document)

        return document
    
    def find_by_url(self, url: str) -> Dict:
        document = self.__db_collection.find_one({"url": url})
        
        if document: document['_id'] = str(document['_id'])

        return document
