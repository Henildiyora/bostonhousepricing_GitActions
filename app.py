import pickle
from flask import Flask,request,app,jsonify,url_for,render_template
import os
import numpy as np
import pandas as pd

app = Flask(__name__)

## Load the model 
model = pickle.load(open('model.pkl','rb'))
scaler = pickle.load(open('scaler.pkl','rb'))

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/predict_api',methods=['POST'])
def predict_api():
    data = request.json['data']

    if data is None:
        return jsonify({"error":"NO data provided"})
    
    print(type(data))
    print(np.array(list(data.values())).reshape(1,-1))

    new_data = scaler.transform(np.array(list(data.values())).reshape(1,-1))

    output = model.predict(new_data)

    print(output)

    return jsonify(output[0])

@app.route('/predict',methods=['POST'])
def predict():
    data = [float(x) for x in request.form.values()]
    final_input = scaler.transform(np.array(data).reshape(1,-1))

    print(f'Final input from HTML page = {final_input}')

    output = model.predict(final_input)[0]

    return render_template("home.html",prediction_text = "The House price prediction is {}".format(output))









if __name__ == "__main__":
    app.run(debug=True)









