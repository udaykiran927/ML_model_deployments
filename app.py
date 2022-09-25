import os
from flask import Flask,render_template,request,jsonify
import numpy as np
import pickle

app=Flask(__name__)
model=pickle.load(open("model.pkl","rb"))

@app.route("/")
@app.route("/index")
def home():
    return render_template("index.html")

@app.route("/predict",methods=["POST"])

def predict():
    int_features=[int(i) for i in request.form.values()]
    print(int_features)
    features=[np.array(int_features)]
    prediction=model.predict(features)
    return render_template("index.html",house_price="The House Price will be around: {}".format(prediction))
        
if __name__=='__main__':
    app.run(debug=True)
