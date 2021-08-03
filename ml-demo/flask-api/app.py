from flask import Flask, jsonify, render_template, request

import ml

app = Flask(__name__)

# 템플릿 자동 리로딩
# app.config['TEMPLATES_AUTO_RELOAD'] = True


@app.route("/predict", methods=["POST"])
def predict():
    expected = {}
    for name, f in request.files.items():
        expected_number = ml.predict(f)
        expected[name] = expected_number
    return jsonify(expected)
