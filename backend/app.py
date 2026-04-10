from flask import Flask, request, jsonify
import joblib
import numpy as np
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

model = joblib.load("model.pkl")

@app.route("/predict", methods=["POST"])
def predict():
    print("API HIT")   # 👈 ADD THIS
    
    data = request.json

    features = np.array([[
        float(data['study_hours']),
        float(data['sleep_hours']),
        float(data['play_hours']),
        float(data['attendance'])
    ]])

    prediction = model.predict(features)[0]

    if prediction > 75:
        status = "SAFE"
    elif prediction > 50:
        status = "WARNING"
    else:
        status = "AT RISK"
        # Suggestions
    if prediction < 50:
        suggestion = "Increase study hours, reduce distractions, and improve attendance."
    elif prediction < 75:
        suggestion = "Focus more on weak subjects and maintain consistency."
    else:
        suggestion = "Excellent performance! Keep it up."

    return jsonify({
        "prediction": prediction,
        "status": status,
        "suggestion": suggestion,
        "input": data,
        "distribution": [70,20,10]
    })

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)