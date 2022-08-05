from flask import Flask

# creamos objeto flask
app = Flask(__name__) # __name__ es alias de nombre del archivo

@app.route('/') # va a ser una API web, necesita una ruta
def hello_flask():
    return 'Hello Flask'

if __name__ == '__main__':
    app.run(debug = True, host = '127.0.0.1', port = 5000)