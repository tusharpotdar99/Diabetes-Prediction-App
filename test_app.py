import unittest
from flask import Flask, request, render_template
import pickle
import numpy as np
import xgboost

from main import app

class FlaskTestCase(unittest.TestCase):
    def setUp(self):
        # Create a test client
        self.app = app.test_client()
        self.app.testing = True

    def test_home(self):
        # Test the home page
        result = self.app.get('/')
        self.assertEqual(result.status_code, 200)
        self.assertIn(b'Welcome to the Diabetes Prediction App', result.data)

    def test_predict(self):
        # Test the prediction functionality
        form_data = {
            'fasting_blood_glucose': 120,
            'postprandial_blood_glucose': 150,
            'hba1c': 5.5,
            'random_blood_glucose': 160,
            'bmi': 25,
            'waist_circumference': 35,
            'triglyceride_levels': 100,
            'blood_pressure': '120/80',
            'ldl_cholesterol': 90,
            'hdl_cholesterol': 50,
            'crp_levels': 2.0,
            'insulin_levels': 10,
            'homa_ir': 1.5,
            'ogtt': 140,
            'creatinine_levels': 1.0,
            'egfr': 90,
            'microalbuminuria': 20,
            'uric_acid_levels': 5,
            'fructosamine_levels': 250,
            'alt': 30,
            'ast': 20,
            'c_peptide': 1.0,
            'proinsulin_levels': 5,
            'family_history_of_diabetes': 'No',
            'gestational_diabetes': 'No',
            'pcos': 'No',
            'hypertension': 'No',
            'physical_activity': 'Yes',
            'smoking': 'No',
            'alcohol_consumption': 'No',
            'obesity': 'No',
            'diet': 'No',
            'sleep_apnea': 'No'
        }
        result = self.app.post('/predict', data=form_data)
        self.assertEqual(result.status_code, 200)
        self.assertIn(b'Result:', result.data)

if __name__ == '__main__':
    unittest.main()
