import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
import pickle
df=pd.read_csv("Housing.csv")
df.basement.replace(['yes','no'],[1,0],inplace=True)
df.hotwaterheating.replace(['yes','no'],[1,0],inplace=True)
df.guestroom.replace(['yes','no'],[1,0],inplace=True)
df.airconditioning.replace(['yes','no'],[1,0],inplace=True)
df.prefarea.replace(['yes','no'],[1,0],inplace=True)
df.mainroad.replace(['yes','no'],[1,0],inplace=True)
df.furnishingstatus.replace(['furnished','semi-furnished','unfurnished'],[2,1,0],inplace=True)
x=df.drop("price",axis=1)
y=df.price
x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.2,random_state=42)
regg=LinearRegression()
regg.fit(x_train, y_train)
pickle.dump(regg,open("model.pkl","wb"))




