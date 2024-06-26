from flask import Flask, jsonify, request
# from utilities import predict_pipeline

app = Flask(__name__)

@app.post("/predict")
def predict():
    data = request.json
    try:
        sample = data['text']
    except KeyError:
        return jsonify({'error': 'No text was sent.'})

    # sample = [sample]
    # predictions = predict_pipeline(sample)
    # try:
    #     result = predictions[0]
    # except TypeError as e:
    #     result = jsonify({'error': str(e)})
    
    # return result
    return "We have received your text..."


if  __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)
