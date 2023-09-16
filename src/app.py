'''
Creado por Oscar Fernando López Barrios
Proyecto Servir
Prueba Técnica
'''

# Importar librerias necesarias
from flask import Flask, render_template
import psycopg2 
import psycopg2.extras
from dotenv import load_dotenv
import os

# Cargar informacion de la conexion a la base de datos
load_dotenv()

# Correr Flask para la pagina
app = Flask(__name__)

# Conexion a la base de datos que contiene la informacion
database_connection = psycopg2.connect(
    database = os.getenv("DATABASE"),
    user = os.getenv("USER"),
    password = os.getenv("PASSWORD"),
    host = os.getenv("HOST"),
    port = os.getenv("PORT")
)

# Crear la ruta principal
@app.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)