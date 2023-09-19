# Proyecto-Servir

### Descripción del Funcionamiento
Esta Web App realiza tareas de un sistema de control para empleados de una empresa, esto mediante una conexión a la base de datos con la estructura definida para dos entidades: Departamento y Empleado. Mediante la app se pueden realizar distintas operaciones:
- Crear Registros de Departamentos y Empleados
- Listar Registros
- Eliminar Registros
- Actualizar Registros

### Características necesarias para utilizar la Web App:
- Instalar flask: `pip install flask`
- Instalar psycopg2: `pip install psycopg2`
- Instalar dotenv: `pip install python-dotenv`
  
Se debe de crear un archivo .env con las siguiente características de la conexión a la base de datos:

```
DATABASE = database-name
USER = database-user
PASSWORD = database-password
HOST = database-host
PORT = database-host
```

El archivo .env se debe de guardar en src.

### Proceso para utilización de la Web App:
- Clonar el repositorio: `git clone https://github.com/Racso1624/Proyecto-Servir`
- Entrar a la carpeta: `cd src`
- Ejecutar la app: `flask run `
