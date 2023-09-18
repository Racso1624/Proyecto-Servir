'''
Creado por Oscar Fernando López Barrios
Proyecto Servir
Prueba Técnica
'''

# Importar librerias necesarias
from flask import Flask, render_template, request, url_for, redirect, flash, session
from database_connector import DatabaseConnector

# Conectar la base de datos 
database = DatabaseConnector()

# Correr Flask para la pagina
app = Flask(__name__)
app.secret_key = 'prueba'

# Crear la ruta principal
@app.route('/')
def index():
    return render_template('index.html')

# Rutas para paginas de creacion
# Metodo para cargar la pagina de registro de informacion
@app.route('/create_register')
def create_register():
    return render_template('create_register.html')

# Metodo para cargar la pagina de crear departamento
@app.route('/create_department', methods=['GET'])
def create_department():
    return render_template('create_department.html')

# Metodo para realizar la accion de crear departamento
@app.route('/register_department', methods=['POST'])
def register_department():

    # Se obtienen los datos por parte del form
    department_id = request.form['code']
    department_name = request.form['name']
    department_description = request.form['description']

    # Se ingresan los datos al query y se recibe el resultado
    result = database.create_department_query(department_id, department_name, department_description)

    # Si el resultado da error
    if(result == "ERROR"):
        # Se brinda un mensaje de error
        flash(("Código de departamento ya existe", 'danger'))
    # De lo contrario
    else:
        # Se brinda un mensaje correcto
        flash(("Departamento registrado exitosamente", 'success'))

    # Se redirecciona a la pagina de creacion
    return redirect(url_for('create_department'))

# Metodo para cargar la pagina de crear empleado
@app.route('/create_employee', methods=['GET'])
def create_employee():
    return render_template('create_employee.html')

# Metodo para realizar la accion de registrar empleado
@app.route('/register_employee', methods=['POST'])
def register_employee():

    # Se obtienen los datos por parte del form
    employee_name = request.form['name']
    employee_lastname = request.form['lastname']
    employee_birthdate = request.form['dateOfBirth']
    employee_department = request.form['department']

    # Se ingresan los datos al query y se recibe el resultado
    result = database.create_employee_query(employee_name, employee_lastname, employee_birthdate, employee_department)

    # Si el resultado da error
    if(result == "ERROR"):
        # Se brinda un mensaje de error
        flash(("Código de departamento no existe", 'danger'))
    # De lo contrario
    else:
        # Se brinda un mensaje correcto
        flash(("Empleado registrado exitosamente", 'success'))

    # Se redirecciona a la pagina de creacion
    return redirect(url_for('create_employee'))


# Rutas para paginas de listado
# Metodo para mostrar paginas de listado
@app.route('/list_registers')
def list_registers():
    return render_template('list_registers.html')

# Metodo para cargar la pagina de listar departamento
@app.route('/list_departments', methods=['GET'])
def list_departments():
    # Se obtiene el resultado de la base de datos
    result = database.get_departments()

    # Se comprueba que existan datos
    if(result):
        message = None
    # Si no existen se manda el mensaje para imprimir
    else:
        message = "No existen departamentos"

    # Se renderiza la pantalla con los resultados
    return render_template('list_departments.html', departments=result, message=message)

# Metodo para cargar la pagina de listar empleados
@app.route('/list_employees', methods=['GET'])
def list_employees():
    # Se obtiene el resultado de la base de datos
    result = database.get_employees()
    # Se comprueba que existan datos
    if(result):
        message = None
    # Si no existen se manda el mensaje para imprimir
    else:
        message = "No existen empleados"
    
    # Se renderiza la pantalla con los resultados
    return render_template('list_employees.html', employees=result, message=message)


# Rutas para paginas de eliminacion
@app.route('/delete_register')
def delete_register():
    return render_template('delete_register.html')

# Metodo para cargar la pagina de eliminar departamento
@app.route('/delete_department', methods=['GET'])
def delete_department():
    return render_template('delete_department.html')

# Metodo para realizar la accion de eliminar departamento
@app.route('/delete_register_department', methods=['POST'])
def delete_register_department():

    # Se obtienen los datos por parte del form
    department_id = request.form['code']

    # Se ingresan los datos al query y se recibe el resultado
    result = database.delete_department_query(department_id)

    # Si el resultado da error
    if(result == "ERROR"):
        # Se brinda un mensaje de error
        flash(("Código de departamento no existe", 'danger'))
    # Si tiene empleados asociados
    elif(result == "TIENE EMPLEADOS"):
        flash(("Departamento tiene empleados asociados", 'danger'))
    # De lo contrario
    else:
        # Se brinda un mensaje correcto
        flash(("Departamento eliminado exitosamente", 'success'))

    # Se redirecciona a la pagina de creacion
    return redirect(url_for('delete_department'))

# Metodo para cargar la pagina de eliminar empleado
@app.route('/delete_employee', methods=['GET'])
def delete_employee():
    return render_template('delete_employee.html')

# Metodo para realizar la accion de eliminar empleado
@app.route('/delete_register_employee', methods=['POST'])
def delete_register_employee():

    # Se obtienen los datos por parte del form
    employee_id = request.form['code']

    # Se ingresan los datos al query y se recibe el resultado
    result = database.delete_employee_query(employee_id)

    # Si el resultado da error
    if result == "ERROR":
        # Se brinda un mensaje de error
        flash(("Código de empleado no existe", 'danger'))
    # De lo contrario
    else:
        # Se brinda un mensaje correcto
        flash(("Empleado eliminado exitosamente", 'success'))

    # Se redirecciona a la pagina de creacion
    return redirect(url_for('delete_employee'))


# Rutas para paginas de actualizacion
@app.route('/update_register')
def update_register():
    return render_template('update_register.html')

@app.route('/update_department')
def update_department():
    return render_template('update_department.html')

@app.route('/update_employee')
def update_employee():
    return render_template('update_employee.html')

if __name__ == '__main__':
    app.run(debug=True)