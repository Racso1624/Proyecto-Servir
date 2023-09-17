'''
Creado por Oscar Fernando López Barrios
Proyecto Servir
Prueba Técnica
'''

# Importar librerias necesarias
from flask import Flask, render_template, request, url_for, redirect, flash, session
from database_connector import DatabaseConnector

database = DatabaseConnector()

# Correr Flask para la pagina
app = Flask(__name__)
app.secret_key = 'prueba'

# Crear la ruta principal
@app.route('/')
def index():
    return render_template('index.html')

# Rutas para paginas de creacion
@app.route('/create_register')
def create_register():
    return render_template('create_register.html')

@app.route('/create_deparment', methods=['GET'])
def create_deparment():
    return render_template('create_deparment.html')

@app.route('/create_employee', methods=['POST'])
def create_employee():
    return render_template('create_employee.html')

@app.route('/register_employee')
def register_employee():
    return redirect(url_for('create_employee'))

@app.route('/register_department', methods=['POST'])
def register_department():

    deparment_id = request.form['code']
    deparment_name = request.form['name']
    deparment_description = request.form['description']
    result = database.create_deparment_query(deparment_id, deparment_name, deparment_description)

    if result == "ERROR":
        flash(("Código de departamento ya existe", 'danger'))
    else:
        flash(("Departamento registrado exitosamente", 'success'))

    return redirect(url_for('create_deparment'))


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