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

    def get_department_code_query(self, department_code):

        database_cursor = self.database_connection.cursor(cursor_factory=psycopg2.extras.DictCursor)

        database_cursor.execute(
            """
            SELECT * FROM departamento WHERE id = '{0}';
            """.format(department_code)
        )

        return database_cursor.fetchone()
    
    def get_number_of_employees_query(self):

        database_cursor = self.database_connection.cursor(cursor_factory=psycopg2.extras.DictCursor)

        database_cursor.execute(
            """
            SELECT COUNT(*) FROM empleado;
            """
        )

        return database_cursor.fetchone()

    def create_department_query(self, department, name, description):
        
        if(not self.get_department_code_query(department)):
            database_cursor = self.database_connection.cursor(cursor_factory=psycopg2.extras.DictCursor)

            database_cursor.execute(
                """
                INSERT INTO departamento(id, nombre, descripcion) VALUES ('{0}', '{1}', '{2}');
                """.format(department, name, description)
            )

            self.database_connection.commit()
        else:
            return "ERROR"


    def create_employee_query(self, name, lastname, birthdate, department_code):

        if(self.get_department_code_query(department_code)):
            database_cursor = self.database_connection.cursor(cursor_factory=psycopg2.extras.DictCursor)
            
            employee_number = str(self.get_number_of_employees_query()[0] + 1)
            employee_id = "EMP-" + employee_number

            database_cursor.execute(
                """
                INSERT INTO empleado(id, nombres, apellidos, fecha_nacimiento, id_departamento) VALUES ('{0}', '{1}', '{2}', '{3}', '{4}');
                """.format(employee_id, name, lastname, birthdate, department_code)
            )

            self.database_connection.commit()
        else:
            return "ERROR"
        
        return None