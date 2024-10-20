from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/inscripcion', methods=['GET', 'POST'])
def inscripcion():
    if request.method == 'POST':
        nombre = request.form['nombre']
        apellido = request.form['apellido']
        curso = request.form['curso']
        return f'Inscripción exitosa: {nombre} {apellido} en {curso}'
    return render_template('inscripcion.html')

@app.route('/usuarios', methods=['GET', 'POST'])
def usuarios():
    if request.method == 'POST':
        nombre = request.form['nombre']
        apellido = request.form['apellido']
        correo = request.form['correo']
        return f'Usuario registrado: {nombre} {apellido} ({correo})'
    return render_template('usuarios.html')

@app.route('/productos', methods=['GET', 'POST'])
def productos():
    if request.method == 'POST':
        producto = request.form['producto']
        categoria = request.form['categoria']
        precio = request.form['precio']
        return f'Producto registrado: {producto} ({categoria}) - ${precio}'
    return render_template('productos.html')

@app.route('/libros', methods=['GET', 'POST'])
def libros():
    if request.method == 'POST':
        titulo = request.form['titulo']
        autor = request.form['autor']
        resumen = request.form['resumen']
        return f'Libro registrado: {titulo} por {autor}'
    return render_template('libros.html')

if __name__ == '__main__':
    app.run(debug=True)
