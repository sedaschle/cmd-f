from flask import Flask, render_template, request, url_for, redirect, session
from datetime import datetime
from .cohereTemp import sentiment_analysis, topic_analysis, summarize, resultData
import praw

app = Flask(__name__)
app.secret_key = 'BAD_SECRET_KEY'


@app.route('/', methods=['GET', 'POST'])
def index():
    a = ["The cgi is shit", "this coffee is cold", "the story is ok"]
    topic_analysis(a)
    return render_template('index.html')


@app.route("/result")
def result():
    if request.method == 'POST':
        title = request.form.get("title")
        subreddit = request.form.get("subreddit")

        data = praw.scrape_reddit(title, subreddit)

        if data is None:
            # TODO: send error message to front end
            return Error

        result = resultData(data)

        # TODO: pass to frontend and test
        return render_template('result.html', dataToRender=result)

    return redirect(url_for('index'))


@app.route("/about")
def about():
    return render_template('about.html')
