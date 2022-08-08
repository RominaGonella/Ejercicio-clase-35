import pickle
import pandas pd
import numpy as np

country = 'Other'
variety = 'Other'
aroma = 7.42
aftertaste = 7.33
acidity = 7.42
body = 7.25
balance = 7.33
moisture = 0.0

# datos para probar el modelo
cols = ['country_of_origin', 'variety', 'aroma', 'aftertaste', 'acidity', 'body', 'balance', 'moisture']
data = [country, variety, aroma, aftertaste, acidity, body, balance, moisture]
posted = pd.DataFrame(np.array(data).reshape(1,8), columns = cols)

# se carga el modelo
loaded_model = pikle.load(open('../models/coffee_model.pkl', 'rb'))

# se predice con datos creados
result = loaded_model.predict(posted)

# salida a mostrar
text_result = result.tolist(result)[0]
print(text_result)