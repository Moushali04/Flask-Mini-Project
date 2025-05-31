from flask import Flask, render_template, request
from sentimental import get_sentiment
from sqlite import SentimentLog, Session

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    sentiment = None
    score = None

    if request.method == 'POST':
        text = request.form['text']
        sentiment, score = get_sentiment(text)

        # Save to database
        session = Session()
        log = SentimentLog(text=text, sentiment=sentiment, score=score)
        session.add(log)
        session.commit()
        session.close()

    return render_template('index.html', sentiment=sentiment, score=score)

if __name__ == '__main__':
    app.run(debug=True)
