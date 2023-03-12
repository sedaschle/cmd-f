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
    if request.method == 'POST':
        title = request.form.get("title")
        subreddit = request.form.get("subreddit")

        data = praw.scrape_reddit(title, subreddit)

        if data is None:
            # TODO: send error message to front end
            return Error

        result = resultData(data)
        return render_template('result.html', dataToRender=result)

    return redirect(url_for('index'))


@app.route("/about")
def about():
    return render_template('about.html')



