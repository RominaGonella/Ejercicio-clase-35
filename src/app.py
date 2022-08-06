from flask import Flask, render_template, jsonify, request

# creamos objeto flask
app = Flask(__name__) # __name__ es alias de nombre del archivo

@app.route('/') # va a ser una API web, necesita una ruta
def hello_flask():
    return 'Hello Flask'

@app.route('/inicio')
def show_home():
    return render_template('index.html')

@app.route('/url_variables/<string:name>/<int:age>')
def url_variables(name, age):
    if age < 18:
        return jsonify(message = 'Lo siento ' + name + ', no estas autorizado/a'), 401 # convierte a json
    else:
        return jsonify(message = 'Bienvenido/a ' + name + ' puedes pasar'), 200

# 401 es código de error, 200 es que está bien

if __name__ == '__main__':
    app.run(debug = True, host = '127.0.0.1', port = 5000)