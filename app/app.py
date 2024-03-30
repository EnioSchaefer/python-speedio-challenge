import uvicorn
from models.connection_options.connection import DBConnectionHandler
from controllers.api_controller import ApiController
from fastapi import FastAPI

class SpeedioChallenge:
    def __init__(self):
        self.app = FastAPI()
        self.__db_handler = DBConnectionHandler()
        self.__db_handler.connect_to_db()
        self.__db_connection = self.__db_handler.get_db_connection()
        self.__controller = ApiController(self.__db_connection)

    def setup_routes(self):
        @self.app.post('/salve_info')
        def salve_info(): return self.__controller.salve_info()

        @self.app.post('/get_info')
        def get_info(): return self.__controller.get_info()

if __name__ == '__main__':
    speedio_challenge = SpeedioChallenge()
    speedio_challenge.setup_routes()
    uvicorn.run(speedio_challenge.app, host="localhost", port=8000)