from flask import Flask, jsonify, request
from data import  get_prediction

app = Flask(__name__)

@app.route("/predict-data", methods=["POST"])
def predict_data():
  # image = cv2.imdecode(np.fromstring(request.files.get("digit").read(), np.uint8), cv2.IMREAD_UNCHANGED)
  image = request.files.get("alphabet")
  prediction = get_prediction(image)
  return jsonify({
    "prediction": prediction
  })

if __name__ == "__main__":
  app.run(debug=True)