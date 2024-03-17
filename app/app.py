from models.connection_options.connection import DBConnectionHandler
from controllers.api_controller import ApiController
from flask import Flask


class SpeedioChallenge:
    def __init__(self, name=__name__):
        self.app = Flask(name)
        self.__db_handler = DBConnectionHandler()
        self.__db_handler.connect_to_db()
        self.__db_connection = self.__db_handler.get_db_connection()
        self.__controller = ApiController(self.__db_connection)

    def setup_routes(self):
        @self.app.route('/salve_info', methods=['POST'])
        def salve_info(): return self.__controller.salve_info()

        @self.app.route('/get_info', methods=['POST'])
        def get_info(): return self.__controller.get_info()

if __name__ == '__main__':
    speedio_challenge = SpeedioChallenge()
    speedio_challenge.setup_routes()
    speedio_challenge.app.run(debug=True)