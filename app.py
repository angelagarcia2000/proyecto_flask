# Importamos la clase Flask desde el módulo flask
from flask import Flask

# Creamos una instancia de la aplicación Flask
# __name__ indica que el archivo actual será el punto de entrada
app = Flask(__name__)

# -------------------------------
# Ruta principal del sitio web
# -------------------------------
# Cuando un usuario accede a la URL raíz ('/'), se ejecuta la función inicio()
@app.route('/')
def inicio():
    # La función devuelve un texto plano que se mostrará en el navegador
    return '¡Hola, Flask está funcionando!'

# -------------------------------
# Ruta personalizada con parámetro
# -------------------------------
# Cuando el usuario accede a /usuario/<nombre>,
# Flask toma el valor que se ponga en <nombre> y lo pasa como argumento a la función usuario()
@app.route('/usuario/<nombre>')
def usuario(nombre):
    # Devuelve un mensaje dinámico con el nombre ingresado en la URL
    return f'Bienvenido, {nombre}!'

# -------------------------------
# Punto de entrada de la aplicación
# -------------------------------
# Verifica que el archivo se ejecute directamente (no como módulo importado)
if __name__ == '__main__':
    # Ejecuta la aplicación en modo debug (recarga automática y mensajes de error detallados)
    app.run(debug=True)
