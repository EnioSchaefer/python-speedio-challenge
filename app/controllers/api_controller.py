from models.repository.scrapedDataCollection_repository import scrapedDataCollectionRepository
from flask import request

class ApiController:
    def __init__(self, db_connection) -> None:
        self.__db_connection = db_connection
        self.__repository = scrapedDataCollectionRepository(self.__db_connection)

    # Ps.: Implementar essa função após criar o código de webScraping
    # def salve_info(self):
    #     scraped_data = request.json["scrapedData"]

    #     response = self.__repository.scrape_data(scraped_data)
    #     return response
    
    def get_info(self):
        url = request.json["url"]

        response = self.__repository.find_by_url(url)

        return response
