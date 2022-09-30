from flask import Flask,render_template,request
import numpy as np
import pickle

app=Flask(__name__)
model=pickle.load(open("model.pkl","rb"))

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/predict",methods=["GET","POST"])

def predict():
    int_features=[int(i) for i in request.form.values()]
    print(int_features)
    def ar():
        return int_features[0]
    def bed():
        return int_features[1]
    def dress():
        return int_features[2]
    def upst():
        return int_features[3]
    def mr():
        if int_features[4]==1:
            return "Yes"
        else:
            return "No"
    def gest():
        if int_features[5]==1:
            return "Yes"
        else:
            return "No"
    def bs():
        if int_features[6]==1:
            return "Yes"
        else:
            return "No"
    def ht():
        if int_features[7]==1:
            return "Yes"
        else:
            return "No"
    def air():
        if int_features[8]==1:
            return "Yes"
        else:
            return "No"
    def par():
        return int_features[9]
    def pre():
        if int_features[10]==1:
            return "Yes"
        else:
            return "No"
    def furn():
        if int_features[11]==2:
            return "Furnished"
        elif int_features[11]==1:
            return "Semi Furnished"
        else:
            return "No Furnishing"
    area=ar()
    bd=bed()
    bat=dress()
    us=upst()
    mard=mr()
    gs=gest()
    base=bs()
    hot=ht()
    airc=air()
    pr=par()
    pf=pre()
    fur=furn()
    features=[np.array(int_features)]
    prediction=model.predict(features)[0]
    return render_template("submit.html",are=area,bedrooms=bd,bathrms=bat,upstair=us,ma_rd=mard,gst=gs,bst=base,ht_wt=hot,ar_cn=airc,prk=pr,pr_f=pf,fr_st=fur,house_price="₹"+str(int(prediction)))
        
if __name__=='__main__':
    app.run(debug=True)
