import json
from flask import Flask, render_template, request, url_for, redirect, session
from datetime import datetime
from .cohereTemp import sentiment_analysis, topic_analysis, summarize, resultData
from .reddit_scrape import search_comments

app = Flask(__name__)
app.secret_key = 'BAD_SECRET_KEY'

@app.route('/',methods=['GET','POST'])
def index():   
    return render_template('index.html')


@app.route("/result")
def result():
    error = None
    if request.method == 'POST':
        title = request.form.get("title")
        subreddit = request.form.get("subreddit")

        data = praw.scrape_reddit(title, subreddit)

        if data is None:
            error = 'Error: Subreddit could not be found.'

        result = resultData(data)
        return render_template('result.html', dataToRender=result, error=error)

    return redirect(url_for('index'))


@app.route("/about")
def about():
    return render_template('about.html')



