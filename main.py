import numpy as np
import pandas as pd
import pickle
from sklearn.preprocessing import LabelEncoder
from flask import Flask, request, jsonify, render_template
from Mapping.file import (race_mapping, dwelling_mapping, dwelling_type_mapping, province_code_mapping, metro_code_mapping, nationality_mapping, RTH_mapping,
                        marital_st_mapping, Lang_inside_mapping, Lang_outside_mapping, Education_mapping, lw_work_mapping, lw_business_mapping, 
                        help_on_household_mapping, job_or_business_mapping, nature_of_work_mapping  ) 

# Instantiat Flask App
app = Flask(__name__, template_folder= "templates")

#Call in model
model = pickle.load(open('new_model.pkl', 'rb'))

le= LabelEncoder()


#Create the home route
@app.route('/', methods=['GET', 'POST'])
def home():
    return render_template('home.html')

#Create the predition route
@app.route('/predict', methods=['GET', 'POST'])
def predict():
    #Get input from webservice
    try:
        age= request.form.get('age')

        nature_of_work= request.form.get('nature_of_work')
        nature_of_work= nature_of_work_mapping.get(nature_of_work)

        psu= request.form.get('psu')

        Race= request.form.get('Race')
        Race= race_mapping.get(Race)

        Dwelling= request.form.get('Dwelling')
        Dwelling= dwelling_mapping.get(Dwelling)

        dwelling_type= request.form.get('dwelling_type')
        dwelling_type= dwelling_type_mapping.get(dwelling_type)

        province_code= request.form.get('province_code')
        province_code= province_code_mapping.get(province_code)

        metro_code= request.form.get('metro_code')
        metro_code= metro_code_mapping.get(metro_code)

        nationality= request.form.get('nationality')
        nationality= nationality_mapping.get(nationality)

        RTH= request.form.get('RTH')
        RTH= RTH_mapping.get(RTH)

        marital_st= request.form.get('marital_st')
        marital_st= marital_st_mapping.get(marital_st)
        print(marital_st)

        Lang_inside= request.form.get('Lang_inside')
        Lang_inside= Lang_inside_mapping.get(Lang_inside)

        Lang_outside= request.form.get('Lang_outside')
        Lang_outside= Lang_outside_mapping.get(Lang_outside)

        Education= request.form.get('Education')
        Education= Education_mapping.get(Education)

        lw_work= request.form.get('lw_work')
        lw_work= lw_work_mapping.get(lw_work)

        lw_business= request.form.get('lw_business')
        lw_business= lw_business_mapping.get(lw_business)

        help_on_household= request.form.get('help_on_household')
        help_on_household= help_on_household_mapping.get(help_on_household)

        job_or_business= request.form.get('job_or_business')
        job_or_business= job_or_business_mapping.get(job_or_business)

        result= [age, nature_of_work, psu, Race, Dwelling, dwelling_type, province_code, metro_code, nationality, RTH,
        marital_st, Lang_inside, Lang_outside, Education, lw_business, lw_work, help_on_household, job_or_business]
        print(result)

        #Get prediction from model
        final_features = [np.array(result)]
        prediction = model.predict(final_features)


        final = round(prediction[0], 2)
        print(final)

        return render_template('home.html', prediction_text='The result is {}'.format(final))

    except ValueError as e:
        return str(e)
#Instantiate the local host
if __name__ == "__main__":
    app.run(debug=True)
