from models.repository.scrapedDataCollection_repository import scrapedDataCollectionRepository
from utils.similar_web_scraping import SimilarWebScraping
from fastapi import BackgroundTasks, Response, status
from fastapi.responses import JSONResponse

class ApiController:
    def __init__(self, db_connection) -> None:
        self.__db_connection = db_connection
        self.__repository = scrapedDataCollectionRepository(self.__db_connection)

    async def __scrape_data(self, response: Response, url: str):
        try:
            web_scraper = SimilarWebScraping(url)
            result = await web_scraper.scrape_data()
            
            self.__repository.update_status(url=url, document=result, status='complete')
        except ValueError as e:
            self.__repository.update_status(url, {}, 'error')
            print({"error": str(e)})
        except Exception as e:
            self.__repository.update_status(url, {}, 'error')
            print({"error": str(e)})


    async def salve_info(self, response: Response, background_tasks: BackgroundTasks, url: str):
        try:
            find_document = self.__repository.find_by_url(url)

            result = {}

            if not find_document:
                result = self.__repository.insert_processing_document(url)
            else:
                result = str(find_document['_id'])

            background_tasks.add_task(self.__scrape_data, response, url)
            
            response.status_code = status.HTTP_202_ACCEPTED
            return JSONResponse(content={'id': result})
        except Exception as e:
            response.status_code = status.HTTP_500_INTERNAL_SERVER_ERROR
            return JSONResponse(content={"error": str(e)})
    
    async def get_info(self, response: Response, url: str):
        try:
            result = self.__repository.find_by_url(url)
            if not result: 
                response.status_code = status.HTTP_404_NOT_FOUND
                return JSONResponse(content={"error": "Website not found"})

            if result['status'] == "in progress":
                response.status_code = status.HTTP_102_PROCESSING
                return JSONResponse(content={"error": "Request is still being processed"})
            
            if result['status'] == "error":
                response.status_code = status.HTTP_400_BAD_REQUEST
                return JSONResponse(content={"error": "There was a problem with the request"})

            response.status_code = status.HTTP_200_OK
            return JSONResponse(content=result)
        except Exception as e:
            response.status_code = status.HTTP_500_INTERNAL_SERVER_ERROR
            return JSONResponse(content={"error": str(e)})
