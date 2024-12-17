from flask import Flask, render_template, request, redirect, url_for

# Crear la instancia de la aplicación Flask
app = Flask(__name__)

# Lista de estudiantes (simulando una base de datos)
estudiantes = []

# Ruta para la página principal (Formulario de registro)
@app.route('/')
def index():
    return render_template('index.html')

# Ruta para registrar estudiantes
@app.route('/registrar', methods=['POST'])
def registrar():
    # Obtener los datos del formulario
    nombre = request.form['nombre']
    edad = request.form['edad']
    email = request.form['email']

    # Validar que los campos no estén vacíos
    if nombre and edad and email:
        # Agregar el nuevo estudiante a la lista
        estudiantes.append({'nombre': nombre, 'edad': edad, 'email': email})
        # Redirigir a la página de estudiantes registrados
        return redirect(url_for('estudiantes_page'))
    
    # Si algún campo está vacío, volver a la página principal
    return redirect(url_for('index'))

# Ruta para mostrar los estudiantes registrados
@app.route('/estudiantes')
def estudiantes_page():
    return render_template('estudiantes.html', estudiantes=estudiantes)

# Ejecutar la aplicación
if __name__ == '__main__':
    app.run(debug=True)
