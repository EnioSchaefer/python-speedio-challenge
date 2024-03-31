from typing import Dict

class scrapedDataCollectionRepository:
    def __init__(self, db_connection):
        self.__db_connection = db_connection
        self.__db_collection = self.__db_connection.get_collection("scrapedData")

    def insert_processing_document(self, url: str) -> str:
        result = self.__db_collection.insert_one({
            "url": url,
            "status": "in progress"
        })
        format_inserted_id = str(result.inserted_id)

        return format_inserted_id

    def update_status(self, url: str, document: Dict, status: str) -> Dict:
        filter = {'url': url}

        new_values = {"$set": {'status': status, 'result': document}}

        self.__db_collection.update_one(filter, new_values)

        return document
    
    def find_by_url(self, url: str) -> Dict:
        document = self.__db_collection.find_one({"url": url})
        
        if document: document['_id'] = str(document['_id'])

        return document

    def delete_one(self, url: str) -> None:
        self.__db_collection.delete_one({"url": url})

        return
