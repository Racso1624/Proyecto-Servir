'''
Creado por Oscar Fernando López Barrios
Proyecto Servir
Prueba Técnica
'''

# Librerias necesarias para la conexion
import psycopg2 
import psycopg2.extras
from dotenv import load_dotenv
import os

# Cargar informacion de la conexion a la base de datos
load_dotenv()

# Clase para Conectar la Base de Datos
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

    # Funcion para consultar el codigo de un departamento
    def get_department_code_query(self, department_code):

        # Se crea el cursor para realizar la consulta
        database_cursor = self.database_connection.cursor(cursor_factory=psycopg2.extras.DictCursor)

        # Se ejecuta el query que se escribe dentro
        database_cursor.execute(
            """
            SELECT * FROM departamento WHERE id = '{0}';
            """.format(department_code)
        )

        # Se retorna el resultado del query
        return database_cursor.fetchone()
    
    # Funcion para obtener el numero de los empleados que existen en la base de datos 
    def get_number_of_employees_query(self):

        # Se crea el cursor para realizar la consulta
        database_cursor = self.database_connection.cursor(cursor_factory=psycopg2.extras.DictCursor)

        # Se ejecuta el query que se escribe dentro
        database_cursor.execute(
            """
            SELECT COUNT(*) FROM empleado;
            """
        )

        # Se retorna el resultado del query
        return database_cursor.fetchone()
    
    # Funcion para crear un departamento
    def create_department_query(self, department, name, description):
        
        # Si el codigo del departamento no ha sido utilizado se crea el nuevo departamento
        if(not self.get_department_code_query(department)):
            # Se crea el cursor para realizar la consulta
            database_cursor = self.database_connection.cursor(cursor_factory=psycopg2.extras.DictCursor)

            # Se ejecuta el query que se escribe dentro
            database_cursor.execute(
                """
                INSERT INTO departamento(id, nombre, descripcion) VALUES ('{0}', '{1}', '{2}');
                """.format(department, name, description) # Se brindan los valores necesarios para el query
            )

            # Se realiza el commit de la nueva informacion en la base de datos
            self.database_connection.commit()
        # Si el codigo ya fue utilizado se retorna error
        else:
            return "ERROR"

    # Funcion para crear un nuevo empleado
    def create_employee_query(self, name, lastname, birthdate, department_code):

        # Si el codigo del departamento existe en la base de datos, se agrega el empleado
        if(self.get_department_code_query(department_code)):
            # Se crea el cursor para realizar la consulta
            database_cursor = self.database_connection.cursor(cursor_factory=psycopg2.extras.DictCursor)
            
            # REVISAR EL FUNCIONAMIENTO DE ESTA PARTE
            # Se obtiene el numero de empleados en la base de datos
            employee_number = self.get_number_of_employees_query()[0] + 1
            employee_id = "EMP-"

            # Se crea el codigo a asignar del empleado
            for i in range(4 - employee_number):
                employee_id += "0"
            
            employee_id += str(employee_number)

            # Se ejecuta el query que se escribe dentro
            database_cursor.execute(
                """
                INSERT INTO empleado(id, nombres, apellidos, fecha_nacimiento, id_departamento) VALUES ('{0}', '{1}', '{2}', '{3}', '{4}');
                """.format(employee_id, name, lastname, birthdate, department_code) # Se brindan los valores necesarios para el query
            )

            # Se realiza el commit de la nueva informacion en la base de datos
            self.database_connection.commit()
        # Si el codigo ya fue utilizado se retorna error
        else:
            return "ERROR"