"""
@author: kb
"""



import pipeline
import preprocessors as pp
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score




X, y = pp.get_features_and_target()

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, stratify=y ,random_state=123)

pipeline.my_pipeline.fit(X_train, y_train)

test_pred = pipeline.my_pipeline.predict(X_test)

print('The accuracy of prediction is:', accuracy_score(y_test, test_pred))

