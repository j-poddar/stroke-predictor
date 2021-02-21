from flask import Flask, request, render_template
from flask_cors import cross_origin
import sklearn
import pickle
import pandas as pd
import numpy as np

app = Flask(__name__)
model = pickle.load(open("stroke_prediction_knn.pkl", "rb"))



@app.route("/")
@cross_origin()
def home():
    return render_template("index.html")




@app.route("/predict", methods = ["GET", "POST"])
@cross_origin()
def predict():
    if request.method == "POST":

        # Age
        age = float(request.form['age'])
        

        # avg_glucose_level
        avg_glucose_level = float(request.form['avg_glucose_level'])
        
        #bmi
        bmi = float(request.form['bmi'])
        
        #gender
        # Female = 0 (Not in column)
        gender = request.form['gender']
        if (gender == 'Male'):
            Male = 1
            Other = 0
        elif (gender == 'Other'):
            Male = 0
            Other = 1
        else:
            Male = 0
            Other = 0
            
        #hypertension
        # hype_No = 0 (Not in column)
        hypertension = request.form['hypertension']
        if (hypertension == 'hype_Yes'):
            hype_Yes = 1
        else:
            hype_Yes = 0
            
        #heart_disease
        #hdis_No = 0 (Not in column)
        heart_disease = request.form['heart_disease']
        if (heart_disease == 'hdis_Yes'):
            hdis_Yes = 1
        else:
            hdis_Yes = 0
            
        #ever_married
        #mar_No = 0 (Not in column)
        ever_married = request.form['ever_married']
        if (ever_married == 'mar_Yes'):
            mar_Yes = 1
        else:
            mar_Yes = 0
            
        
        #work_type
        
        
        #Govt_job = 0 (Not in column)
        work_type = request.form['work_type']
        if (work_type == 'Never_worked'):
            Never_worked = 1
            Private = 0
            Self_employed = 0
            children = 0
        elif (work_type == 'Private'):
            Never_worked = 0
            Private = 1
            Self_employed = 0
            children = 0
        elif (work_type == 'Self_employed'):
            Never_worked = 0
            Private = 0
            Self_employed = 1
            children = 0
        elif (work_type == 'children'):
            Never_worked = 0
            Private = 0
            Self_employed = 0
            children = 1
        else:
            Never_worked = 0
            Private = 0
            Self_employed = 0
            children = 0
            
        # Residence_type
        #Rural = 0 (Not in column)
        Residence_type = request.form['Residence_type']
        if (Residence_type == 'Urban'):
            Urban = 1
        else:
            Urban = 0
            
        # smoking_status 
        # Formerly_Smoked = 0 (Not in column)
        smoking_status = request.form['smoking_status']
        if (smoking_status == 'Never_Smoked'):
            Never_Smoked = 1
            Unknown = 0
            smokes = 0
        elif (smoking_status == 'Unknown'):
            Never_Smoked = 0
            Unknown = 1
            smokes = 0
        elif (smoking_status == 'smokes'):
            Never_Smoked = 0
            Unknown = 0
            smokes = 1
        else:
            Never_Smoked = 0
            Unknown = 0
            smokes = 0
            
        
        data =np.array([[age, avg_glucose_level, bmi, Male, Other, hype_Yes, hdis_Yes, mar_Yes, Never_worked,Private, Self_employed, children, Urban, Never_Smoked, Unknown, smokes]])
        
        my_prediction = model.predict(data)

        #output=round(prediction[0],2)

        return render_template('result.html', prediction = my_prediction)


  #  return render_template("home.html")




if __name__ == "__main__":
    app.run(debug=True)
