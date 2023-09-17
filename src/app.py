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

@app.route('/create_department', methods=['GET'])
def create_department():
    return render_template('create_department.html')

@app.route('/create_employee', methods=['GET'])
def create_employee():
    return render_template('create_employee.html')

@app.route('/register_employee', methods=['POST'])
def register_employee():
    employee_name = request.form['name']
    employee_lastname = request.form['lastname']
    employee_birthdate = request.form['dateOfBirth']
    employee_department = request.form['department']
    result = database.create_employee_query(employee_name, employee_lastname, employee_birthdate, employee_department)

    if result == "ERROR":
        flash(("Código de departamento no existe", 'danger'))
    else:
        flash(("Empleado registrado exitosamente", 'success'))

    return redirect(url_for('create_employee'))

@app.route('/register_department', methods=['POST'])
def register_department():

    department_id = request.form['code']
    department_name = request.form['name']
    department_description = request.form['description']
    result = database.create_department_query(department_id, department_name, department_description)

    if result == "ERROR":
        flash(("Código de departamento ya existe", 'danger'))
    else:
        flash(("Departamento registrado exitosamente", 'success'))

    return redirect(url_for('create_department'))


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