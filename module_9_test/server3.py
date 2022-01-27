from sklearn.linear_model import LinearRegression
from sklearn.datasets import load_diabetes
import numpy as np
import pickle
import numpy as np
from flask import Flask, request

X, y = load_diabetes(return_X_y=True)
X = X[:, 0].reshape(-1, 1) # Берём только один признак
regressor = LinearRegression()
regressor.fit(X,y)

with open('myfile.pkl', 'wb') as output:
   	pickle.dump(regressor, output) #Сохраняем

with open('myfile.pkl', 'rb') as pkl_file:
    	regressor_from_file = pickle.load(pkl_file) #Загружаем

app = Flask(__name__)

def model_predict(value):
    value_to_predict = np.array([value]).reshape(-1, 1)
    return regressor_from_file.predict(value_to_predict)

@app.route('/predict')
def predict_func():
    value = request.args.get('value')
    prediction = model_predict(int(value))
    return f'the result is {prediction}'

if __name__ == '__main__':
    app.run('localhost', 5000)

