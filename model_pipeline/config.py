"""
@author: kb
"""


DATAURL = 'http://archive.ics.uci.edu/ml/machine-learning-databases/heart-disease/processed.cleveland.data'

COL_NAMES = ['age', 'sex', 'chest_pain_type', 'resting_blood_pressure', 'cholesterol', 'fasting_blood_sugar', 'rest_ecg', 'max_heart_rate_achieved','exercise_induced_angina', 'st_depression', 'st_slope', 'num_major_vessels', 'thalassemia', 'num']

TARGET = 'diagnosed'

FEATURES = ['age', 'sex', 'chest_pain_type', 'resting_blood_pressure',
       'cholesterol', 'fasting_blood_sugar', 'rest_ecg',
       'max_heart_rate_achieved', 'exercise_induced_angina', 'st_depression',
       'st_slope', 'num_major_vessels', 'thalassemia']


CATEGORICAL_FEATURES = ['sex', 'chest_pain_type', 'fasting_blood_sugar', 'rest_ecg',
                        'exercise_induced_angina', 'st_slope', 'num_major_vessels', 'thalassemia']

