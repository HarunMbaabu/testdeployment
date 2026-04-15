import joblib
import numpy as np
from flask import Flask, render_template, request

app = Flask(__name__)


model = joblib.load("iris_model.joblib")

class_names = ["setosa", "versicolor", "virginica"]


@app.route("/", methods=["GET"])
def index():
    return render_template("index.html")


@app.route("/predict", methods=["POST", "GET"])
def predict():
    try:
        sepal_length = float(request.form["sepal_length"])
        sepal_width = float(request.form["sepal_width"])
        petal_length = float(request.form["petal_length"])
        petal_width = float(request.form["petal_width"])

        features = [[sepal_length, sepal_width, petal_length, petal_width]]
        features_array = np.array(features)

        prediction = model.predict(features_array)[0]

        if isinstance(prediction, (int, np.integer)) and prediction < len(class_names):
            prediction_label = class_names[prediction]
        else:
            prediction_label = str(prediction)

        return render_template("predict.html", prediction_text=f"Prediction: {prediction_label}")

    except Exception as e:
        return render_template("predict.html", prediction_text=f"Error: {str(e)}")


if __name__ == "__main__":
    app.run(debug=True)