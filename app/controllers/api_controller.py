from models.repository.scrapedDataCollection_repository import scrapedDataCollectionRepository
from app.utils.similar_web_scraping import SimilarWebScraping

class ApiController:
    def __init__(self, db_connection) -> None:
        self.__db_connection = db_connection
        self.__repository = scrapedDataCollectionRepository(self.__db_connection)

    async def __scrape_data(self, url: str):
        web_scraper = SimilarWebScraping(url)
        result = await web_scraper.scrape_data()

        self.__repository.insert_document(result)

    async def salve_info(self, url: str):
        result = await self.__repository.insert_processing_document(url)

        self.__scrape_data(str)
        
        return result
    
    async def get_info(self, url: str):
        response = await self.__repository.find_by_url(url)

        return response
