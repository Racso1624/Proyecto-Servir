import psycopg2 
import psycopg2.extras
from dotenv import load_dotenv
import os

# Cargar informacion de la conexion a la base de datos
load_dotenv()

class DatabaseConnector():

    def __init__(self) -> None:
        # Conexion a la base de datos que contiene la informacion
        self.database_connection = psycopg2.connect(
            database = os.getenv("DATABASE"),
            user = os.getenv("USER"),
            password = os.getenv("PASSWORD"),
            host = os.getenv("HOST"),
            port = os.getenv("PORT")
        )

    def get_deparment_code_query(self, deparment_code):

        database_cursor = self.database_connection.cursor(cursor_factory=psycopg2.extras.DictCursor)

        database_cursor.execute(
            """
            SELECT * FROM departamento WHERE id = '{0}'
            """.format(deparment_code)
        )

        return database_cursor.fetchone()

    def create_deparment_query(self, id, name, description):

        database_cursor = self.database_connection.cursor(cursor_factory=psycopg2.extras.DictCursor)

        database_cursor.execute(
            """
            SELECT * FROM departamento WHERE id = '{0}'
            """.format(id, name, description)
        )

        return


    def create_employee_query(self):
        return None