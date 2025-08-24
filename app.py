
from flask import Flask, render_template

# Crear la aplicación Flask
app = Flask(__name__)

# Configuración básica
app.config['SECRET_KEY'] = 'tu_clave_secreta_aqui'

@app.route('/')
def index():
    """Página de inicio"""
    # Datos dinámicos para la página de inicio
    datos = {
        'titulo': 'Bienvenido a Mi Proyecto Flask',
        'mensaje': 'Esta es la página principal de nuestro sitio web.',
        'caracteristicas': [
            'Plantillas dinámicas con Jinja2',
            'Estructura de proyecto organizada',
            'Reutilización de componentes',
            'Diseño responsive'
        ]
    }
    return render_template('index.html', **datos)

@app.route('/about')
def about():
    """Página Acerca de"""
    # Información sobre el proyecto
    info_proyecto = {
        'titulo': 'Acerca de Nosotros',
        'descripcion': 'Este es un proyecto Flask desarrollado como parte del aprendizaje de desarrollo web con Python.',
        'tecnologias': [
            {'nombre': 'Flask', 'descripcion': 'Framework web de Python'},
            {'nombre': 'Jinja2', 'descripcion': 'Motor de plantillas'},
            {'nombre': 'HTML5', 'descripcion': 'Estructura del contenido'},
            {'nombre': 'CSS3', 'descripcion': 'Estilos y diseño'}
        ],
        'version': '1.0.0',
        'autor': 'Tu Nombre'
    }
    return render_template('about.html', **info_proyecto)

@app.errorhandler(404)
def page_not_found(error):
    """Página de error 404"""
    return render_template('404.html'), 404

if __name__ == '__main__':
    # Ejecutar la aplicación en modo debug
    app.run(debug=True, host='0.0.0.0', port=5000)


