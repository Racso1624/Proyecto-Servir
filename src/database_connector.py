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
# Mediante el archivo .env
load_dotenv()

# Clase para Conectar la Base de Datos
class DatabaseConnector():

    def __init__(self) -> None:
        # Conexion a la base de datos que contiene la informacion
        # Mediante el uso de un archivo .env con la informacion
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
    
    # Funcion para consultar el codigo de un empleado
    def get_employee_code_query(self, employee_code):

        # Se crea el cursor para realizar la consulta
        database_cursor = self.database_connection.cursor(cursor_factory=psycopg2.extras.DictCursor)

        # Se ejecuta el query que se escribe dentro
        database_cursor.execute(
            """
            SELECT * FROM empleado WHERE id = '{0}';
            """.format(employee_code)
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
    
    # Funcion para obtener los empleados que estan asociados a un departamento
    def employees_in_department_query(self, department_id):

        # Se crea el cursor para realizar la consulta
        database_cursor = self.database_connection.cursor(cursor_factory=psycopg2.extras.DictCursor)

        # Se ejecuta el query que se escribe dentro
        database_cursor.execute(
            """
            SELECT * FROM empleado
            WHERE id_departamento = '{0}';
            """.format(department_id)
        )

        # Se retorna el resultado del query
        return database_cursor.fetchall()
    
    # Funcion para obtener todos los departamentos
    def get_departments_query(self):

        # Se crea el cursor para realizar la consulta
        database_cursor = self.database_connection.cursor(cursor_factory=psycopg2.extras.DictCursor)

        # Se ejecuta el query que se escribe dentro
        database_cursor.execute(
            """
            SELECT * FROM departamento;
            """
        )

        # Se retorna el resultado del query
        return database_cursor.fetchall()
    
    # Funcion para obtener todos los empleados
    def get_employees_query(self):

        # Se crea el cursor para realizar la consulta
        database_cursor = self.database_connection.cursor(cursor_factory=psycopg2.extras.DictCursor)

        # Se ejecuta el query que se escribe dentro
        database_cursor.execute(
            """
            SELECT * FROM empleado;
            """
        )

        # Se retorna el resultado del query
        return database_cursor.fetchall()
    
    # Funcion para crear un departamento
    def create_department_query(self, department_id, name, description):
        
        # Si el codigo del departamento no ha sido utilizado se crea el nuevo departamento
        if(not self.get_department_code_query(department_id)):
            # Se crea el cursor para realizar la consulta
            database_cursor = self.database_connection.cursor(cursor_factory=psycopg2.extras.DictCursor)

            # Se ejecuta el query que se escribe dentro
            database_cursor.execute(
                """
                INSERT INTO departamento(id, nombre, descripcion) VALUES ('{0}', '{1}', '{2}');
                """.format(department_id, name, description) # Se brindan los valores necesarios para el query
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

            # Se ejecuta el query que se escribe dentro
            database_cursor.execute(
                """
                INSERT INTO empleado(nombres, apellidos, fecha_nacimiento, id_departamento) VALUES ('{0}', '{1}', '{2}', '{3}');
                """.format(name, lastname, birthdate, department_code) # Se brindan los valores necesarios para el query
            )

            # Se realiza el commit de la nueva informacion en la base de datos
            self.database_connection.commit()
        # Si el codigo ya fue utilizado se retorna error
        else:
            return "ERROR"
    
    # Funcion para eliminar el departamento
    def delete_department_query(self, department_code):

        # Si el codigo del departamento existe se realiza la eliminacion
        if(self.get_department_code_query(department_code)):
            # Si el departamento no tiene empleados se elimina
            if(not self.employees_in_department_query(department_code)):

                # Se crea el cursor para realizar la consulta
                database_cursor = self.database_connection.cursor(cursor_factory=psycopg2.extras.DictCursor)

                # Se ejecuta el query que se escribe dentro
                database_cursor.execute(
                    """
                    DELETE FROM departamento WHERE id = '{0}';
                    """.format(department_code) # Se brindan los valores necesarios para el query
                )

                # Se realiza el commit de la nueva informacion en la base de datos
                self.database_connection.commit()
            # Se retorna el error
            else:
                return "TIENE EMPLEADOS"
        # Si el codigo ya fue utilizado se retorna error
        else:
            return "ERROR"
    
    # Funcion para eliminar el empleado
    def delete_employee_query(self, employee_code):

        # Si el codigo del empleado existe se elimina el empleado
        if(self.get_employee_code_query(employee_code)):
            # Se crea el cursor para realizar la consulta
            database_cursor = self.database_connection.cursor(cursor_factory=psycopg2.extras.DictCursor)

            # Se ejecuta el query que se escribe dentro
            database_cursor.execute(
                """
                DELETE FROM empleado WHERE id = '{0}';
                """.format(employee_code) # Se brindan los valores necesarios para el query
            )

            # Se realiza el commit de la nueva informacion en la base de datos
            self.database_connection.commit()
        # Si el codigo no existe se devuelve error
        else:
            return "ERROR"
    
    # Funcion para actualizar un departamento
    def update_department_query(self, department_id, name, description):

        # Si el codigo del departamento existe, entonces se actualiza
        if(self.get_department_code_query(department_id)):
            # Se crea el cursor para realizar la consulta
            database_cursor = self.database_connection.cursor(cursor_factory=psycopg2.extras.DictCursor)

            # Se ejecuta el query que se escribe dentro
            database_cursor.execute(
                """
                UPDATE departamento
                SET nombre = '{1}',
                    descripcion = '{2}'
                WHERE id = '{0}';
                """.format(department_id, name, description) # Se brindan los valores necesarios para el query
            )

            # Se realiza el commit de la nueva informacion en la base de datos
            self.database_connection.commit()
        # Si el codigo no existe se devuelve error
        else:
            return "ERROR"
        
    # Funcion para actualizar la informacion del empleado
    def update_employee_information_query(self, employee_id, name, lastname, birthdate):

        # Si el codigo del empleado existe se actualiza el empleado
        if(self.get_employee_code_query(employee_id)):
            # Se crea el cursor para realizar la consulta
            database_cursor = self.database_connection.cursor(cursor_factory=psycopg2.extras.DictCursor)

            # Se ejecuta el query que se escribe dentro
            database_cursor.execute(
                """
                UPDATE empleado
                SET nombres = '{1}',
                    apellidos = '{2}',
                    fecha_nacimiento = '{3}'
                WHERE id = '{0}';
                """.format(employee_id, name, lastname, birthdate) # Se brindan los valores necesarios para el query
            )

            # Se realiza el commit de la nueva informacion en la base de datos
            self.database_connection.commit()
        # Si el codigo no existe se devuelve error
        else:
            return "ERROR"
        
    # Funcion para actualizar el departamento del empleado
    def update_employee_department_query(self, employee_id, department_code):

        # Si el codigo del empleado existe se actualiza el empleado
        if(self.get_employee_code_query(employee_id)):
            if(self.get_department_code_query(department_code)):
                # Se crea el cursor para realizar la consulta
                database_cursor = self.database_connection.cursor(cursor_factory=psycopg2.extras.DictCursor)

                # Se ejecuta el query que se escribe dentro
                database_cursor.execute(
                    """
                    UPDATE empleado
                    SET id_departamento = '{1}'
                    WHERE id = '{0}';
                    """.format(employee_id, department_code) # Se brindan los valores necesarios para el query
                )

                # Se realiza el commit de la nueva informacion en la base de datos
                self.database_connection.commit()
            else:
                return "DEPARTAMENTO"
        # Si el codigo no existe se devuelve error
        else:
            return "ERROR"