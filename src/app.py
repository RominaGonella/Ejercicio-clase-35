from flask import Flask, render_template, jsonify, request
import pickle
import pandas as pd
import numpy as np

# creamos objeto flask
app = Flask(__name__) # __name__ es alias de nombre del archivo

@app.route('/') # va a ser una API web, necesita una ruta
def hello_flask():
    return 'Hello Flask'

@app.route('/inicio')
def show_home():
    return render_template('index.html')

# en flask app.route se debe escribir toda la palabra string
@app.route('/<string:country>/<string:variety>/<float:aroma>/<float:aftertaste>/<float:acidity>/<float:body>/<float:balance>/<float:moisture>')
def result(country, variety, aroma, aftertaste, acidity, body, balance, moisture):
    cols = ['country_of_origin', 'variety', 'aroma', 'aftertaste', 'acidity', 'body', 'balance', 'moisture']
    data = [country, variety, aroma, aftertaste, acidity, body, balance, moisture]
    posted = pd.DataFrame(np.array(data).reshape(1,8), columns = cols)
    # se carga el modelo
    loaded_model = pickle.load(open('models/coffee_model.pkl', 'rb'))
    # se predice con datos creados
    result = loaded_model.predict(posted)
    # salida a mostrar
    text_result = result.tolist()[0]
    if text_result == 'Yes':
        return jsonify(message = 'Sí es un café de especialidad'), 200 # 200 es el código de error
    else:
        return jsonify(message = 'No es un café de especialidad'), 200

if __name__ == '__main__':
    app.run(debug = True, host = '127.0.0.1', port = 5000)