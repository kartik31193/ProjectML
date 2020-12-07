from flask import Flask, request, render_template, jsonify
import pandas as pd
import pickle

app = Flask(__name__)

model = pickle.load(open("model.pkl", 'rb'))
x = open("model_columns.pkl", "rb")
model_columns = pickle.load(x)


@app.route('/')
def home():
    return render_template("home.html")


@app.route('/predict', methods=['POST'])
def predict():
    data = request.form
    features = pd.get_dummies(pd.DataFrame([data]))
    test = features.reindex(columns=model_columns, fill_value=0)
    prediction = model.predict(test)

    prediction = int(prediction[0])
    if prediction == 1:
        return render_template('home.html', pred='You Have Heart Disease - prediction value is {}'.format(prediction))
    else:
        return render_template('home.html', pred='You Don\'t Have Heart Disease - prediction value is {}'.format(prediction))


@app.route('/predict_api', methods=['POST'])
def predict_api():
    data = request.get_json(force=True)
    data_unseen = pd.DataFrame([data])
    prediction = model.predict(data_unseen)
    output = int(prediction[0])
    return jsonify(output)


if __name__ == '__main__':
    app.run(debug=True)
