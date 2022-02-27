#!/usr/bin/env python
# coding: utf-8

# In[1]:


from flask import Flask


# In[2]:


app=Flask(__name__)


# In[3]:


from flask import request, render_template
from keras.models import load_model
import joblib

@app.route("/", methods=["GET","POST"])
def index():
    if request.method=="POST":
        Income = request.form.get("Income")
        Age = request.form.get("Age")
        Loan = request.form.get("Loan")
        Model = request.form.get("model")
        print(Income, Age, Loan, Model)
        
        if Model == 'Logistic Regression':
            model = joblib.load("LogisticRegression")
            
        elif Model == 'Decision Tree':
            model = joblib.load("DecisionTree")
            
        elif Model == 'Random Forest':
            model = joblib.load("RandomForest")
            
        elif Model == 'XGBoost':
            model = joblib.load("XGBoost")
            
        elif Model == 'Neural Network':
             model = load_model("NN")
                
        pred = model.predict([[float(Income), float(Age), float(Loan)]])
        if pred == [0]:
            pred = 'No'
        if pred == [1]:
            pred = 'Yes'
            
        final = "The predicted default is : " + pred
        return(render_template("index.html", result = final))
    
    else:
        return(render_template("index.html", result = "Thank you!!!"))


# In[4]:


if __name__ == "__main__":
    app.run()


# In[ ]:




