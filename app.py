from flask import Flask, render_template, request
from transformers import pipeline

app = Flask(__name__)
classifier = pipeline("text-classification", model="nateraw/bert-base-uncased-emotion")

@app.route("/", methods=["GET"])
def homepage():
    return render_template("index.html")

@app.route("/detect", methods=["POST"])
def detect_emotion():
    if request.method == "POST":
        user_input = request.form.get("text")
        if user_input:
            result = classifier(user_input)[0]
            label = result['label']
            score = round(result['score'], 2)
            return render_template("index.html", emotion=label, score=score, user_input=user_input)
        else:
            return render_template("index.html", error="Please enter some text to analyze.")
    return render_template("index.html")

@app.route("/demo", methods=["GET"])
def demo_page():
    return render_template("demo.html")

if __name__ == "__main__":
    app.run(debug=True)