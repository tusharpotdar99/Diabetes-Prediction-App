from flask import Flask, request, render_template
import pickle
import numpy as np
import xgboost

app = Flask(__name__)


# Load the trained machine learning model
with open('model/model_diabetes.pkl', 'rb') as model_file:
    model = pickle.load(model_file)

normal_ranges = {
    'fasting_blood_glucose': (126, 200),
    'postprandial_blood_glucose': (200, 250),
    'hba1c': (6.5, 10.0),
    'random_blood_glucose': (200, 300),
    'bmi': (30, 40),
    'waist_circumference': (35, 50),  # Varies with gender
    'triglyceride_levels': (150, 300),
    'blood_pressure_systolic': (140, 180),
    'blood_pressure_diastolic': (90, 120),
    'ldl_cholesterol': (100, 200),
    'hdl_cholesterol': (60, 100),
    'crp_levels': (3.0, 10.0),
    'insulin_levels': (25, 50),
    'homa_ir': (2.9, 5.0),
    'ogtt': (200, 300),
    'creatinine_levels': (1.2, 2.0),
    'egfr': (60, 120),
    'microalbuminuria': (30, 300),
    'uric_acid_levels': (7.2, 10),
    'fructosamine_levels': (285, 400),
    'alt': (56, 100),
    'ast': (40, 80),
    'c_peptide': (2.0, 5.0),
    'proinsulin_levels': (10, 20),
}

@app.route('/')
def home():
    return  render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    # Extract data from form
    form_data = request.form
    data = [
        float(form_data['fasting_blood_glucose']),
        float(form_data['postprandial_blood_glucose']),
        float(form_data['hba1c']),
        float(form_data['random_blood_glucose']),
        float(form_data['bmi']),
        float(form_data['waist_circumference']),
        float(form_data['triglyceride_levels']),
        float(form_data['blood_pressure_systolic']),  # Systolic
        float(form_data['blood_pressure_diastolic']),  # Diastolic
        float(form_data['ldl_cholesterol']),
        float(form_data['hdl_cholesterol']),
        float(form_data['crp_levels']),
        float(form_data['insulin_levels']),
        float(form_data['homa_ir']),
        float(form_data['ogtt']),
        float(form_data['creatinine_levels']),
        float(form_data['egfr']),
        float(form_data['microalbuminuria']),
        float(form_data['uric_acid_levels']),
        float(form_data['fructosamine_levels']),
        float(form_data['alt']),
        float(form_data['ast']),
        float(form_data['c_peptide']),
        float(form_data['proinsulin_levels']),
        1 if form_data['family_history_of_diabetes'] == 'Yes' else 0,
        1 if form_data['gestational_diabetes'] == 'Yes' else 0,
        1 if form_data['pcos'] == 'Yes' else 0,
        1 if form_data['hypertension'] == 'Yes' else 0,
        1 if form_data['physical_activity'] == 'Yes' else 0,
        1 if form_data['smoking'] == 'Yes' else 0,
        1 if form_data['alcohol_consumption'] == 'Yes' else 0,
        1 if form_data['obesity'] == 'Yes' else 0,
        1 if form_data['diet'] == 'Yes' else 0,
        1 if form_data['sleep_apnea'] == 'Yes' else 0
    ]


    # Convert data to numpy array and reshape for prediction
    data = np.array(data).reshape(1, -1)

    # Make prediction
    risk_factor = model.predict_proba(data)[:,1][0]
    prediction = model.predict(data)
    # print(prediction)
    # Map prediction to output

    output = 'Positive for diabetes' if prediction[0] == 1 else 'Negative for diabetes'
    feature_status = {}
    for feature, value in form_data.items():
        if feature in normal_ranges:
            min_val, max_val = normal_ranges[feature]
            feature_status[feature] = {
                'value': float(value),
                'status': 'out_of_range' if min_val <= float(value) <= max_val else 'normal'
            }
        else:
            feature_status[feature] = {'value': value, 'status': 'normal'}

    return render_template('report.html',data=feature_status,predict_prob=risk_factor, prediction_text=output)

if __name__ == "__main__":
    app.run(debug=True)
