from flask import Flask, request, render_template, jsonify
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

app = Flask(__name__)
analyzer = SentimentIntensityAnalyzer()

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/analyze', methods=['POST'])
def analyze():
    text = request.form.get('text', '')
    sentiment = analyzer.polarity_scores(text)
    return jsonify(sentiment)

if __name__ == '__main__':
    app.run(debug=True)
