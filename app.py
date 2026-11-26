
## @file app.py
# @brief Aplicación web ligera en Flask para la demostración de CI/CD y documentación.
# @details Este módulo expone servicios HTTP REST para saludar a los usuarios y registrar eventos.
# @author Ariel Silva Ortega
# @date 2026-11-25

from flask import Flask, request
import html

app = Flask(__name__)

## @brief Ruta de saludo principal de la aplicación.
# @details Recibe el parámetro GET 'name', aplica sanitización contra XSS y retorna el mensaje HTML.
# @param name Nombre del usuario recibido por Query String (por defecto 'Mundo').
# @return Cadena de texto HTML con el saludo seguro renderizado.
@app.route('/hello')
def hello():
    name = request.args.get('name', 'Mundo')
    safe_name = html.escape(name)
    return f"Hello, {safe_name}!"


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)

