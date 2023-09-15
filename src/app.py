'''
Creado por Oscar Fernando López Barrios
Proyecto Servir
Prueba Técnica
'''

# Importar librerias necesarias
from flask import Flask, render_template

# Correr Flask para la pagina
app = Flask(__name__)

# Crear la ruta principal
@app.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)