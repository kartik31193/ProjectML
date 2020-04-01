"""
@author: kb
"""

import xgboost as xgb


# optimized model parameters
xgb_params={'colsample_bytree': 0.6423716721494608,
 'gamma': 4.640448122287516,
 'learning_rate': 0.33851466059837393,
 'max_depth': 1,
 'min_child_weight': 3,
 'n_estimators': 802,
 'reg_alpha': 2.8379661620427266,
 'reg_lambda': 0.5797836880329088,
 'subsample': 0.7032759078465736}


def get_optimized_model():
    model = xgb.XGBClassifier(**xgb_params)
    return model