from flask import Flask, request, jsonify, render_template

import joblib

app = Flask(__name__)


model = joblib.load("iris_model.joblib")

@app.route("/predict", methods=["POST"])
def predict():
    data = request.get_json()
    
    features = [[
        data["SepalLengthCm"],
        data["SepalWidthCm"],
        data["PetalLengthCm"],
        data["PetalWidthCm"]
    ]]
    
    prediction = model.predict(features)
    
    return jsonify({"prediction": prediction[0]})

if __name__ == "__main__":
    app.run(debug=True)