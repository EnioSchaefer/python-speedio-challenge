import uvicorn
from models.connection_options.connection import DBConnectionHandler
from controllers.api_controller import ApiController
from fastapi import FastAPI, Response, Body, BackgroundTasks
import tracemalloc
from pydantic import BaseModel

class RequestBody(BaseModel):
    url: str

class SpeedioChallenge:
    def __init__(self):
        self.app = FastAPI()
        self.__db_handler = DBConnectionHandler()
        self.__db_handler.connect_to_db()
        self.__db_connection = self.__db_handler.get_db_connection()
        self.__controller = ApiController(self.__db_connection)

    def setup_routes(self):
        @self.app.post('/salve_info')
        async def salve_info(response: Response, background_tasks: BackgroundTasks, body: RequestBody):
            return await self.__controller.salve_info(response, background_tasks, body.url)

        @self.app.post('/get_info')
        async def get_info(response: Response, body: RequestBody):
            return await self.__controller.get_info(response, body.url)

if __name__ == '__main__':
    speedio_challenge = SpeedioChallenge()
    speedio_challenge.setup_routes()
    tracemalloc.start()
    uvicorn.run(speedio_challenge.app, host="localhost", port=8000)