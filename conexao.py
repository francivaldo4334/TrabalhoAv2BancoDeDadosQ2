import pymysql
from pymysql import cursors

class Conexao:

    def __init__(self) -> None:
        self.connection = pymysql.connect(
            host="127.0.0.1",
            user="root",
            passwd="root",
            port=3306,
            db="agenda",
        )

    def get_connection(self):
        return self.connection
