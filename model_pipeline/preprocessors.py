"""
@author: kb
"""

import config
import data_management
import category_encoders as ce

def get_features_and_target():
    heart_df = data_management.load_dataset()
    X = heart_df[config.FEATURES]
    y = heart_df[config.TARGET]
    return X, y


def categoricalEncoder():
    ce.one_hot.OneHotEncoder(cols=config.CATEGORICAL_FEATURES)




