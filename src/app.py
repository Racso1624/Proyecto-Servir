'''
Creado por Oscar Fernando López Barrios
Proyecto Servir
Prueba Técnica
'''

# Importar librerias necesarias
from flask import Flask, render_template, request, url_for, redirect, flash, session
import psycopg2 
import psycopg2.extras
from dotenv import load_dotenv
import os

# Cargar informacion de la conexion a la base de datos
load_dotenv()

# Correr Flask para la pagina
app = Flask(__name__)
app.debug = True

# # Conexion a la base de datos que contiene la informacion
# database_connection = psycopg2.connect(
#     database = os.getenv("DATABASE"),
#     user = os.getenv("USER"),
#     password = os.getenv("PASSWORD"),
#     host = os.getenv("HOST"),
#     port = os.getenv("PORT")
# )

# Crear la ruta principal
@app.route('/')
def index():
    return render_template('index.html')

# Rutas para paginas de creacion
@app.route('/create_register')
def create_register():
    return render_template('create_register.html')

@app.route('/create_deparment')
def create_deparment():
    return render_template('create_deparment.html')

@app.route('/create_employee')
def create_employee():
    return render_template('create_employee.html')

@app.route('/register_employee')
def register_employee():
    return redirect(url_for('create_employee.html'))

@app.route('/register_department')
def register_department():
    return redirect(url_for('create_deparment.html'))


# Rutas para paginas de listado
@app.route('/list_registers')
def list_registers():
    return render_template('list_registers.html')


# Rutas para paginas de eliminacion
@app.route('/delete_register')
def delete_register():
    return render_template('delete_register.html')


# Rutas para paginas de actualizacion
@app.route('/update_register')
def update_register():
    return render_template('update_register.html')

if __name__ == '__main__':
    app.run(debug=True)