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
    int_features=[i for i in request.form.values()]
    if int_features[4]=="Yes":
        int_features[4]=1
    else:
        int_features[4]=0
    if int_features[5]=="Yes":
        int_features[5]=1
    else:
        int_features[5]=0
    if int_features[6]=="Yes":
        int_features[6]=1
    else:
        int_features[6]=0
    if int_features[7]=="Yes":
        int_features[7]=1
    else:
        int_features[7]=0
    if int_features[8]=="Yes":
        int_features[8]=1
    else:
        int_features[8]=0
    if int_features[10]=="Yes":
        int_features[10]=1
    else:
        int_features[10]=0
    if int_features[11]=="Furnished":
        int_features[11]=2
    elif int_features[11]=="Semi-Furnished":
        int_features[11]=1
    else:
        int_features[11]=0
    int_feature=[int(i) for i in int_features]


    print(int_feature)
    def ar():
        return int_feature[0]
    def bed():
        return int_feature[1]
    def dress():
        return int_feature[2]
    def upst():
        return int_feature[3]
    def mr():
        if int_feature[4]==1:
            return "Yes"
        else:
            return "No"
    def gest():
        if int_feature[5]==1:
            return "Yes"
        else:
            return "No"
    def bs():
        if int_feature[6]==1:
            return "Yes"
        else:
            return "No"
    def ht():
        if int_feature[7]==1:
            return "Yes"
        else:
            return "No"
    def air():
        if int_feature[8]==1:
            return "Yes"
        else:
            return "No"
    def par():
        return int_feature[9]
    def pre():
        if int_feature[10]==1:
            return "Yes"
        else:
            return "No"
    def furn():
        if int_feature[11]==2:
            return "Furnished"
        elif int_feature[11]==1:
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
    features=[np.array(int_feature)]
    prediction=model.predict(features)[0]
    return render_template("submit.html",are=area,bedrooms=bd,bathrms=bat,upstair=us,ma_rd=mard,gst=gs,bst=base,ht_wt=hot,ar_cn=airc,prk=pr,pr_f=pf,fr_st=fur,house_price="₹"+str(int(prediction)))
        
if __name__=='__main__':
    app.run(debug=True)
